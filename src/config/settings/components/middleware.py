# =============================================================================
# Django Middleware Configuration
# -----------------------------------------------------------------------------
# This file defines the middleware stack for the Django application.
# Middleware are executed in the order listed and handle various aspects of
# request/response processing, including logging, security, sessions,
# authentication, CSRF protection, messaging, and clickjacking prevention.
# =============================================================================

MIDDLEWARE_PREFIXES = [
    "django_structlog.middlewares.RequestMiddleware",
]

DJANGO_MIDDLEWARE = [
    # Built-in Django middleware for core functionality
    "django.middleware.security.SecurityMiddleware",  # Security enhancements
    "django.contrib.sessions.middleware.SessionMiddleware",  # Session management
    "django.middleware.common.CommonMiddleware",  # Common HTTP features
    "django.middleware.csrf.CsrfViewMiddleware",  # CSRF protection
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # User authentication
    "django.contrib.messages.middleware.MessageMiddleware",  # Messaging framework
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Clickjacking protection
]

# Final middleware stack used by Django
MIDDLEWARE = MIDDLEWARE_PREFIXES + DJANGO_MIDDLEWARE
