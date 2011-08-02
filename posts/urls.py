from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('posts.views',
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>.*)', 'show_post'),
	url(r'^archive', 'archive'),
    url(r'^$', 'index'),
)