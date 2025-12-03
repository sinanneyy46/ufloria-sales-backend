import os
from pathlib import Path
import dj_database_url
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------
# SECURITY
# -------------------------------------
# CHANGE THIS → put anything strong
SECRET_KEY = os.environ.get("SECRET_KEY", "CHANGE_THIS_PRODUCTION_KEY")

# Render will set DEBUG=False automatically
DEBUG = os.environ.get("DEBUG", "False") == "True"

# CHANGE THIS → add your Render backend URL
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "your-backend-name.onrender.com",   # <--- CHANGE THIS
]

# -------------------------------------
# INSTALLED APPS
# -------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 3rd party
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",

    # your app
    "ufloria",
]

# -------------------------------------
# MIDDLEWARE
# -------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # STATIC HANDLING

    "corsheaders.middleware.CorsMiddleware",       # CORS

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"  # <--- CHANGE if your project folder name is different

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "backend.wsgi.application"   # <--- CHANGE if needed

# -------------------------------------
# DATABASE (Render PostgreSQL)
# -------------------------------------
DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# -------------------------------------
# PASSWORDS
# -------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------------------
# STATIC FILES (Render + WhiteNoise)
# -------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -------------------------------------
# CORS (Vercel Frontend)
# -------------------------------------
# CHANGE THIS → add your real Vercel frontend URL
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://your-frontend.vercel.app",   # <--- CHANGE THIS
]

CORS_ALLOW_CREDENTIALS = True

# -------------------------------------
# DRF + JWT AUTH
# -------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
}

# -------------------------------------
# INTERNATIONALIZATION
# -------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

# -------------------------------------
# DEFAULT PRIMARY FIELD
# -------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
