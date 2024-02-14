import logging
from abc import ABC,abstractmethod
from ..managers import elastic_manager

logger = logging.getLogger(__name__)

class Processor(ABC):

    elastic = elastic_manager.ElasticManager()

    def __init__(self,name):
        self.name = name

    @abstractmethod  
    def process_data(self):
        pass

    def extract_sample_documents(self,index_name,sample_size):
        query = {
            "size": sample_size,
            "query": {
                "function_score": {
                    "query": {"match_all": {}},
                    "random_score": {} # this help randomize the document
                }
            }
        }
        response = self.elastic.query_data(index_name,query)
        return response
