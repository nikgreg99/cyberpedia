import logging
from .processor import Processor
from data_collector.models import Index
from django.conf import settings
from data_collector.apps import sources

logger = logging.getLogger(__name__)

class IPProcessor(Processor):

    # ALL the suspicious IP are deepen trough different analysis
    HONEYDB_INDEX = 'honeydb'

    def __init__(self, name,quota_limit) -> None:
        super().__init__(name)
        self.quota_limit = quota_limit

    def process_data(self):
        ip_data = []
        indexes = Index.indexes_by_key(self.name)

        if len(indexes) > 1:
            logger.info(indexes)
            for index in indexes:
                if index['name'].endswith('ip'):
                    index_name = index['name']
                    break
        else:
            index_name = indexes['name']

        if settings.DEBUG:
            logger.info(index_name)

        # Since API are limited, we process a sample for the data choose randomly each day
        ip_addresses = self.extract_sample_documents(self.HONEYDB_INDEX,self.quota_limit)
        for ip_address in ip_addresses:
            remote_host = ip_address['remote_host']
            response = sources[self.name].collect_target(remote_host)
            ip_data.append(response)

            if settings.DEBUG:
                logger.info(index_name)
         
        self.elastic.insert(index_name=index_name,data=ip_data)

