import requests
import enum
from data_collector.exceptions import ErrorRequestException

class WhoisOutputFormatType(enum):
    XML = "XML"
    JSON = "JSON"



class Whois():

    base_url : str = "https://www.whoisxmlapi.com/whoisserver/WhoisService"
    session = requests.Session()
    
    def set_parameters(self):
        self.api_key = ""
        self.params = {
            "apiKey": self.api_key,
            "outputFormat": WhoisOutputFormatType.JSON,
            "preferFresh": 1,
            "ip": 1,
            "ipWhois": 1
        }
      
    def collect_target(self,target: str):
        self.params["domainName"] = target
        try:
            response =  self.session.get(self.base_url,params=self.params)
            response.raise_for_status()
        except ErrorRequestException as ex:
            pass

    