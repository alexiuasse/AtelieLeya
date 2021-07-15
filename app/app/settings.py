#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/11/2020 08:42.
import os
from pathlib import Path

from frontend.icons import *
from google.oauth2 import service_account

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#h&#*+%u34e_e&3ryjifv8y)&m)t#tia09ejqdvyv(7x_c3+5g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if os.getenv('GAE_APPLICATION', None):
    ALLOWED_HOSTS = ['localhost', 'www.leyamonteiro.com']
else:
    ALLOWED_HOSTS = ['localhost', '0.0.0.0', '192.168.0.103']

# GENERAL
# #FF63C7
VERSION = "1.0.0"
NAME_OF_ENTERPRISE = "NAME_OF_ENTERPRISE"
NAME_OF_ENTERPRISE_SHORT = "NAME_OF_ENTERPRISE_SHORT"
CRISPY_TEMPLATE_PACK = 'bootstrap4'
DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

# Status Payment
STATUS_PAYMENT_DEFAULT = 1
STATUS_PAYMENT_SUCCESS = 2
# Status Service
STATUS_SERVICE_DEFAULT = 1
STATUS_SERVICE_FINISHED = 2

# Icons
ICON_CONFIRMED = f"<span class='badge bg-success'>{ICON_CHECK} Sim</span>"
ICON_NOT_CONFIRMED = f"<span class='badge bg-warning'>{ICON_TRIANGLE_ALERT} Não </span>"
ICON_FINISHED = f"<span class='badge bg-success'>{ICON_DOUBLE_CHECK} Sim</span>"
ICON_NOT_FINISHED = f"<span class='badge bg-warning'>{ICON_TRIANGLE_ALERT} Não</span>"

# Slot of time, used to tell the slices of time
SLICE_OF_TIME = 30  # min

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_cleanup.apps.CleanupConfig',
    'corsheaders',
    'simple_history',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'bootstrap4',
    'crispy_forms',
    'django_tables2',
    'django_filters',
    'users',
    'frontend',
    'config',
    'service',
    'financial',
    'business',
    'homepage',
]

SITE_ID = 1
# CORS Config
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'METHOD': 'js_sdk',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            # 'gender',
            'updated_time',
        ],
        'LOCALE_FUNC': lambda request: 'pt_BR',
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': False,
        'VERSION': 'v8.0',
    }
}

# facebook
SOCIAL_AUTH_FACEBOOK_KEY = 'YOUR_FACEBOOK_KEY'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'YOUR_FACEBOOK_KEY_AUTH'  # app key

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'simple_history.middleware.HistoryRequestMiddleware',
    # 'base.middleware.BaseMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'frontend.context_processors.frontend_template_context',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3308',
        'NAME': 'db',
        'USER': 'admin-leya',
        'PASSWORD': '$enhadeMerda123',
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'atelie-leya-monteiro-bucket-static'
GS_DEFAULT_ACL = 'publicRead'
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    "YOUR_FILE_CREDENTIALS.json"
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Login redirect
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = '/'

# Social Allauth
ACCOUNT_EMAIL_VERIFICATION = 'none'
