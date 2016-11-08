from django.utils.translation import ugettext_lazy as _


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'camomilla4',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
    }
}

LANGUAGE_CODE = 'it'

LANGUAGES = (
    ('it', _('Italian')),
    ('en', _("English")),
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'abe1z$e@ii490wzee=-%s(dh-2o5y3(wgj7sl6)0wiyb0k6-4i'
