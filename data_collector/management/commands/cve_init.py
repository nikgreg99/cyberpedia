import logging
from typing import Any 
from data_collector.downloaders.feed.nve import NVECollector
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> str | None:
        nve = NVECollector()
        nve.download_feed()