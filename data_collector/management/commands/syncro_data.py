from django.core.management import BaseCommand
from data_collector.models import Index
from data_collector.managers.synch_manager import SynchManager

synch = SynchManager()

class Command(BaseCommand):

    help = "Syncronize data from MongoDB to ElasticSearch"
    synch = SynchManager()

    def handle(self, *args, **options) -> str | None:
        indexes = Index.indexes()
        self.synch.sync(indexes)
       