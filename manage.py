#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRUDDemo.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobasicproject.settings')
>>>>>>> ecc8dc299e56430b6af587aa9f218151c9d0717e
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> ecc8dc299e56430b6af587aa9f218151c9d0717e
