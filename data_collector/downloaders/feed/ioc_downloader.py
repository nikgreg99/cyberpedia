import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources
from django.conf import settings

logger = logging.getLogger(__name__)

class IOCDownloader(FeedDownloader):

    THREAT_FOX = 'ThreatFox'
    THREAT_FOX_MALWARE_LIST = "threat-fox-ioc"


    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self

    def __init__(self) -> None:
        super().__init__()
    

    def download_feed(self):
         data_ioc = sources[self.THREAT_FOX].collect()
         if settings.DEBUG:
             logger.info(data_ioc)
         self.elastic.insert(self.THREAT_FOX_MALWARE_LIST,data_ioc)