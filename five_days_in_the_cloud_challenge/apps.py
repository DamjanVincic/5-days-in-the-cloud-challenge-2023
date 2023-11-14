from django.apps import AppConfig
import sys


class StartAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'five_days_in_the_cloud_challenge'

    def ready(self):
        if not sys.argv[1].startswith('migrate') or sys.argv[1].startswith('makemigrations'):
            from .signals import load_data
            load_data()