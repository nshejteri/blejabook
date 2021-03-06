"""
Django settings for blejabook project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w)@#(yt!kecsymjk6c6--&nfvh420t*_j99i2$^tgv&jslt6_&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'main_app',
    'userprofile',
    'userauth',
    'private_messages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'userprofile.onlineusers.OnlineNowUsersMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request', 
)

ROOT_URLCONF = 'blejabook.urls'

WSGI_APPLICATION = 'blejabook.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = None

USE_I18N = True

USE_L10N = False

USE_TZ = False

DATE_FORMAT = 'd m Y'

DATE_INPUT_FORMATS = ('%d/%m/%Y', '%Y-%m-%d',)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
"""
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "media/static")

STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    STATIC_PATH,    
)"""


STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('assets', os.path.join(BASE_DIR, "static")),
)

TEMPLATE_MAIN_PATH = os.path.join(BASE_DIR, 'main_app/templates')
TEMPLATE_PROFILE_PATH = os.path.join(BASE_DIR, 'userprofile/templates')
TEMPLATE_AUTH_PATH = os.path.join(BASE_DIR, 'userauth/templates')
TEMPLATE_MESSAGES_PATH = os.path.join(BASE_DIR, 'messages/templates')

TEMPLATE_DIRS = [
    TEMPLATE_MAIN_PATH,
    TEMPLATE_PROFILE_PATH,
    TEMPLATE_AUTH_PATH,
    TEMPLATE_MESSAGES_PATH,
]

#AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'karrapandza@gmail.com'
DEFAULT_HTTP_PROTOCOL = 'http'

SITE_ID = 1

LOGIN_URL = 'index'

# Interval od 20min za koji se korisnik smatra 'Online'. Ako se zakomentarise ova konstanta
# default vrednost je 15min
#ONLINE_TIMEOUT = 60 * 20


#SESSION_COOKIE_AGE = 60 * 60
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
