import logging
from .data_download import DataDownloader
from data_collector.sources.apps import sources

logger = logging.getLogger(__name__)

class UrlDownload(DataDownloader):

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self


    def download_data():
        pass