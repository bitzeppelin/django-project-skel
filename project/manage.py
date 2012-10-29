#!/usr/bin/env python
import os
import sys
import settings

sys.path.insert(0, os.path.join(settings.ROOT_DIR, 'apps'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
