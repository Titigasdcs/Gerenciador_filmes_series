import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-duv-$2dn(dd@g(5lt)(vkw4c)5d7*#9geehj25&hg68a+x3z@3'

DEBUG = True

ALLOWED_HOSTS = []


# -------------------------------
# APLICAÇÕES INSTALADAS
# -------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # sua aplicação principal
]


# -------------------------------
# MIDDLEWARE
# -------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'


# -------------------------------
# TEMPLATES
# -------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'app' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# -------------------------------
# BANCO DE DADOS
# -------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -------------------------------
# VALIDAÇÃO DE SENHAS
# -------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -------------------------------
# INTERNACIONALIZAÇÃO
# -------------------------------
LANGUAGE_CODE = 'pt-br'  # ✅ Corrigido para português
TIME_ZONE = 'America/Sao_Paulo'  # ✅ corrigido: o erro vinha de "Sao Paulo" sem underline
USE_I18N = True
USE_TZ = True


# -------------------------------
# ARQUIVOS ESTÁTICOS
# -------------------------------
STATIC_URL = '/static/'

# ✅ Onde o Django vai procurar os arquivos CSS, JS, imagens, etc.
STATICFILES_DIRS = [
    BASE_DIR / "app" / "static",
]

# ✅ Pasta onde o collectstatic junta tudo (usado em deploy)
STATIC_ROOT = BASE_DIR / "staticfiles"

# -------------------------------
# ARQUIVOS DE MÍDIA (caso tenha imagens futuramente)
# -------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
