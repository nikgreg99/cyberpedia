import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources
logger = logging.getLogger(__name__)


class PayloadDownloader(FeedDownloader):

    _self = None
    URLHAUS = "UrlHaus"

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def __init__(self) -> None:
        super().__init__()


    def download_feed(self):
        _,data_payload = sources[self.URLHAUS].collect()
        self.elastic.insert('urlhaus-payload',data_payload)
        self.mongo.save_data('urlhaus-payload',data_payload)
