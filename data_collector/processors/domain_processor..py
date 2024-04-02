import logging
from .processor import Processor
from data_collector.models import Index
from django.conf import settings
from data_collector.apps import sources

logger = logging.getLogger(__name__)

class DomainProcessor(Processor):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DomainProcessor, cls).__new__(cls)
        return cls.instance

    def __init__(self, name,quota_limit) -> None:
        super().__init__(name)
        self.quota_limit = quota_limit