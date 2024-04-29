import logging
from typing import Any 
from django.core.management.base import BaseCommand
from data_collector.managers.elastic_manager import ElasticManager
from django.conf import settings

logger = logging.getLogger(__name__)

#STATUS: OK
class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> str | None:
        elastic = ElasticManager()  
        data =  elastic.count_total_records()
        if settings.DEBUG:
            logger.info(data)