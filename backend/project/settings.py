"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import ast
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ast.literal_eval(os.getenv('DJANGO_DEBUG'))

# SECURITY: restrict allowed hosts in production
PRODUCTION_HOSTS = [
    '159.89.8.174',
    'taxjungle.propulsion-learn.ch',
    'www.taxjungle.propulsion-learn.ch',
]
ALLOWED_HOSTS = ['*'] if DEBUG else PRODUCTION_HOSTS

# SECURITY: define same origin policy exceptions
# https://pypi.org/project/django-cors-headers/#:~:text=django%2Dcors%2Dheaders%20is%20a,Origin%20Resource%20Sharing%20(CORS).
CORS_ALLOWED_ORIGINS = [
    'https://taxjungle.propulsion-learn.ch',
    'https://www.taxjungle.propulsion-learn.ch',
    'http://localhost:3000',
    'http://0.0.0.0:8000',
]

# Fixes mixed-content and too-many redirects warning
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'corsheaders',
    'drf_yasg',

    # Own apps
    'apps.user',
    'apps.authentication',
    'apps.article',
    'apps.comment',
    'apps.share',
    'apps.social_network',
    'apps.article_category',
    'apps.article_image',
    'apps.article_video',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB'),
        "PORT": os.getenv('POSTGRES_PORT'),
        "HOST": os.getenv('POSTGRES_HOST'),
        "USER": os.getenv('POSTGRES_USER'),
        "PASSWORD": os.getenv('POSTGRES_PASSWORD'),
    }
}

# Custom user model
# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = "user.User"  # Uncomment after User app has been implemented

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
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

# Static files (CSS, JavaScript, images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static-files/'
STATIC_ROOT = '/static-files/'

# Media files (user uploads)
# https://docs.djangoproject.com/en/3.1/topics/files/
MEDIA_URL = '/media-files/'
MEDIA_ROOT = '/media-files/'

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_PORT = os.getenv('EMAIL_PORT')

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Django rest_framework and simple_jwt authentication settings
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # If removed, default: AllowAny
    ]
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5)
}

# API documentation
# https://drf-yasg.readthedocs.io/en/stable/readme.htm
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,  # Change settings to True to enable Django Login option
    'LOGIN_URL': 'admin/',  # URL For Django Login
    'LOGOUT_URL': 'admin/logout/',  # URL For Django Logout
    'SECURITY_DEFINITIONS': {  # Allows usage of Access token to make requests on the docs.
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
