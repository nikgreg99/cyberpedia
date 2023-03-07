import requests
from data_collector.exceptions import ErrorRequestException

class Maldatabase():

    base_url : str = "https://api.maldatabase.com"
    api_key = None
    session = requests.Session()

    def set_parameters(self):
        self.session.headers = {
            "Authorization": self.api_key,
            "Accept-Encoding": 'gzip'       
        }
    

    def collect(self):
        try:
            final_url = self.base_url.join("/download")
            response = self.session.get(final_url,headers=self.session.headers)
            response.raise_for_status()
        except ErrorRequestException as ex:
            pass
        return response.json()