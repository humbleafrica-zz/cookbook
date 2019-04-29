#!/usr/bin/env python
import os, sys, sqlite3

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cookbook.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
