from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('tags.views',
    url(r'^tag/(?P<slug>.*)', 'show_tag'),
    url(r'^$', 'index'),
)