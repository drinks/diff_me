from django.conf.urls.defaults import *

urlpatterns = patterns('diff_me.main.views',
    # Example:
    # (r'^diff_me/', include('diff_me.foo.urls')),
    url(r'^$', 'index', name="home"),
    url(r'^new/$', 'create', name="create"),
    url(r'^diff/(?P<base58>[-\w]{1,})/edit/$', 'edit', name="edit"),
    url(r'^diff/(?P<base58>[-\w]{1,})/$', 'diff_html', name="diff_html"),
    url(r'^diff/(?P<base58>[-\w]{1,}).(?P<type>(txt|diff))$', 'diff_raw', name="diff_raw"),
)
