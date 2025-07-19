# =============================================================================
# Django Middleware Configuration
# -----------------------------------------------------------------------------
# Defines the stack of middleware components used by the Django application.
# Middleware are executed in the order listed below and handle various aspects
# such as security, sessions, authentication, CSRF protection, messaging, and
# clickjacking prevention.
# =============================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
