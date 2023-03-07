import requests
from data_collector.exceptions import ErrorRequestException
class HoneyDB():

    base_url :str = "https://honeydb.io/api"

    def set_parameters(self):
        self.honey_db_api_id = ""
        self.honey_db_api_key = ""
        self.session = requests.Session()
        self.session.headers = {
            "X-HoneyDb-ApiId": self.honey_db_api_id,
            "X-HoneyDb-ApiKey": self.honey_db_api_key
        }

    def _collect_bad_ip(self):
        try:
            final_url = self.base_url.join("/bad-hosts")
            response = self.session.get(final_url,headers=self.session.headers)
        except ErrorRequestException as ex:
            pass
        
        return response.json()
    
    def _collect_twitter_feed(self):
        try:
            final_url = self.base_url.join("/twitter-threat-feed")
            response = self.session.get(final_url,headers=self.session.headers)
        except ErrorRequestException as ex:
            pass
        return response.json()
    
    def _ip_info(self,ip):
        try:
            internet_scanner_url = self.base_url.join("/internet-scanner/info/{}".format(ip))
            response_ip_info_scanner = self.session.get(internet_scanner_url,headers=self.session.headers)
            ip_info = response_ip_info_scanner.json()
            ip_url = self.base_url.join("/ipinfo/{}".format(ip))
            response_ip_url = self.session.get(ip_url,self.session.headers)
            ip_url = response_ip_url.json()
            ip_info.extend(ip_url)
        except ErrorRequestException as ex:
            pass
        return ip_info