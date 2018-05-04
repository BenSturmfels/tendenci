from django.conf.urls import patterns, url
from tendenci.apps.directories.feeds import LatestEntriesFeed
from tendenci.apps.site_settings.utils import get_setting
from tendenci.apps.directories.signals import init_signals

init_signals()

urlpath = get_setting('module', 'directories', 'url')
if not urlpath:
    urlpath = "directories"

urlpatterns = patterns('tendenci.apps.directories.views',
    url(r'^%s/$' % urlpath, 'search', name="directories"),
    url(r'^%s/search/$' % urlpath, 'search_redirect', name="search"),
    url(r'^%s/print-view/(?P<slug>[\w\-\/]+)/$' % urlpath, 'print_view', name="print_view"),
    url(r'^%s/add/$' % urlpath, 'add', name="add"),
    url(r'^%s/query_price/$' % urlpath, 'query_price', name="query_price"),
    url(r'^%s/edit/(?P<id>\d+)/$' % urlpath, 'edit', name="edit"),
    url(r'^%s/renew/(?P<id>\d+)/$' % urlpath, 'renew', name="renew"),
    url(r'^%s/edit/meta/(?P<id>\d+)/$' % urlpath, 'edit_meta', name="edit.meta"),
    url(r'^%s/delete/(?P<id>\d+)/$' % urlpath, 'delete', name="delete"),
    url(r'^%s/feed/$' % urlpath, LatestEntriesFeed(), name='feed'),
    url(r'^%s/logo/(?P<id>\d+)/$' % urlpath, 'logo_display', name="logo"),
    url(r'^%s/pricing/(?P<id>\d+)/$' % urlpath, 'pricing_view', name="pricing.view"),
    url(r'^%s/pricing/add/$' % urlpath, 'pricing_add', name="pricing.add"),
    url(r'^%s/pricing/edit/(?P<id>\d+)/$' % urlpath, 'pricing_edit', name="pricing.edit"),
    url(r'^%s/pricing/delete/(?P<id>\d+)/$' % urlpath, 'pricing_delete', name="pricing.delete"),
    url(r'^%s/pricing/search/$' % urlpath, 'pricing_search', name="pricing.search"),
    url(r'^%s/pending/$' % urlpath, 'pending', name="pending"),
    url(r'^%s/approve/(?P<id>\d+)/$' % urlpath, 'approve', name="approve"),
    url(r'^%s/thank-you/$' % urlpath, 'thank_you', name="thank_you"),

    # export directory
    url(r"^%s/export/$" % urlpath, "directory_export", name="export"),
    url(r"^%s/export/status/(?P<identifier>\d+)/$" % urlpath,
        "directory_export_status",
        name="export_status"),
    url(r"^%s/export/download/(?P<identifier>\d+)/$" % urlpath,
        "directory_export_download",
        name="export_download"),

    url(r'^%s/get_subcategories/$' % urlpath, 'get_subcategories', name="get_subcategories"),


    url(r'^%s/(?P<slug>[\w\-\/]+)/$' % urlpath, 'details', name="directory"),
)
