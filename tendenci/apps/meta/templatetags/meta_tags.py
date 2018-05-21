import re
from django.db.models import ForeignKey, TextField
from django.core.cache import cache
from django.template import Library

from BeautifulSoup import BeautifulSoup
from tendenci.libs.tinymce.models import HTMLField

from tendenci.apps.files.models import File
from tendenci.apps.site_settings.utils import get_setting
from tendenci.apps.meta.models import CustomMeta


register = Library()


@register.inclusion_tag("meta/og_image.html")
def meta_og_image(obj, field_name):
    base_url = get_setting('site', 'global', 'siteurl')
    keys = [u"meta_og_image", obj._meta.app_label, str(obj.id),
            field_name, obj.update_dt.strftime('%m%d%Y%H%M%S')]
    cache_key = "_".join(keys)
    cached_value = cache.get(cache_key)
    if cached_value:
        return cached_value

    try:
        field = obj._meta.get_field_by_name(field_name)[0]
        image_list = []

        if isinstance(field, HTMLField) or isinstance(field, TextField):
            content = getattr(obj, field_name)
            soup = BeautifulSoup(content)
            for image in soup.findAll("img"):
                image_url = base_url + image["src"]
                image_list.append(image_url)

        elif isinstance(field, ForeignKey):
            image = getattr(obj, field_name)
            if isinstance(image, File):
                image_list.append(base_url + image.get_absolute_url())

        value = {'urls': image_list}
        cache.set(cache_key, value)
        return value
    except Exception:
        return {}


@register.filter(name='contains_custom_meta')
def contains_custom_meta(page_path, key_to_return=None):
    path = re.sub(r'(?<=\/)(\d+)(?=\/)', '#', page_path)
    try:
        meta_data_object = CustomMeta.objects.get(page_path=path)
        if key_to_return:
            return {"title": meta_data_object.title, "keywords": meta_data_object.keywords,
                    "description": meta_data_object.description,
                    "canonical_url": meta_data_object.canonical_url}.get(key_to_return)
        else:
            return {"title": meta_data_object.title, "keywords": meta_data_object.keywords,
                    "description": meta_data_object.description, "canonical_url": meta_data_object.canonical_url}
    except CustomMeta.DoesNotExist:
        return False