"""
Django settings for chatbot_project project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

from chatterbot.ext.django_chatterbot.settings import CHATTERBOT


import os
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^_@9296a#7jiy&g2i#so^g#+!o=afhs2=rttyy*r#zz9h+868^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'chatterbot.ext.django_chatterbot',
    'users.apps.UsersConfig',
    'todo_list.apps.TodoListConfig',
    'chatbot.apps.ChatbotConfig',
    'sentiment_analysis.apps.SentimentAnalysisConfig',
    'youtube_analysis.apps.YoutubeAnalysisConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    "crispy_bootstrap5"
]

CHATTERBOT = {
    'name' : 'Sakuuragi',
    'django_app_name' : 'django_chatterbot',
    'logic_adapters': [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    'storage_adapter' :"chatterbot.storage.SQLStorageAdapter",
    'database' : "botData.sqlite3"
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chatbot_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SETTINGS_PATH, 'templates'),
                 os.path.join(BASE_DIR, 'chatbot', 'templates', 'chatbot'),
                 os.path.join(BASE_DIR, 'users', 'templates', 'users'),
                 os.path.join(BASE_DIR, 'sentiment_analysis', 'templates', 'sentiment_analysis'),
                 os.path.join(BASE_DIR, 'todo_list', 'templates', 'todo_list')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

WSGI_APPLICATION = 'chatbot_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home-page'


# Youtube API :



# YOUTUBE_DEVELOPER_KEY = 'AIzaSyD2-CXZu9MJ04hX6-dYohzaFvCBzmsSpWo'
# YOUTUBE_CLIENT_ID = '35225584560-o2p8e71k47b9ks892gmssk7jbrskrrvv.apps.googleusercontent.com'