import logging
from typing import Any 
from django.core.management.base import BaseCommand
from data_collector.managers.elastic_manager import ElasticManager

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> str | None:
        elastic = ElasticManager()  
        data = elastic.count_total_records()