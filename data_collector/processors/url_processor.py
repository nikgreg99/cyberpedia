import logging 
from .processor import Processor
from data_collector.models import Index
from django.conf import settings
from data_collector.apps import sources

logger = logging.getLogger(__name__)

class URLProcessor(Processor):

    URLHAUS_FEED = "urlhaus-urls"
    def __init__(self, name,quota_limit) -> None:
        super().__init__(name)
        self.quota_limit = quota_limit

    def process_data(self):
        url_data = []

        indexes = Index.indexes_by_key(self.name)

        if len(indexes) > 1:
            logger.info(indexes)
            for index in indexes:
                if index['name'].endswith('url'):
                    index_name = index['name']
                    break
        else:
            index_name = indexes['name']

        if settings.DEBUG:
            logger.info(index_name)

        urls_response = self.extract_sample_documents(self.URLHAUS_FEED,self.quota_limit)

        for url_response in urls_response:
            data_urls = url_response["urls"]
            for data_url in data_urls:
                url = data_url["url"]
                unescaped_url = url.replace('\\','')
                response = sources[self.name].collect_target(unescaped_url)
                if settings.DEBUG:
                    logger.info(response)
                url_data.append(response)
        
        self.elastic.insert(index_name,url_data)
                
