import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources
from django.conf import settings

logger = logging.getLogger(__name__)

class FeodoDownloader(FeedDownloader):

    _self = None
    FEODO_TRACKER = "FeodoTracker"

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def __init__(self) -> None:
        super().__init__()

    def download_feed(self):
        feodo_data = sources[self.FEODO_TRACKER].collect()
        self.elastic.insert("feodo-ip",feodo_data["ip_blocklisted"])
        self.elastic.insert("feodo-ip",feodo_data["ip_blocklisted_ioc"])
                                               