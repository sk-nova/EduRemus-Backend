# ==============================================================================
# Local Environment Settings
# ==============================================================================

import socket

import environ

# ------------------------------------------------------------------------------
# Import shared components for apps and middleware
# ------------------------------------------------------------------------------
from config.settings.components.app import INSTALLED_APPS
from config.settings.components.middleware import MIDDLEWARE

# ------------------------------------------------------------------------------
# Load environment variables from .env
# ------------------------------------------------------------------------------
env = environ.Env()
environ.Env.read_env()

# ------------------------------------------------------------------------------
# Secret Key
# ------------------------------------------------------------------------------
# Used for cryptographic signing. Keep secret in production environments.
# ------------------------------------------------------------------------------
SECRET_KEY = env("DJANGO_SECRET_KEY")

# ------------------------------------------------------------------------------
# Debug Mode
# ------------------------------------------------------------------------------
# Enables full tracebacks and error messages. Should be disabled in production.
# ------------------------------------------------------------------------------
DEBUG = True

# ------------------------------------------------------------------------------
# Allowed Hosts
# ------------------------------------------------------------------------------
# Hosts/domains the Django site can serve.
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOST")

# ------------------------------------------------------------------------------
# Local Development Specific Applications
# ------------------------------------------------------------------------------
# Extra apps used for development and debugging.
# ------------------------------------------------------------------------------
_LOCAL_DEV_APPS = [
    "django_extensions",  # Extra management commands and tools
    "debug_toolbar",  # In-browser debug panel
]

# Extend the shared installed apps
INSTALLED_APPS += _LOCAL_DEV_APPS

# ------------------------------------------------------------------------------
# Middleware
# ------------------------------------------------------------------------------
# Add development-specific middleware like debug toolbar.
# ------------------------------------------------------------------------------
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

# Callback for determining whether to show the toolbar in Docker setups
SHOW_TOOLBAR_CALLBACK = "debug_toolbar.middleware.show_toolbar_with_docker"

# ------------------------------------------------------------------------------
# Django Shell Plus Configuration
# ------------------------------------------------------------------------------
SHELL_PLUS = "ipython"  # Use IPython as backend for shell_plus
IPYTHON_ARGUMENTS = []
IPYTHON_KERNEL_DISPLAY_NAME = "Django Shell-Plus"

SHELL_PLUS_DONT_LOAD = []  # Models not to preload
SHELL_PLUS_PRINT_SQL = True
SHELL_PLUS_PRINT_SQL_TRUNCATE = None  # Do not truncate printed SQL
SHELL_PLUS_SQLPARSE_FORMAT_KWARGS = {
    "reindent_aligned": True,
    "truncate_strings": 500,
}

# ------------------------------------------------------------------------------
# Internal IPs (for Debug Toolbar)
# ------------------------------------------------------------------------------
# These IPs are allowed to see the debug toolbar.
# ------------------------------------------------------------------------------
INTERNAL_IPS = [
    "127.0.0.1",
    "0.0.0.0",
]

# Add Docker internal host IPs if available
try:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [ip[: ip.rfind(".")] + ".1" for ip in ips]
except Exception:
    # Fail silently if unable to resolve Docker IPs
    pass

# ==============================================================================
# End of Local Environment Settings
# ==============================================================================
