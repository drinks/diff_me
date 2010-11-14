from django.conf.urls.defaults import *

urlpatterns = patterns('diff_me.main.views',
    # Example:
    # (r'^diff_me/', include('diff_me.foo.urls')),
    (r'^$', 'index'),
    (r'^diff/(?P<id>[\s\d-_])/$', show_by_slug_or_base58)
)
