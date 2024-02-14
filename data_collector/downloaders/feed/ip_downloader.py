import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources
from django.conf import settings

logger = logging.getLogger(__name__)


class IPDownloader(FeedDownloader):

    _self = None
    HONEY_DB = 'HoneyDB'

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def __init__(self) -> None:
        super().__init__()
    

    def download_IP(self):
        data = sources[self.HONEY_DB].collect()
        if settings.DEBUG:
            logger.info(data['bad-ip'])
        self.elastic.insert('honeydb',data['bad-ip'])

        
    def download_feed(self):
        self.download_IP()