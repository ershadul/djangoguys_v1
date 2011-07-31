#!/user/bin/python

import os, sys

sys.path.append('/var/www/djangoguys')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
