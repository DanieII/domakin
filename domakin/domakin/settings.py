from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-@q00&p*4nai&y76-(j(_yx-0=ypwh2w87=u#x$@4d@=upml72-"

DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS = [
    "127.0.0.1",
]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third Party
    "tailwind",
    "theme",
    "django_browser_reload",
    "compressor",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    # Project
    "users",
    "common",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Third Party
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "domakin.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "domakin.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [BASE_DIR / "static"]


MEDIA_ROOT = BASE_DIR / "mediafiles"

MEDIA_URL = "/media/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Custom User Model

AUTH_USER_MODEL = "users.CustomUser"


# Compressor

COMPRESS_ROOT = BASE_DIR / "static"

COMPRESS_ENABLED = False

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)


# Tailwind

TAILWIND_APP_NAME = "theme"


# Auth

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/"

ACCOUNT_AUTHENTICATION_METHOD = "email"

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_USER_MODEL_USERNAME_FIELD = None

SOCIALACCOUNT_EMAIL_REQUIRED = True

SOCIALACCOUNT_LOGIN_ON_GET = True

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

ACCOUNT_FORMS = {
    "login": "users.forms.UserLoginForm",
    "signup": "users.forms.UserRegisterForm",
}

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,
    }
}


SITE_ID = 1


# Email

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_FILE_PATH = BASE_DIR / "emails"
