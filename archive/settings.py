"""
Django settings for archive project.

"""

import os

from django.utils.log import DEFAULT_LOGGING  # for pretty development logs
import sys  # for use in DEFAULT_LOGGING

from dotenv import load_dotenv  # handles development environment variables

import django_heroku  # handles heroku settings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Uses python-dotenv to import dev environment variables.
# See `sample-env` file in root for details on how to make your own .env file.

env_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=env_path)

# Load SECRET_KEY from environment variable
SECRET_KEY = os.environ.get('SECRET_KEY')


# Turns on debugging in development environment.
# To set your heroku app's DEBUG variable as false, run:
# `heroku config:set DEBUG=False
# Or set it at https://dashboard.heroku.com/apps/your-app-name/settings

DEBUG = os.environ.get('DEBUG', True)


# Logging

DEFAULT_LOGGING['handlers']['console']['filters'] = []

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'stream': sys.stdout
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', ],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}


# Development-specific settings for allowed hosts

ALLOWED_HOSTS = ['testserver', 'localhost', '127.0.0.1', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Registering the Fanarchive app
    'fanarchive.apps.FanarchiveConfig',
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

ROOT_URLCONF = 'archive.urls'

TEMPLATES = [
    # Django template engine's default settings
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
           ],
        },
    },
]

WSGI_APPLICATION = 'archive.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

# Importing all heroku specific settings (will not show up in dev~)

django_heroku.settings(locals())
