from pathlib import Path

# =============================================================================
# Base Directory and Root Directory Configuration
# -----------------------------------------------------------------------------
# Defines the root directory of the project using pathlib for path operations.
# =============================================================================
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent
ROOT_DIR = BASE_DIR.parent

# =============================================================================
# URL Configuration
# -----------------------------------------------------------------------------
# Specifies the module containing the URL patterns for the project.
# =============================================================================
ROOT_URLCONF = "config.urls"

# =============================================================================
# WSGI Application
# -----------------------------------------------------------------------------
# Points to the WSGI application callable for deployment.
# =============================================================================
WSGI_APPLICATION = "config.wsgi.application"

# =============================================================================
# Default Primary Key Field Type
# -----------------------------------------------------------------------------
# Sets the default type for auto-generated primary keys in Django models.
# =============================================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
