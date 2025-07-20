# =============================================================================
# Local Environment Settings
# =============================================================================

# =============================================================================
# Import Installed Apps and Middleware
# -----------------------------------------------------------------------------
# Import the base installed apps and middleware configuration from the main
# components to extend them for local development.
# =============================================================================
from config.settings.components.app import INSTALLED_APPS
from config.settings.components.middleware import MIDDLEWARE

# =============================================================================
# Import Base Development Settings
# -----------------------------------------------------------------------------
# Load all base development settings to inherit common configuration for
# local development.
# =============================================================================
from config.settings.environments.development import *  # noqa

# =============================================================================
# Local Development Specific Apps
# -----------------------------------------------------------------------------
# Add any third-party packages or extensions that are useful for local
# development and debugging.
# =============================================================================
_LOCAL_DEV_APPS = [
    "django_extensions",  # Useful extensions for Django development
    "debug_toolbar",  # Django Debug Toolbar for debugging
]

# =============================================================================
# Extend Installed Apps
# -----------------------------------------------------------------------------
# Append local development apps to the main installed apps list.
# =============================================================================
INSTALLED_APPS += _LOCAL_DEV_APPS

# =============================================================================
# Middleware Configurations
# -----------------------------------------------------------------------------
# Add middleware specific to local development, such as the Debug Toolbar.
# =============================================================================
MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

# =============================================================================
# Django Shell Plus Configuration
# -----------------------------------------------------------------------------
# Configure Django Shell Plus to use IPython and customize its behavior
# for local development.
# =============================================================================
IPYTHON_ARGUMENTS = []  # Arguments for IPython shell (empty for now)
IPYTHON_KERNEL_DISPLAY_NAME = "Django Shell-Plus"  # Display name for IPython kernel
SHELL_PLUS = "ipython"  # Use IPython for shell_plus
SHELL_PLUS_DONT_LOAD = []  # Do not auto-load any models into shell_plus
SHELL_PLUS_PRINT_SQL = True  # Print SQL queries in shell_plus
SHELL_PLUS_PRINT_SQL_TRUNCATE = None  # No truncation for printed SQL queries
SHELL_PLUS_SQLPARSE_FORMAT_KWARGS = dict(
    reindent_aligned=True,  # Align SQL reindentation
    truncate_strings=500,  # Truncate long strings in SQL output
)

# =============================================================================
# Internal IPs for Debug Toolbar
# -----------------------------------------------------------------------------
# Specify internal IP addresses that are allowed to access the Debug Toolbar.
# =============================================================================
INTERNAL_IPS = [
    "127.0.0.1",
]

# =============================================================================
# End of Local Environment Settings
# =============================================================================
