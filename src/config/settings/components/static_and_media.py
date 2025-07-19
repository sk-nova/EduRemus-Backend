import os
from config.settings.components.base import BASE_DIR

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
