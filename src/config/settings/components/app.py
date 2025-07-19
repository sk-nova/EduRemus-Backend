# =============================================================================
# Custom App Prefixes
# -----------------------------------------------------------------------------
# List any custom app prefixes or third-party packages that should be loaded
# before Django core apps.
# =============================================================================
CUSTOM_APP_PREFIXES = [
    "jazzmin",
]

# =============================================================================
# Django Core Applications
# -----------------------------------------------------------------------------
# Essential Django apps required for basic functionality.
# =============================================================================
DJANGO_CORE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# =============================================================================
# Third-Party Applications
# -----------------------------------------------------------------------------
# Add any external Django apps (e.g., REST framework, Celery) here.
# =============================================================================
THIRD_PARTY_APPS = [
    "django_structlog",
]

# =============================================================================
# Local Applications
# -----------------------------------------------------------------------------
# Add your project-specific Django apps here.
# =============================================================================
LOCAL_APPS = []

# =============================================================================
# Installed Applications
# -----------------------------------------------------------------------------
# The final list of apps to be installed by Django.
# =============================================================================
INSTALLED_APPS = CUSTOM_APP_PREFIXES + DJANGO_CORE_APPS + THIRD_PARTY_APPS + LOCAL_APPS
