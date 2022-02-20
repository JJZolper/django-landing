from config.settings import *

import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS', '*')]

DATABASES['default'] = dj_database_url.config(conn_max_age=600)

# GEO IP / Maxmind
GEOIP_PATH=os.environ['GEOIP_GEOLITE2_PATH']
GEOIP_CITY=os.environ['GEOIP_GEOLITE2_CITY_FILENAME']
GEOIP_COUNTRY=os.environ['GEOIP_GEOLITE2_COUNTRY_FILENAME']

MAXMIND_LICENSE_KEY=os.environ['MAXMIND_LICENSE_KEY']

# Google Analytics
GOOGLE_ANALYTICS_ID = os.getenv('GOOGLE_ANALYTICS_ID')