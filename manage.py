#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HomeServiceManagement.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure Django is installed "
            "and the virtual environment is activated."
        ) from exc

    # If no arguments are passed, default to runserver on port 8000
    if len(sys.argv) == 1:
        sys.argv.extend(["runserver", "0.0.0.0:8000"])

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
