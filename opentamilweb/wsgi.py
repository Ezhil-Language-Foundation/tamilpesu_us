"""
WSGI config for opentamilweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
import sys
sys.path.insert(0,'/var/www/opentamil')
import os
import django
from django.conf import settings
os.environ["DJANGO_SETTINGS_MODULE"] = "opentamilweb.settings"
from opentamilweb import settings as ot_settings 
#settings.configure(ot_settings,DEBUG=False)
#django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
