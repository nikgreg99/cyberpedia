import logging
import json
import os

from django.core.management.base import BaseCommand
from data_collector.serializers import CollectorSerializer
from data_collector.models import APIConfig,Feed,Index
from data_collector.managers.elastic_manager import ElasticManager

logger = logging.getLogger(__name__)

elastic = ElasticManager()

#STATUS OK
class Command(BaseCommand):

    help = "Migrate secrets and indexes from .env file file to database"
  

    @staticmethod
    def get_env_var(name):
        value = os.getenv(name)
        try:
            return json.loads(name)
        except(json.JSONDecodeError,TypeError):
            return value

    @classmethod
    def migrate_secrets(cls,collector_list):
        for collector in collector_list:
            
            for secret_key in collector['secrets']:
                secret = collector['secrets'][secret_key]
                print(secret)
                _, created = APIConfig.objects.get_or_create(
                        name = collector["name"],
                        type = secret_key,
                        value = cls.get_env_var(secret["env_var_key"]),
                        required = secret['required']
                )
            
                if created:
                    logger.info("Key registered successfully")

                if "indexes" in collector:
                     for index in collector["indexes"]:
                        _, created = Index.objects.get_or_create(
                            name=index
                        )
                        elastic.create_index(index)
                        if created:
                            logger.info("Index registered successfully")
                    
        logger.info("All API Key and index are  migrated succesfully")
                        
    @classmethod 
    def init_data_feed(cls,collector_list):
        for collector in collector_list:
            print(collector["name"])
            _ , created = Feed.objects.get_or_create(
                name= collector["name"]
            )


    def handle(self, *args, **options):
        collectors_list = CollectorSerializer.read_and_verify_config()
        self.migrate_secrets(collectors_list)
        self.init_data_feed(collectors_list)
        data = APIConfig.to_json()
        #Index for API KEY
        elastic.create_index('secrets')
        elastic.insert_data_bulk('secrets',data)
        
        
        

