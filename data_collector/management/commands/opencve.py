import logging
from django.core.management.base import BaseCommand
from data_collector.managers.mongo_manager import MongoManager
from data_collector.managers.elastic_manager import ElasticManager
from data_collector.sources.apps import sources
from data_collector.models import Index

OPENCVE = "OpenCVE"

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self,*args, **options):
        mongo = MongoManager()
        elastic = ElasticManager()
        indexes = Index.indexes_by_key(OPENCVE)
        CVE,CWE,vendors,products = sources[OPENCVE].collect()
    
        
            