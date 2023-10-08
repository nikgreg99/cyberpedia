import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources
from django.conf import settings

logger = logging.getLogger(__name__)

class YaraDownloader(FeedDownloader):

    _self = None
    YARIFY = "Yarify"

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def download_feed(self):
        data = sources[self.YARIFY].collect()
        if settings.DEBUG:
            logger.info(data)
        self.elastic.insert(self.YARIFY.lower(),data)

