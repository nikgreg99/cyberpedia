import logging
from .data_download import DataDownloader
from data_collector.sources.apps import sources

logger = logging.getLogger(__name__)

YARIFY = 'Yarify'

class YaraDownloader(DataDownloader):

    _self = None

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def download_data(self):
        data = sources[YARIFY].collect()

