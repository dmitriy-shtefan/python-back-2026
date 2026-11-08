SECRET_KEY = "django-insecure-lost-and-found-classroom"
DEBUG = True

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "bureau",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    },
]

LANGUAGE_CODE = "uk"
STATIC_URL = "/static/"
