import json
import os

from django.core.management.base import BaseCommand
from data_collector.serializers import CollectorSerializer
from data_collector.models import DataCollectorSecret

class Command(BaseCommand):

    help = "Migrate secrets from .env file to database"

    @staticmethod
    def get_env_var(name):
        value = os.getenv(name)
        try:
            return json.loads(name)
        except(json.JSONDecodeError,TypeError):
            return value

    @classmethod
    def migrate_secrets(cls,collectors_list):
        for collector in collectors_list:
            for secret in  collector['secrets']:
                secret_name = secret['env_var_key']
                if cls.get_env_var(secret_name):
                    _, created = DataCollectorSecret.objects.get_or_create(
                        name = secret_name,
                        value = cls.get_env_var(secret_name),
                        required = secret['required']
                    )
    
    def add_arguments(self,parser):
        pass

    def handle(self, *args, **options):
        self.migrate_secrets(CollectorSerializer().read_json_file())
        

