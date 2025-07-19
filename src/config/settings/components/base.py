from pathlib import Path


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
