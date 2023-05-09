import logging
from .data_download import DataDownloader
from data_collector.sources.apps import sources
from data_collector.managers.elastic_manager import ElasticManager
from data_collector.managers.mongo_manager import MongoManager


logger = logging.getLevelName(__name__)

class MISPDownloader(DataDownloader):

    _self = None

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def download_data():
        pass