"""
Django settings for warwick_gg project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os

import stripe

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'seating',
    'dashboard',
    'events',
    'avatar',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'uwcs_auth',

    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',

    'djangobower',
    'compressor',
    'svg',
    'markdown_deux',
    'anymail',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'warwick_gg.urls'

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
            os.path.join(PROJECT_DIR, 'templates', 'allauth'),
            os.path.join(BASE_DIR, 'media', 'seating')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'dashboard.context_processors.has_launched',
            ],
        },
    },
]

# Allauth config
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

ACCOUNT_SIGNUP_FORM_CLASS = 'uwcs_auth.forms.SignupForm'

ACCOUNT_ADAPTER = 'uwcs_auth.adapter.WarwickGGUserAccountAdapter'
SOCIALACCOUNT_ADAPTER = 'uwcs_auth.adapter.UWCSUserAccountAdapter'

LOGIN_REDIRECT_URL = '/dashboard/'

WSGI_APPLICATION = 'warwick_gg.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Django Compressor
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_PATH, "../components")
COMPRESS_PRECOMPILERS = (
    ('text/x-scss',
     'sass --style compressed -I "%s/bower_components/bulma" "{infile}" "{outfile}"' % BOWER_COMPONENTS_ROOT),
)

# Django-bower
BOWER_INSTALLED_APPS = [
    'bulma~0.6.2',
]

# Django-avatar
AVATAR_AUTO_GENERATE_SIZES = (80, 64, 128, 256)
AVATAR_CLEANUP_DELETED = True
AVATAR_GRAVATAR_DEFAULT = 'identicon'
AVATAR_EXPOSE_USERNAMES = False
AVATAR_MAX_AVATARS_PER_USER = 1

# In-development sign in switch
HAS_LAUNCHED = True

# Anymail config
EMAIL_BACKEND = 'anymail.backends.sendgrid.EmailBackend'
EMAIL_ABS_URL = 'https://warwick.gg'
DEFAULT_FROM_EMAIL = 'accounts@warwick.gg'
ANYMAIL = {
    'SENDGRID_API_KEY': os.environ.get('SENDGRID_API_KEY')
}

# Warwick SU API keys
UWCS_API_KEY = os.environ.get('UWCS_API_KEY')
ESPORTS_API_KEY = os.environ.get('ESPORTS_API_KEY')

# Stripe API keys
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
STRIPE_PRIVATE_KEY = os.environ.get('STRIPE_PRIVATE_KEY')

stripe.api_key = STRIPE_PRIVATE_KEY
