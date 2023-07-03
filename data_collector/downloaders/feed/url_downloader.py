import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources



logger = logging.getLogger(__name__)

class URLDownloader(FeedDownloader):

    URL_HAUS = 'URLHaus'

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self


    def download_feed(self):
        pass