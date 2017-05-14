import os

from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LANGUAGE_CODE = 'it'

LANGUAGES = (
    ('it', _('Italian')),
    ('en', _('English')),
)

USER_PROFILE_MODEL = 'camomilla.UserProfile'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = []
if os.path.exists(os.path.join(BASE_DIR, 'build')):
    STATICFILES_DIRS.append(os.path.join(BASE_DIR, 'build'))
if os.path.exists(os.path.join(BASE_DIR, 'public')):
    STATICFILES_DIRS.append(os.path.join(BASE_DIR, 'public'))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

THUMB_ROOT = os.path.join(BASE_DIR, 'media', 'thumbnails')
THUMB_URL = '/media/thumbnails/'
THUMB_FOLDER = 'thumbnails'

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    )
}

from django.utils.translation import ugettext_lazy as _

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', _("English")),
    ('it', _('Italian')),
)

ADMIN_SITE_HEADER = _("Camomilla advanced panel")

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 480,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

CAMOMILLA_THUMBNAIL_WIDTH = 50
CAMOMILLA_THUMBNAIL_HEIGHT = 50

SITE_URL = 'http://localhost:8000'

PREFIX_DEFAULT_LANGUAGE = True

REDACTOR_OPTIONS = {
    'air' : True
}

REDACTOR_OPTIONS = {}
REDACTOR_UPLOAD = 'uploads/'

PNG_OPTIMIZATION_COMMAND = 'pngquant {0} -f --ext .png'
JPEG_OPTIMIZATION_COMMAND = 'jpegoptim {0}'

