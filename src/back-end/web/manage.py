#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# pylint: disable=import-outside-toplevel
import os
import sys


def main():
    """Run administrative tasks."""
    if "prod" in sys.argv:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
        sys.argv.remove("prod")
    elif "dev" in sys.argv:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
        sys.argv.remove("dev")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
