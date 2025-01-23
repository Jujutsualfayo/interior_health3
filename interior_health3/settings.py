import os
from pathlib import Path
import dj_database_url
import django_heroku

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key from environment variable (mandatory in production)
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "your-default-key-for-dev")  # Replace in production!

# Debug mode
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

# Allowed Hosts
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# Trusted CSRF origins
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'https://localhost:8000',
    'https://your-production-domain.com',
]

# CORS Configuration
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # React local development
    'https://your-production-domain.com',
]
CORS_ALLOW_ALL_ORIGINS = DEBUG  # Allow all in dev only

# Installed apps
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
    "whitenoise.runserver_nostatic",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL configuration
ROOT_URLCONF = "interior_health3.urls"

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', BASE_DIR / 'frontend/build'],  # React build directory
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

# WSGI and ASGI configuration
WSGI_APPLICATION = "interior_health3.wsgi.application"
ASGI_APPLICATION = "interior_health3.asgi.application"

# Channel Layers
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# Database
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3', conn_max_age=600)
}

# Authentication and Password Validation
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

# M-Pesa Configuration (Environment variables recommended)
MPESA_ENV = os.getenv('MPESA_ENV', 'sandbox')
MPESA_CONSUMER_KEY = os.getenv('MPESA_CONSUMER_KEY', 'your-default-key')
MPESA_CONSUMER_SECRET = os.getenv('MPESA_CONSUMER_SECRET', 'your-default-secret')
MPESA_SHORTCODE = os.getenv('MPESA_SHORTCODE', 'your-default-shortcode')
MPESA_PASSKEY = os.getenv('MPESA_PASSKEY', 'your-default-passkey')
MPESA_BASE_URL = 'https://sandbox.safaricom.co.ke/' if MPESA_ENV == 'sandbox' else 'https://api.safaricom.co.ke/'

# Language, timezone, and localization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static and Media Files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'frontend/build/static',  # React static files
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Security settings for production
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# Configure Django App for Heroku
django_heroku.settings(locals(), logging=False)

# Optional: Manually add WhiteNoiseMiddleware to avoid conflicts
if 'MIDDLEWARE' in locals():
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

