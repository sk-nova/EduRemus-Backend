import os

from config.settings.components.base import BASE_DIR

# =============================================================================
# Static Files Configuration
# -----------------------------------------------------------------------------
# Define the URL and root directory for serving static files.
# STATIC_URL: Relative URL for static assets.
# STATIC_ROOT: Absolute path where static files are collected.
# =============================================================================
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
