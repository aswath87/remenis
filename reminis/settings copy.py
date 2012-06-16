# Django settings for reminis project.
#import dj_database_url
import socket

if socket.gethostname() == 'Nathans-MacBook-Air.local':
    DEBUG = True
else:
    DEBUG = False

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Nathan Chan', 'nchan87+django@gmail.com'),
)

MANAGERS = ADMINS

if not DEBUG:
    DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '/Users/nathanwchan/djcode/reminis/reminis.db',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/Users/nathanwchan/djcode/reminis/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8n0s+#vt^uo(^_fdz=ks%+!$%hc^ohmxa_zq=18u=p7_pi1vt3'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'reminis.FacebookConnectMiddleware.FacebookConnectMiddleware',
#    'facebook.middleware.SignedRequestMiddleware',
#    'facebook.middleware.AppRequestMiddleware',
)

ROOT_URLCONF = 'reminis.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'reminis.wsgi.application'

TEMPLATE_DIRS = (
    '/Users/nathanwchan/djcode/reminis/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reminis.core',              
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_facebook',
#    'facebook',
#    'facebook.modules.profile.page',
#    'facebook.modules.profile.user',
#    'facebook.modules.profile.event',
#    'facebook.modules.profile.application',
#    'facebook.modules.connections.post',
)

FACEBOOK_APP_ID = '301406439948925'
FACEBOOK_APP_SECRET = 'd4e5d448e3e40c2fb13e21d8b4ef40e4'
FACEBOOK_STORE_LIKES = True
FACEBOOK_STORE_FRIENDS = True
FACEBOOK_LOGIN_DEFAULT_REDIRECT = '/facebook/connect/'
FACEBOOK_REGISTRATION_BACKEND = 'django_facebook.registration_backends.UserenaBackend'

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                           'django_facebook.auth_backends.FacebookBackend',
)
AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'
ACCOUNT_ACTIVATION_DAYS = 10
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django_facebook.context_processors.facebook',
)

#FACEBOOK_APPS = {
#    'name' : {
#            'ID': '301406439948925',
#            'SECRET': 'd4e5d448e3e40c2fb13e21d8b4ef40e4',
#            'CANVAS-PAGE': 'https://apps.facebook.com/yourapp',
#            'CANVAS-URL': '',
#            'SECURE-CANVAS-URL': '',
#            'REDIRECT-URL': 'mydomain.com/facebook/redirect/?next=%2F%2Fwww.facebook.com%2Fpages%2F',
#            'DOMAIN' : 'localhost.local:8000',
#            'NAMESPACE': 'mynamespace',
#    }
#}
#
#AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.ModelBackend',
#    'facebook.backends.authentication.AuthenticationBackend',
#)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# Manually inject Heroku settings due to lack of a settings.py file
# https://github.com/heroku/heroku-buildpack-python/blob/master/bin/compile
# 
# Issue logged https://github.com/heroku/heroku-buildpack-python/issues/15

import os
import sys
import urlparse
urlparse.uses_netloc.append('postgres')
urlparse.uses_netloc.append('mysql')

try:
    
    # Check to make sure DATABASES is set in settings.py file.
    # If not default to {}
    
    if 'DATABASES' not in locals():
        DATABASES = {}
    
    if 'DATABASE_URL' in os.environ:
        url = urlparse.urlparse(os.environ['DATABASE_URL'])
        
        # Ensure default database exists.
        DATABASES['default'] = DATABASES.get('default', {})
        
        # Update with environment configuration.
        DATABASES['default'].update({
                                    'NAME': url.path[1:],
                                    'USER': url.username,
                                    'PASSWORD': url.password,
                                    'HOST': url.hostname,
                                    'PORT': url.port,
                                    })
        if url.scheme == 'postgres':
            DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
        
        if url.scheme == 'mysql':
            DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
except:
    print 'Unexpected error:', sys.exc_info()

