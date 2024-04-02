import hashlib
import datetime
import os
import logging
from datetime import datetime
from .manager import Manager
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from django.conf import settings

logger = logging.getLogger(__name__)

class ElasticManager(Manager):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ElasticManager, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
            timeout = os.environ.get('ELASTIC_TIMEOUT')
            self.elastic = Elasticsearch(os.environ.get('ELASTIC_HOST'),timeout=int(timeout))
            if settings.DEBUG:
                logger.info(self.elastic.info())

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def compute_doc_id(self,content): 
        #compute a SHA256 based on the content to prevent duplicated record
        doc_content_string = str(content)
        sha_256_hash = hashlib.sha256(doc_content_string.encode()).hexdigest()
        return sha_256_hash

   
    def gen_index_data(self,index_name,doc_type,data):
        for doc in data:
            doc_id = self.compute_doc_id(doc)
            # using a yield generator data are not loaded directly into memory
            yield{
                '_index': index_name,
                '_id': doc_id,
                "timestamp": datetime.now(),
                'doc_type': doc_type,
                '_source': doc,
            }            

    def insert(self,index_name: str ,data):
     
     if isinstance(data,dict):
         doc_id = self.compute_doc_id(data)
         self.elastic.index(index=index_name,id=doc_id,document=data)
     else: 
        bulk(self.elastic, self.gen_index_data(index_name,index_name.capitalize(),data),chunk_size=4000)
    
     if settings.DEBUG:  
        logger.info("Total number of occurences: ",self.elastic.cat.count(index=index_name,format="json"))


    def create_index(self,index_name):
     if not self.elastic.indices.exists(index=index_name):
            self.elastic.indices.create(index=index_name)

     if settings.DEBUG:
         logger.info(f"{index_name} is created succesfully")


    def create_index_mapping(self,index_name,mappings={}):
        if not self.elastic.indices.exists(index_name):
            self.elastic.indices.create(index=index_name,mappings=mappings)

        if settings.DEBUG:
            logger.info(f'{index_name} with the following mappings {mappings} has been created')


    def delete_index(self,index_name):
        if self.elastic.indices.exists(index=index_name):
          self.elastic.indices.delete(index=index_name)

        if settings.DEBUG:
            logger.info(f"{index_name} has been deleted succesfully")

    def count_doc_index(self,index_name):
        if self.elastic.indices.exists(index=index_name):
           data =  self.elastic.cat.count(index_name,params={'format': 'json'})
           print(data)
           return int(data[0]['count'])
        
    def get_index_metadata_stats(self,index_name):
        index_metadata = self.elastic.indices.stats(index=index_name)["indices"]
        index_size = index_metadata[index_name]["total"]["store"]["size_in_bytes"]
        index_size_gb = index_size / (1024 ** 3)
        return {
            'index': {
                'name': index_name,
                'size_in_gigabytes': index_size_gb
            }
        }
        
    def create_data_indexes(self,indexes):
        for index in indexes:
            self.create_index(index)
       
    def query_data(self,index_name,query):
         response = self.elastic.search(index=index_name,body=query)
         documents = [doc["_source"] for doc in response["hits"]["hits"]]
         if settings.DEBUG:
             logger.info(documents)
         return documents