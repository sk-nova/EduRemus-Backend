from os import environ

from split_settings.tools import include, optional

_ENV = environ.get("DJANGO_ENV", default="development")


_base_settings = [
    "components/base.py",
    "components/app.py",
    "components/middleware.py",
    "components/template.py",
    "components/database.py",
    "components/security.py",
    "components/i8n.py",
    "components/static_and_media.py",
    "components/logging.py",
    "components/third_party.py",
    f"environments/{_ENV}.py",
    optional("environments/local.py"),
]

include(*_base_settings)
