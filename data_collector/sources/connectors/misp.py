from pymisp import PyMISP
from .connector import Connector
from django.conf import settings
import logging


logger = logging.getLogger(__name__)

class MISPConnector(Connector):

    _self = None

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def init_connector(self):
        url = settings.MISP_URL
        auth_key = settings.MISP_API_KEY
        verify_cert = settings.MISP_VERIFY_CERT
        self.misp = PyMISP(url,auth_key,ssl=False,proxies = settings.PROXIES)
       
        
    def get_misp_feed(self,feed_name):
        feed = self.misp.fetch_feed(feed_name)
        return feed

    
    def get_misp_events(self,feed_name):
        print(self.get_misp_feed(feed_name))
        



        