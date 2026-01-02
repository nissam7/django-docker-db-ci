"""
Django settings for core project.
"""

import os
import random
import string
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# SECURITY
# =========================

SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    SECRET_KEY = "".join(
        random.choice(string.ascii_lowercase) for _ in range(32)
    )

# 🔐 PRODUCTION MODE
DEBUG = False

# =========================
# HOSTS (PRODUCTION SAFE)
# =========================

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "16.16.212.60",   # EC2 IP (temporary)
    # later add: "<ALB-DNS-NAME>"
]

CSRF_TRUSTED_ORIGINS = [
    "http://16.16.212.60",
    "http://16.16.212.60:8000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

# =========================
# APPLICATIONS
# =========================

INSTALLED_APPS = [
    "admin_black.apps.AdminBlackConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home",
]

# =========================
# MIDDLEWARE
# =========================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

# =========================
# TEMPLATES
# =========================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# =========================
# DATABASE (AWS RDS POSTGRESQL)
# =========================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_db",
        "USER": "django_user",
        "PASSWORD": "StrongPassword123",
        "HOST": "django-postgres-db.cv6m8aiiqflt.eu-north-1.rds.amazonaws.com",
        "PORT": "5432",
        "CONN_MAX_AGE": 60,
        "OPTIONS": {
            "sslmode": "require",
        },
    }
}

# =========================
# PASSWORD VALIDATION
# =========================

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# =========================
# I18N
# =========================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# =========================
# STATIC FILES (WHITENOISE)
# =========================

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# =========================
# DEFAULTS
# =========================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_REDIRECT_URL = "/"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
