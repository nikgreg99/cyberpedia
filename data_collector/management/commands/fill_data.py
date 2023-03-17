from django.core.management.base import BaseCommand
import logging
from data_collector.classes import Collector

from data_collector.sources.models import DataFeed,DataFeedElement
from data_collector.sources.api.exploit_alert import ExploitAlert

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    help = "Migrate secrets from .env file to database"
    
    def handle(self, *args, **options):
        client = ExploitAlert()
        client.collect_target('Apache')
        

   
       
                        