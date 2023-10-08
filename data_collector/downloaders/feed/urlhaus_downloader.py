import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources
from django.conf import settings

logger = logging.getLogger(__name__)

class URLHausDownloader(FeedDownloader):

    URL_HAUS = 'UrlHaus'

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self


    def download_feed(self):
        data = sources[self.URL_HAUS].collect()
        if settings.DEBUG:
            logger.info(data['url'])
            logger.info(data["payload"])
        self.elastic.insert('urlhaus-urls',data['url'])
        self.elastic.insert('urlhaus-payloads',data['payload'])