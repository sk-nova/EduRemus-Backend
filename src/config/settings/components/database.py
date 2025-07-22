import environ

# =============================================================================
# DATABASE CONFIGURATION
# =============================================================================
# This section defines the database settings for the Django project.
# - Uses PostgreSQL as the database engine.
# - Loads credentials and connection details from environment variables.
# - Reads variables from a .env file using django-environ.
# =============================================================================

env = environ.Env()
environ.Env.read_env()  # Load environment variables from .env file

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # Database engine
        "NAME": env("POSTGRES_DB"),  # Database name
        "USER": env("POSTGRES_USER"),  # Database user
        "PASSWORD": env("POSTGRES_PASSWORD"),  # Database password
        "HOST": env("POSTGRES_HOST"),  # Database host
        "PORT": env("POSTGRES_PORT", default="5432"),  # Database port (default: 5432)
    }
}
