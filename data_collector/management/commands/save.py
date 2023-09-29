from django.core.management import BaseCommand
from data_collector.downloaders.feed.valhalla_downloader import ValhallaDownloader
from data_collector.apps import sources
from data_collector.sources.connectors.taxi import TaXXIConnector

class Command(BaseCommand):

    def handle(self, *args, **options):
        connector = TaXXIConnector()
        connector.init_connector()
        collections = connector.get_collections()
        print(connector.filter_IPs("c1f43330-103b-11ee-9ee3-4b022e286589"))

        