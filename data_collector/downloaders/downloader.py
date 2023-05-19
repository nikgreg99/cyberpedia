from abc import abstractmethod
import logging
logger = logging.getLogger(__name__)
from data_collector.managers.elastic_manager import ElasticManager
from data_collector.managers.mongo_manager import MongoManager
from data_collector.models import Index

class DataDownloader(object):

    def __init__(self) -> None:
        self.mongo = MongoManager()
        self.elastic = ElasticManager()

    def get_indexes(self,collector_name):
        return Index.indexes_by_key(collector_name)

    @abstractmethod
    def download_data(self):
        raise NotImplementedError()