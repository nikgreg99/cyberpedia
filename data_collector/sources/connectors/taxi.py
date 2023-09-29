import logging
from .connector import Connector

from django.conf import settings
from taxii2client import Server, Collection
from stix2 import TAXIICollectionSource, Filter

logger = logging.getLogger(__name__)

class TaXXIConnector(Connector):

    self = None 

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)

        return cls._self
    
    def init_connector(self):
        self.url = settings.DIGITAL_SIDE_OSINT_URL
        self.collection_endpoint = settings.DIGITAL_SIDE_URL_COLLECTIONS
        self.user = settings.TAXII_SERVER_USERNAME
        self.password = settings.TAXII_SERVER_PASSWORD
        self.server = Server(self.url, user=self.user, password=self.password)


    def get_collections(self)-> dict:
        api_by_collections = dict()
        for api in self.server.api_roots:

            api_dict = {
                'api': api.url,
                'collections': []
            }

            for collection in api.collections:

                collection_dict = {
                    'title': collection.title,
                    'description': collection.description,
                    'id': collection.id
                }

                api_dict['collections'].append(collection_dict)

            api_by_collections.update(api_dict)
        
        return api_by_collections
    
    def filter_IPs(self,collection):
        collection_url = self.collection_endpoint + collection
        collection = Collection(collection_url,user=self.user,password=self.password)
        tc_source = TAXIICollectionSource(collection)

        filters = [Filter("type","=","indicator"),
                   Filter("pattern","contains","ipv4-addr:value =")]
        
        ips = tc_source.query(filters)
        ipz = ips[0].pattern[1:-1].split("OR")

        for ip in ipz:
            print(ip.strip()[19:-1])

    def filter_urls(self,collection):
        collection_url = self.collection_endpoint + collection
        collection = Collection(collection_url,user=self.user,password=self.password)
        tc_source = TAXIICollectionSource(collection)


        filters = [Filter("type","=","indicator"),
                   Filter("pattern","contains","url:value =")]
        
        urls = tc_source.query(filters)
        urlz = urls[0].pattern[1:-1].split("OR")

        for url in urlz:
            print(url.strip()[13:-1])
    
