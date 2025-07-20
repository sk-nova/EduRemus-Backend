from os import environ

# Import split_settings tools for modular settings management
from split_settings.tools import include, optional

# Get the current environment (e.g., 'development', 'production') from environment variables
_ENV = environ.get("DJANGO_ENV")

# List of base settings components to include
_base_settings = [
    "components/base.py",  # Core Django settings
    "components/app.py",  # Installed apps configuration
    "components/middleware.py",  # Middleware configuration
    "components/template.py",  # Template engine settings
    "components/database.py",  # Database configuration
    "components/security.py",  # Security-related settings
    "components/i8n.py",  # Internationalization settings
    "components/static_and_media.py",  # Static and media files settings
    "components/logging.py",  # Logging configuration
    "components/third_party.py",  # Third-party packages settings
    f"environments/{_ENV}.py",  # Environment-specific settings
    optional("environments/local.py"),  # Optional local overrides
]

# Include all settings components
include(*_base_settings)
