import enum
from abc import abstractmethod


class HashType(enum):
    MD5 = "MD5"
    SHA256 = "SHA256"

class ObservableType(enum):
    IP = "IP"
    HASH = "Hash"
    DOMAIN = "Domain"
    GENERIC = "Generic"

class CollectorServiceType(enum):
    SOURCE = "Source"
    DATA_FORMAT = "Data Format" 

class CollectorService(object):

    collector_data_format : CollectorServiceType

    @abstractmethod
    def set_collector_parameters(**kwargs):
        pass

    @abstractmethod
    def collect(self):
        pass

    @abstractmethod
    def collect_observable(self,target):
        pass

