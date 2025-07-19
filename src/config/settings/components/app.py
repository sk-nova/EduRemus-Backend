CUSTOM_APP_PREFIXES = [
    "jazzmin",
]

DJANGO_CORE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = []

LOCAL_APPS = []

INSTALLED_APPS = CUSTOM_APP_PREFIXES + DJANGO_CORE_APPS + THIRD_PARTY_APPS + LOCAL_APPS
