#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 26/08/2020 10:21.

from pathlib import Path
from frontend.icons import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#h&#*+%u34e_e&3ryjifv8y)&m)t#tia09ejqdvyv(7x_c3+5g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '192.168.0.103']

# GENERAL
VERSION = "1.0.0"
NAME_OF_ENTERPRISE = "Atêlie Leya Monteiro"
CRISPY_TEMPLATE_PACK = 'bootstrap4'
AUTH_USER_MODEL = 'users.CustomUser'
DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

# Status Payment
STATUS_PAYMENT_SUCCESS = 2
STATUS_PAYMENT_DEFAULT = 1
# Status Service
STATUS_SERVICE_FINISHED = 1

# Icons
ICON_CONFIRMED = f"<span class='badge bg-success'>{ICON_CHECK} Sim</span>"
ICON_NOT_CONFIRMED = f"<span class='badge bg-warning'>{ICON_TRIANGLE_ALERT} Não </span>"
ICON_FINISHED = f"<span class='badge bg-success'>{ICON_DOUBLE_CHECK} Sim</span>"
ICON_NOT_FINISHED = f"<span class='badge bg-warning'>{ICON_TRIANGLE_ALERT} Não</span>"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'simple_history',
    'bootstrap4',
    'crispy_forms',
    'django_tables2',
    'django_filters',
    'users',
    'frontend',
    'base',
    'config',
    'service',
    'financial',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'simple_history.middleware.HistoryRequestMiddleware',
    'base.middleware.BaseMiddleware',
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

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Login redirect
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = '/'
