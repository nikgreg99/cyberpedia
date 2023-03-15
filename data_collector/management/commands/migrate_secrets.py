import logging
import json
import os

from django.core.management.base import BaseCommand
from data_collector.serializers import CollectorSerializer
from data_collector.models import Config

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
            for secret in  collector['secrets'].keys():
                secret_type = secret[secret_type]
                if cls.get_env_var(secret_type['env_var_key']):
                    instance, created = Config.objects.get_or_create(
                        name = collector["collector"],
                        type = secret_type
                        value = cls.get_env_var(secret_type["env_var_key"]),
                        required = secret_type['required']
                    )
                    if created:
                        logging.info("Key registered successfully")
                    else:
                        pass
                        
                        
    
    def add_arguments(self,parser):
        pass

    def handle(self, *args, **options):
        self.migrate_secrets(CollectorSerializer().read_json_file())
        

