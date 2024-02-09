import logging
import os

from django.core.management.base import BaseCommand
from data_collector.serializers import CollectorSerializer
from data_collector.models import APIConfig, Feed, Index
from data_collector.managers.elastic_manager import ElasticManager
from data_collector.helpers import read_json_file, get_env_var
from django.conf import settings

logger = logging.getLogger(__name__)

elastic = ElasticManager()

# STATUS OK


class Command(BaseCommand):

    help = "Migrate secrets and indexes from .env file file to database"
    elastic = ElasticManager()

    def load_MISP_feed(cls):
        path = os.path.join(settings.CONFIG_DIR, "misp_feeds.json")
        misp_feeds = read_json_file(path)
        for feed in misp_feeds:
            index = feed["index"]
            elastic.create_index(index)

    @classmethod
    def migrate(cls, collector_list):
        for collector in collector_list:
            feed, created = Feed.objects.get_or_create(
                name=collector["name"]
            )

            for secret_key in collector['secrets']:
                secret = collector['secrets'][secret_key]
                key = get_env_var(secret["env_var_key"])

                conf, created = APIConfig.objects.get_or_create(
                    collector=feed,
                    name=secret_key,
                    value=key,
                    required=secret['required']
                )

                print(secret, key)

                if conf.value != key:
                    conf.update_key()

            if "indexes" in collector:
                for index in collector["indexes"]:
                    _, created = Index.objects.get_or_create(
                        name=index,
                        collector=feed
                    )
                    elastic.create_index(index)

        logger.info("All API Key and index are migrated succesfully")

    def handle(self, *args, **options):
        collectors_list = CollectorSerializer.read_and_verify_config()
        self.migrate(collectors_list)
