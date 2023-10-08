from django.core.management import BaseCommand
from data_collector.downloaders.feed.valhalla_downloader import ValhallaDownloader
from data_collector.apps import sources
from data_collector.sources.connectors.taxi import TaXXIConnector

class Command(BaseCommand):

    def handle(self, *args, **options):
        valhalla = ValhallaDownloader()
        valhalla.download_feed()
        
        