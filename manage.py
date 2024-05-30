#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings")
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


# we use sqlite3 database
# SQLite is a self-contained, serverless, zero-configuration, transactional SQL database engine. It doesn't require a separate server process to operate. Instead, the entire database is stored in a single disk file, making it easy to set up and use.

# MySQL follows a traditional client-server model where the database server process handles database operations, and clients connect to it over a network. This allows multiple clients to access the same database concurrently.
# create default table in db.sqlite3:python manage.py migrate
#create superuser:python manage.py createsuperuser
# to open admin pannel create superuser

# views take the data and render to the html page
# views and url is to be connected