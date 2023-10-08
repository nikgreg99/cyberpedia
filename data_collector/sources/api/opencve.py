import base64
import requests
from requests import HTTPError
import logging
import enum
from data_collector.classes import  FeedCollector,TargetCollector
from django.conf import settings
from data_collector.utils import validate_cve_format, process_data
from data_collector.helpers import get_env_var

logger = logging.getLogger(__name__)


class CVSSSeverity(enum.Enum):
    NONE = "NONE"
    LOW = "LOw"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"



class OpenCVE(FeedCollector,TargetCollector):

    _self = None
    base_url : str = get_env_var('OPENCVE_URL')
    opencve = requests.Session()

    CVE_PAGES = 1000

    vendor_params = {
        "page": 1
    }

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        username = self.secrets["username"]
        password = self.secrets["password"] 
        auth_message_bytes= f"{username}:{password}".encode()
        auth_base64 = base64.b64encode(auth_message_bytes).decode("ascii")
        self.opencve.headers = {
            "Authorization": f"Basic {auth_base64}",
            "Accept": "application/json"
        }
        self.err = {}
        self.opencve.proxies = settings.PROXIES

   
    def make_requests_open_cve(self,final_url,params={}):
        try:
            response = self.opencve.get(final_url,params=params)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.err["opencve"] = ex
        return response.json()
    
    def list_CVE_URL(self):
        url_paged = []
        for i in range(3000):
            final_url = self.base_url + f"/cve?page={str(i)}"
            url_paged.append(final_url)
            page +=1
        data = process_data(self.make_requests_open_cve,url_paged)
        return data

    def CVE_details(self,CVE):
        if validate_cve_format(CVE):
            final_url = self.base_url + f"/cve/{CVE}"
            return self.make_requests_open_cve(final_url)
        
    def CWE_details(self,CWE):
        final_url = self.base_url + f"/cwe/{CWE}"
        return self.make_requests_open_cve(final_url)
    
    def list_CWE(self):
        CWE_params = {
        "page": 1
        }  
        final_url = self.base_url + "/cwe"
        return self.make_requests_open_cve(final_url)
    
    def list_vendors(self):
        final_url = self.base_url + "/vendors"
        return self.make_requests_open_cve(final_url)

    def collect_target(self, target):
        return super().collect_target(target)
    
    def collect(self):
        CVE = self.list_CVE()
        vendors = self.list_vendors()
        return {
            'cve': CVE,
            'cwe': [],
            'vendors': []
        }