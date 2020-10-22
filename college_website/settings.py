"""
Django settings for college_website project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
# import dj_database_url
# import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%auou4l7kh^p@ng#omta7@m$$szq4p!nd2_@taurx&21aiqmd_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_backend',
    'corsheaders',
#    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'django_backend.urls'

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


# WSGI_APPLICATION = 'college_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


# DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME':'df47toahr9qd3r',
#             'USER':'lwkrnivsiyegcg',
#             'PASSWORD':'ad712677c9a999a7a7fb03de17db5192e29155f74bd1fca51797306bbea683ef',
#             'HOST':'postgres://lwkrnivsiyegcg:ad712677c9a999a7a7fb03de17db5192e29155f74bd1fca51797306bbea683ef@ec2-34-193-117-204.compute-1.amazonaws.com:5432/df47toahr9qd3r',
#             'PORT': '5432',
#         }
# # }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {}
# DATABASES['default'] = dj_database_url.config(conn_max_age=600)
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
       
    )
}
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS_ACCESS_KEY_ID = "AKIA6L4D2DGHUY5HU6O3"
# AWS_SECRET_ACCESS_KEY = "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"
# AWS_STORAGE_BUCKET_NAME = "djangobackendbpit"

# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None


# AWS_S3_REGION_NAME = 'ap-south-1'
# AWS_S3_SIGNATURE_VERSION = 's3v4'


STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

MEDIA_ROOT=os.path.join(BASE_DIR, 'media/')
MEDIA_URL="/media/"

# django_heroku.settings(locals())
