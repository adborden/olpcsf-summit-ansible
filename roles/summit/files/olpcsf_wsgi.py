import os
import sys

sys.path.append('/home/summit/app/env/lib/python2.7/site-packages/django')
sys.path.append('/home/summit/app')
sys.path.append('/home/summit/app/summit')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'summit.olpcsf_settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
