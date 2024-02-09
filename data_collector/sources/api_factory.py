import logging
from django.conf import settings

logger = logging.getLogger(__name__)

class ApiFactory():

    def __init__(self) -> None:
        self.api_client = {}

    def register_api_key(self,api_name,api_class):
        self.api_client[api_name] = api_class

    def create_api_client(self,service_name):

        klass = self.api_client.get(service_name)

        if settings.DEBUG:
            logger.info(f"{service_name}")

        if service_name:
            return klass
        else:
            raise ValueError(f"Unsupported service: {service_name}")