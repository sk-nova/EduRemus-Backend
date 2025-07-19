# =============================================================================
# Database Configuration
# -----------------------------------------------------------------------------
# Defines the database settings for the Django project.
# Uses SQLite3 as the default database engine and stores the database file
# in the project's base directory.
# =============================================================================

from config.settings.components.base import BASE_DIR

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
