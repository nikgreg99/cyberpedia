import logging
from .downloader import DataDownloader
from data_collector.sources.apps import sources

URL_HAUS = 'URLHAUS'

logger = logging.getLogger(__name__)

class URLDownloader(DataDownloader):

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self


    def download_data(self):
        pass