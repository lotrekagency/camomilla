from django.utils.translation import ugettext_lazy as _


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
    ('en-us', _("US English")),
    ('it', _('Italian')),
    ('nl', _('Dutch')),
    ('fr', _('French')),
    ('es', _('Spanish')),
)

ADMIN_SITE_HEADER = _("Camomilla advanced panel")
