
import dj_database_url
from culture.settings import *
# DEBUG=False
# TEMPLATE_DEBUG=False
ALLOWED_HOSTS = [
    "cameroon-culture.herokuapp.com",
    "127.0.0.1",
]

SECRET_KEY = '*&zegul5y2+ho#w#2=xl3!)&1zhz5d$u8#%8o*a8q^=-1agf50'
DATABASES["default"] = dj_database_url.config()

PRE_MIDDLEWARE = MIDDLEWARE
MIDDLEWARE = [
    PRE_MIDDLEWARE[0],
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
MIDDLEWARE.extend(PRE_MIDDLEWARE[2:])


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
