import json
import uuid
import os
import logging
from .manager import Manager
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from django.conf import settings

logger = logging.getLogger(__name__)

class ElasticManager(Manager):

    _self = None
    
    def __init__(self) -> None:
            self.elastic = Elasticsearch(os.environ.get('ELASTIC_HOST'),timeout=120)
            self.elastic.info()

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
        

    def create_index(self,index_name,mappings={}):
        if not self.elastic.indices.exists(index_name):
            self.elastic.indices.create(index=index_name,mappings=mappings)


    def gen_index_data(self,index_name,doc_type,data):
        data_json = json.dumps(data,indent=4)
        for doc in data:
            # using a yield generator data are not loaded directly into memory
            yield{
                '_index': index_name,
                '_id': uuid.uuid4(),
                'doc_type': doc_type,
                '_source': doc
            }            

    def insert(self,index_name,data):
     if isinstance(data,dict):
         self.elastic.index(index=index_name,id=uuid.uuid4(),document=data)
     else: 
        bulk(self.elastic, self.gen_index_data(index_name,"CTI",data),chunk_size=4000)
    
     if settings.DEBUG:  
        logger.info("Total number of occurences: ",self.elastic.cat.count(index=index_name,format="json"))


    def create_index(self,name_index):
     if not self.elastic.indices.exists(index=name_index):
            self.elastic.indices.create(index=name_index)

    def delete_index(self,name_index):
        if not self.elastic.indices.exists(index=name_index):
            self.elastic.indices.delete(index=name_index)


    def create_data_indexes(self,indexes):
        for index in indexes:
            self.create_index(index)
       