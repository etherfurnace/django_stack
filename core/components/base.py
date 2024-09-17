import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-j!xj6$2czf)(!8!9a1g03pmw+ei2c70=id6t7t^f3b)_3av!1w')

DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

CSRF_TRUSTED_ORIGINS_CONFIGS = os.getenv("CSRF_TRUSTED_ORIGINS", "")
if CSRF_TRUSTED_ORIGINS_CONFIGS:
    CSRF_TRUSTED_ORIGINS = CSRF_TRUSTED_ORIGINS_CONFIGS.split(",")

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]

if os.getenv('ALLOWED_HOSTS'):
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')
else:
    ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.guardian",
    "guardian",
    "unfold.contrib.simple_history",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_comment_migrate',

    "debug_toolbar",
    "django_select2",
    "import_export",
    "corsheaders",
    "rest_framework",
    "django_filters",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "rest_framework.authtoken",
    "auditlog",
    "drf_yasg",
    "django_celery_beat",
    "django_celery_results",

]

INSTALLED_APPS += [
    "apps.framework",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'better_exceptions.integrations.django.BetterExceptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'core.wsgi.application'

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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = BASE_DIR / 'assets'
STATIC_URL = 'assets/'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = "/media/"

INTERNAL_IPS = ('127.0.0.1',)

WHITENOISE_ROOT = os.path.join(STATIC_ROOT)
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DATA_UPLOAD_MAX_MEMORY_SIZE = int(os.getenv('DATA_UPLOAD_MAX_MEMORY_SIZE', '10485760'))
