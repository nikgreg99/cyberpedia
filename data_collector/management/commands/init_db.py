import logging
import json
import os

from django.core.management.base import BaseCommand
from data_collector.serializers import CollectorSerializer
from data_collector.models import APIConfig
from data_collector.models import DataFeed

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    help = "Migrate secrets from .env file or docker.env file to database"

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
            for secret_key in collector['secrets']:
                secret = collector['secrets'][secret_key]
                instance , created = APIConfig.objects.get_or_create(
                        name = collector["name"],
                        type = secret_key,
                        value = cls.get_env_var(secret["env_var_key"]),
                        required = secret['required']
                )

                if created:
                    logger.info("Key registered successfully")
                    
        logger.info("All API Key migrate succesfully")
                        
    @classmethod 
    def init_data_feed(cls):
        collectors = APIConfig.collector_names()
        for collector in collectors:
            _, created = DataFeed.objects.get_or_create(
                name= collector["name"]
            )


    def handle(self, *args, **options):
        self.migrate_secrets(CollectorSerializer.read_and_verify_config())
        self.init_data_feed()
        
        

