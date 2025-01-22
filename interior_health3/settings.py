import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "%+pbbe50v8$^w$3qs)_i92w0x^anv4@rzp!x#zb5v41%g5vi9q"
DEBUG = False

ALLOWED_HOSTS = ['interiorhealth.herokuapp.com']

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'https://localhost:8000',
]

# Add CORS allowed origins
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Frontend URL
]

CORS_ALLOW_ALL_ORIGINS = True


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users",
    "drugs",
    "orders",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",  
    "channels",
]


# Middleware settings (ensure correct comma placement)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # Corrected with comma
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "interior_health3.urls"

LOGIN_URL = '/users/login/'  # Matches the login view path in users/urls.py


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
            ],
        },
    },
]

WSGI_APPLICATION = "interior_health3.wsgi.application"

ASGI_APPLICATION = "interior_health3.asgi.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# M-Pesa Configuration
MPESA_ENV = 'sandbox'  # Change to 'production' when ready
MPESA_CONSUMER_KEY = 'WLTwUZMRYuG0UhdnXRljFY0rS7XQIhK3DmCMGtkZKL3i8Wdv'
MPESA_CONSUMER_SECRET = 'P2BG5FDs3IeEWNqNWKvncAGoO7mjGAFv4TYSySOw9ZkBXG3NtiylUgHfd8uu4SPF'
MPESA_SHORTCODE = '174379'  # Business Shortcode
MPESA_PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2b290dcb7338b8bd6a83b894c603abc7'
MPESA_BASE_URL = 'https://sandbox.safaricom.co.ke/' if MPESA_ENV == 'sandbox' else 'https://api.safaricom.co.ke/'





AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

INSTALLED_APPS += ['whitenoise.runserver_nostatic']
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Security settings for production (optional, can be activated when going live)
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
