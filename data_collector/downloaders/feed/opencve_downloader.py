import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources
from django.conf import settings
from data_collector.utils import process_data

logger = logging.getLogger(__name__)

class OpenCVEDownloader(FeedDownloader):

    self = None

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def __init__(self) -> None:
        super().__init__()


    def process_vendor(self,vendors):
        filtered_vendors = [vendor['human_name'] for vendor in vendors if 'human_name' in vendor]
        data = sources['ExploitAlert'].collect_target(filtered_vendors)
        self.elastic.insert('exploit-alert',data)
        return filtered_vendors
    
    
  
    def download_feed(self):
        data = sources['OpenCVE'].collect()
        if settings.DEBUG:
            logger.info(data['cve'])
            logger.info(data['cwe'])
            logger.info(data['vendors'])
        self.elastic.insert('opencve-cve',data['cve'])
        self.elastic.insert('opencve-cwe',data['cwe'])
        self.elastic.insert('opencve-vendors',data["vendors"])
        self.process_vendor(data['vendors'])

    