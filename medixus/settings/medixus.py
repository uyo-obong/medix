from datetime import timedelta

from .environment import env


MEDIXUS_FEATURES = env.list(
    "MEDIXUS_FEATURES",
    default=[],
)

# Reset password link lifetime interval (in seconds). By default: 1 hour.
MEDIXUS_RESET_PASSWORD_EXPIRATION_DELTA = timedelta(
    seconds=env.int(
        "MEDIXUS_RESET_PASSWORD_EXPIRATION_DELTA",
        default=3600,
    ),
)

if "LOG_SQL" in MEDIXUS_FEATURES:  # pragma: no cover
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {"require_debug_true": {"()": "django.utils.log.RequireDebugTrue"}},
        "formatters": {
            "simple": {"format": "[%(asctime)s] %(levelname)s %(message)s"},
            "verbose": {"format": "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"},
            "sql": {
                "()": "medixus.loggers.SQLFormatter",
                "format": "[%(duration).3f] %(statement)s",
            },
        },
        "handlers": {
            "console": {"class": "logging.StreamHandler", "formatter": "verbose", "level": "DEBUG"},
            "sql": {"class": "logging.StreamHandler", "formatter": "sql", "level": "DEBUG"},
        },
        "loggers": {
            "django.db.backends": {
                "handlers": ["sql"],
                "level": "DEBUG",
                "filters": ["require_debug_true"],
                "propagate": False,
            },
            "django.db.backends.schema": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
        },
    }
