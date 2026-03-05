# nck_revision/settings.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Load local .env for development (ignored in production)
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ======================
# SECURITY
# ======================
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False") == "True"

<<<<<<< HEAD
# Hosts allowed
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "nursing-portal-10.onrender.com").split(",")
=======
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p62)z75$cuh&@8!&%_=%)928=0*l%51#^7m83@y&5gwzc2g3^1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['nursing-portal-10.onrender.com']


# Application definition
>>>>>>> c903c548791837f24b3d8cb764e860b3f1bf47e6

# ======================
# APPLICATION DEFINITION
# ======================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your app
    'revision',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files on Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nck_revision.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 👈 your templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nck_revision.wsgi.application'

# ======================
# DATABASE (SQLite for simplicity)
# ======================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ======================
# PASSWORD VALIDATION
# ======================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ======================
# INTERNATIONALIZATION
# ======================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

# ======================
# STATIC FILES
# ======================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']  # local static files

# WhiteNoise storage for compression & caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ======================
# LOGIN REDIRECTS
# ======================
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'

# ======================
# DEFAULT PRIMARY KEY
# ======================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ======================
# PAYHERO CONFIGURATION
# ======================
PAYHERO_CONFIG = {
    "AUTH_TOKEN": os.getenv("PAYHERO_AUTH_TOKEN"),
    "ACCOUNT_ID": os.getenv("PAYHERO_ACCOUNT_ID"),
    "CHANNEL_ID": int(os.getenv("PAYHERO_CHANNEL_ID", 5911)),
    "PROVIDER": os.getenv("PAYHERO_PROVIDER", "m-pesa"),
    "CALLBACK_URL": os.getenv("PAYHERO_CALLBACK_URL", f"https://{ALLOWED_HOSTS[0]}/callback/"),
}
