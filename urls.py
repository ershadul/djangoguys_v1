from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoguys.views.home', name='home'),
    # url(r'^djangoguys/', include('djangoguys.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tags/', include('tags.urls')),
    url(r'^', include('posts.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
   ) + urlpatterns