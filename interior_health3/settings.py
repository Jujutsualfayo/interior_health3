import os
from pathlib import Path
import dj_database_url

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key from environment variable (mandatory in production, can be set in development as default for local dev)
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "your-default-key-for-dev")

# Debug mode: Set to True for development
DEBUG = True

# Allowed Hosts: Allow localhost and local IP addresses during development
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Trusted CSRF origins for development
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'https://localhost:8000',
]

# CORS configuration: Allow all origins during development (can be restricted later for production)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # React local development
]
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins in development for convenience

# Installed apps (keep these during development)
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

# Middleware (standard middleware for dev)
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

# Templates: Add frontend/build folder for React's build files
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', BASE_DIR / 'frontend/build'],
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

# WSGI and ASGI configuration for Django channels
WSGI_APPLICATION = "interior_health3.wsgi.application"
ASGI_APPLICATION = "interior_health3.asgi.application"

# Channel Layers (required for WebSockets)
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],  # Ensure Redis is running locally
        },
    },
}

# Database configuration (use SQLite for development)
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3', conn_max_age=600)
}

# Authentication and Password Validation (standard validators)
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# M-Pesa Configuration (use sandbox keys for development)
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

# Static and Media Files (using Whitenoise for static files in development)
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

# Security settings for development: relax security settings
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = False
    SECURE_CONTENT_TYPE_NOSNIFF = False
    SECURE_HSTS_SECONDS = 0  # Don't enforce HSTS in development
    SECURE_SSL_REDIRECT = False  # No need for HTTPS in development
    SESSION_COOKIE_SECURE = False  # Don't require secure cookies in development
    CSRF_COOKIE_SECURE = False  # CSRF cookies don't need to be secure in development
