import logging
from .downloader import DataDownloader
from data_collector.sources.apps import sources

logger = logging.getLevelName(__name__)

class MISPDownloader(DataDownloader):

    _self = None

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def __init__(self) -> None:
        super().__init__()
    
    def download_data(self):
        pass