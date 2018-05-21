from django import forms
from django.forms import BooleanField, CheckboxInput
from tendenci.apps.meta.models import Meta as MetaTag, CustomMeta

class MetaForm(forms.ModelForm):
    class Meta:
        model = MetaTag
        fields = (
            'title',
            'keywords',
            'description',
            'canonical_url',
        )


class CustomMetaForm(forms.ModelForm):
    class Meta:
        model = CustomMeta
        fields = ['title', 'keywords', 'description', 'canonical_url', 'page_path']


class CustomMetaConfirmDeletion(forms.Form):
    confirmation = BooleanField(widget=CheckboxInput, label="Are you sure you want to delete this metadata?",
                                required=True)
