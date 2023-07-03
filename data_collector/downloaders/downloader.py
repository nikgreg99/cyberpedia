from abc import ABC
import logging
logger = logging.getLogger(__name__)
from data_collector.managers.elastic_manager import ElasticManager
from data_collector.managers.mongo_manager import MongoManager
from data_collector.models import Index

class Downloader(ABC):

    def __init__(self) -> None:
        self.mongo = MongoManager()
        self.elastic = ElasticManager()
        logger.info("MongoDB and Elastic are initiated succesfully")

    def get_indexes(self,collector_name):
        return Index.indexes_by_key(collector_name)