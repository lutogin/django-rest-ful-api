import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django commant to pause execution until database is available"""
    """Наследуем базовые команды и дополняем"""

    def handle(self, *args, **options):
        """handle - стандартный метод в классе команды"""
        self.stdout.write('Waitin for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavaulable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
