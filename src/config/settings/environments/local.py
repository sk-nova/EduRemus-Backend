# ==============================================================================
# Local Environment Settings
# ==============================================================================

# Import base development settings
from config.settings.environments.development import *

# Import installed apps from the app configuration
from config.settings.components.app import INSTALLED_APPS

# ------------------------------------------------------------------------------
# Local Development Specific Apps
# ------------------------------------------------------------------------------
_LOCAL_DEV_APPS = [
    "django_extensions",  # Useful extensions for Django development
]

# Add local development apps to the installed apps list
INSTALLED_APPS.append(*_LOCAL_DEV_APPS)

# ------------------------------------------------------------------------------
# Django Shell Plus Configuration
# ------------------------------------------------------------------------------

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

# ==============================================================================
# End of Local Environment Settings
# ==============================================================================
