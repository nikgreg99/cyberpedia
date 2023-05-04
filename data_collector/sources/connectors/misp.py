from pymisp import PyMISP, MISPFeed
from .connector import Connector
from django.conf import settings
import logging


logger = logging.getLogger(__name__)

class MISPConnector(Connector):
    
    def init_connector():
        url = settings.MISP_URL
        auth_key = settings.MISP_KEY
        verify_cert = settings.MISP_VERIFY_CERT
        self.misp = PyMISP(url,auth_key,verify_cert,'json',debug=True)
        self.headers = {
            "Authorization": settings.MISP_AUTH_KEY,
            "Accept": "application/json",
            "Content-type": "application/json"
        }
       
        
    def get_misp_feed(self,feed_name):
        feed = MISPFeed(feed_name,self.misp)
        return feed.download()
    
    def get_misp_events(self,feed_name):
        feed = self.get_misp_feed(feed_name)
        return feed.to_events()
        



        