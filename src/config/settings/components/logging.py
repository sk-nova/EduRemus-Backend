# =============================================================================
# Logging Configuration
# -----------------------------------------------------------------------------
# This module sets up structured logging using structlog and configures Django's
# logging system to output logs in JSON format for easier parsing and analysis.
# =============================================================================

import structlog

# -----------------------------------------------------------------------------
# Django Logging Configuration Dictionary
# -----------------------------------------------------------------------------
LOGGING = {
    "version": 1,  # Logging schema version
    "disable_existing_loggers": False,  # Retain existing loggers
    # -------------------------------------------------------------------------
    # Formatters
    # -------------------------------------------------------------------------
    "formatters": {
        "json": {  # Formatter for JSON output using structlog
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.JSONRenderer(),
            "foreign_pre_chain": [  # Pre-processors for each log record
                structlog.processors.TimeStamper(fmt="iso"),  # Add ISO timestamp
                structlog.stdlib.add_log_level,  # Include log level
                structlog.processors.StackInfoRenderer(),  # Add stack info if available
                structlog.processors.format_exc_info,  # Format exception info
            ],
        },
    },
    # -------------------------------------------------------------------------
    # Handlers
    # -------------------------------------------------------------------------
    "handlers": {
        "default": {  # Stream handler for stdout
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "json",  # Use JSON formatter
        },
    },
    # -------------------------------------------------------------------------
    # Loggers
    # -------------------------------------------------------------------------
    "loggers": {
        "": {  # Root logger setup
            "handlers": ["default"],
            "level": "INFO",
            "propogate": False,
        }
    },
}

# -----------------------------------------------------------------------------
# Structlog Configuration
# -----------------------------------------------------------------------------
structlog.configure(
    processors=[
        structlog.threadlocal.merge_threadlocal,  # Merge thread-local context
        structlog.processors.add_log_level,  # Add log level to event dict
        structlog.processors.TimeStamper(fmt="iso"),  # Add ISO timestamp
        structlog.processors.format_exc_info,  # Format exception info
        structlog.processors.JSONRenderer(),  # Render event dict as JSON
    ],
    context_class=dict,  # Use dict for context
    logger_factory=structlog.stdlib.LoggerFactory(),  # Use standard library logger factory
    wrapper_class=structlog.stdlib.BoundLogger,  # Use BoundLogger for wrapping
    cache_logger_on_first_use=True,  # Cache logger after first use
)

# -----------------------------------------------------------------------------
# Django Structlog Configuration
# -----------------------------------------------------------------------------
# This dictionary configures django_structlog enrichers, which add useful
# context to each log entry, such as user information, request ID, and remote IP.
DJANGO_STRUCTLOG = {
    "ENRICHERS": [
        "django_structlog.enrichers.user",  # Adds authenticated user info
        "django_structlog.enrichers.request_id",  # Adds unique request ID
        "django_structlog.enrichers.remote_ip",  # Adds remote IP address
    ]
}
