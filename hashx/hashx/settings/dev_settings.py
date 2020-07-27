import logging
from .base_settings import *

DEBUG = config("DEBUG", default=True)

INSTALLED_APPS += [
    "debug_toolbar",
]


MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")


DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    # }
    "default": {
        "ENGINE": config("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": config("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": config("SQL_USER", "user"),
        "PASSWORD": config("SQL_PASSWORD", ""),
        "HOST": config("SQL_HOST", "localhost"),
        "PORT": config("SQL_PORT", "5432"),
    }
}

if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'test_database',
            'USER': 'test_user',
            'PASSWORD': 'test_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


# Debug Toolbar

# Debug toolbar will only be shown on these IPs
INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

# Add, remove or change the order of panels here.
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

# Add custom toolbar settings here
DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": True,
    "SHOW_COLLAPSED": True,
}

STATIC_ROOT = ""
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


l = logging.getLogger("django.db.backends")
l.setLevel(logging.DEBUG)
l.addHandler(logging.StreamHandler())

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "debug.log",
        },
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
AXES_ENABLED = True
