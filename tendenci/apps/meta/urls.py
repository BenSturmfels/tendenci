from django.conf.urls import patterns, url
from .views import add_custom_meta_data, show_custom_meta_data, edit_custom_meta_data, \
    delete_custom_meta_data


urlpatterns = [
    url(r'^custom/?$', show_custom_meta_data, name="show_custom_meta_data"),
    url(r'^custom/add/$', add_custom_meta_data, name="add_custom_meta_data"),
    url(r'^custom/edit/(?P<metadata_id>\d+)/$', edit_custom_meta_data, name="edit_custom_meta_data"),
    url(r'^custom/delete/(?P<metadata_id>\d+)/$', delete_custom_meta_data, name="delete_custom_meta_data")
]
