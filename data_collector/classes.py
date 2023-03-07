import enum
from abc import abstractmethod

class CollectorServiceType(enum):
    SOURCE = "Source"
    DATA_FORMAT = "Data Format" 

class CollectorService(object):

    collector_data_format : CollectorServiceType

    @abstractmethod
    def set_collector_parameters(**kwargs):
        pass

    @abstractmethod
    def collect(target=None):
        pass

