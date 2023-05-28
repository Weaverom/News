import logging
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*-qnx3%a_0rsz7y4ydgu7nkg%993*uuniy6e*bn(%olu9tm=d3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'news',
    'accounts',
    'django_filters',
    "django_apscheduler",

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'postgres',
#        'USER': 'postgres',
#        'PASSWORD': 'Sswq09uxr6',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    },
#}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

LOGIN_REDIRECT_URL = "/news"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "Tkach-weaver@yandex.ru"
EMAIL_HOST_PASSWORD = "jalrwfnjehdbnrpz"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "Tkach-weaver@yandex.ru"

SERVER_EMAIL = "Tkach-weaver@yandex.ru"
MANAGERS = (
    ('Tkach', 'tkachroom@mail.ru'),
)
ADMINS = (
    ('Tkach', 'tkachroom@mail.ru'),
)

CASHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_error', 'generals_info'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['errors_error', 'mail_error'],
            'level': 'ERROR',
        },
        'django.server': {
            'handlers': ['errors_error', 'mail_error'],
            'level': 'ERROR',
        },
        'django.template': {
            'handlers': ['errors_error'],
            'level': 'ERROR',
        },
        'django.db.backends': {
            'handlers': ['errors_error'],
            'level': 'ERROR',
        },
        'django.security': {
            'handlers': ['security_info'],
            'level': 'INFO',
        },
    },
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'format_console_debug',
            'filters': ['require_debug_true'],
        },
        'console_warning': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'format_console_warning',
            'filters': ['require_debug_true']
        },
        'console_error': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'format_console_error',
            'filters': ['require_debug_true']
        },
        'generals_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'format_general_info',
            'filters': ['require_debug_false']
        },
        'errors_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'error.log',
            'formatter': 'format_errors_error',
            'filters': ['require_debug_true']
        },
        'security_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'format_security_info',
            'filters': ['require_debug_true']
        },
        'mail_error': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'format_security_info',
            'filters': ['require_debug_false']
        },
    },
    'formatters': {
        'format_console_debug': {
            'format': '{asctime} {levelname} {message}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            "style": '{',
        },
        'format_console_warning': {
            'format': '{asctime} {levelname} {message} {pathname}',
            "style": '{',
        },
        'format_console_error': {
            'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
            "style": '{',
        },
        'format_general_info': {
            'format': '{asctime} {levelname}  {message}',
            "style": '{',
        },
        'format_errors_error': {
            'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
            "style": '{',
        },
        'format_security_info': {
            'format': '{asctime} {levelname} {module} {message}',
            "style": '{',
        },
        'format_mail_error': {
            'format': '{asctime} {levelname} {message} {pathname}',
            "style": '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    }
}
