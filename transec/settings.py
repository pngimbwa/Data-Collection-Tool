"""
Django settings for transec project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't%r+ltdg*%53c4=wy*#lt-4b5b3v19e#p7bas5*99yhhu^16w&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#this email will be used to send email incase one need to reset his/her email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER ='pngimbwa6@gmail.com'
EMAIL_HOST_PASSWORD = 'cgpyfrxjzcsrjmju'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition

INSTALLED_APPS = (
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'farmer',
    'signup',
    #'research',
    #'iwmi',
    #'django-autocomplete-light',
    #'autocomplete_light',
    #'AUTOCOMPLETE',
    'iwmiproject',
    'geoposition',
    #'import_export',
    #'adaptors'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'transec.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        #DIRS=/Users/peterngimbwa/Documents/python/transec/src/templates,
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

WSGI_APPLICATION = 'transec.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'research',
        'USER': 'peterngimbwa',
        'PASSWORD': 'cosmas',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'#'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


'''
Static_root is where the server will look for files
when we go live(is where static file will be collected by server)
'''
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static_in_env','static_root')
#STATIC_DIRS=/Users/peterngimbwa/Documents/python/transec/static_in_env/static_root


#Staticfiles_dirs is where our files will be put inside our project

STATICFILES_DIRS = (
    
    #STATIC_DIRS=/Users/peterngimbwa/Documents/python/transec/src/static_in_pro/our_static
    os.path.join(BASE_DIR, "static_in_pro","our_static"),
   # '/var/www/static/',
)

'''
MEDIA files are related to (user) content.
This directory will mainly contain files uploaded to the website.
'''

'''
FILE_UPLOAD_HANDLERS = (
                        "django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler"
                        )
'''
DATE_INPUT_FORMATS = ('%d-%m-%Y')

MEDIA_URL='/media/'
#MEDIA_ROOT=os.path.join(BASE_DIR, "static_in_env","media_root") #use it for production
MEDIA_ROOT=os.path.join(BASE_DIR,"static_in_pro","media_root") #for development 

GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyAF8sc1RXNIB5Kfdj5tUEeoiOLPXENErK4'

DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')