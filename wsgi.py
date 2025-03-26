import os
from django.core.wsgi import get_wsgi_application

# Replace with your project name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ideathon_sym.settings')

application = get_wsgi_application()



