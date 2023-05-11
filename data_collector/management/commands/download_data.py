import os
import json
import logging
from django.conf import settings
from data_collector.sources.apps import sources
from django.core.management.base import BaseCommand
from data_collector.managers.elastic_manager import ElasticManager
from data_collector.managers.mongo_manager import MongoManager
from data_collector.sources.connectors.misp import MISPConnector

logger = logging.getLogger(__name__)
mongo = MongoManager()
elastic = ElasticManager()


from data_collector.download.download_ip import IPDownloader

class Command(BaseCommand):

    def handle(self, *args, **options):
        data = sources["Maldatabase"].collect()
        print(data)
        elastic.insert_data_bulk("maldatabase",data)
        mongo.save_data("maldatabase",data)
        
