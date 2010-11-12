from django.conf.urls.defaults import *

urlpatterns = patterns('diff_me.main.views',
    # Example:
    # (r'^diff_me/', include('diff_me.foo.urls')),
    (r'^$', 'index'),
)
