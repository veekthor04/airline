#!/usr/bin/env python
import os
import sys
import flask
if __name__ == "__main__":
    #runhttps://github.com/veekthor04/flights.git
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airline.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
