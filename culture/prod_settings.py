
import dj_database_url
from culture.settings import *
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [
    "cameroon-culture.herokuapp.com",
    "127.0.0.1",
]

SECRET_KEY = '*&zegul5y2+ho#w#2=xl3!)&1zhz5d$u8#%8o*a8q^=-1agf50'
DATABASES["default"] = dj_database_url.config()

"""
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
"""
