import ipinfo
from data_collector.mixin import validate_ip_address
from data_collector.exceptions import InvalidIPAddress

class IPInfo():
    
    api_key = None

    def set_params(self):
        self.api_key = ""
        self.handler = ipinfo.getHandler(self.api_key)
        self.async_handler = ipinfo.getHandlerAsync(self.api_key)


    def _ipinfo_sync(self, target: str):
        try:
            if validate_ip_address(target):
                ip_details = self.handler.getDetails(target)
                ip_dict = ip_details.all
        except InvalidIPAddress as ex:
            pass
        return ip_dict

    async def _ipinfo_async(self,target: str):
        try:
            if validate_ip_address(target):
                ip_details =  await self.async_handler.getDetails(target)
                ip_dict = ip_details.all
        except InvalidIPAddress as ex:
            pass
        return ip_dict
