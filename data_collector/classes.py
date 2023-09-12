from abc import ABC,abstractmethod
from data_collector.dataclasses import CollectorConfig
from functools import cached_property

class Collector(ABC):

    name: str
    enabled: bool
    config : CollectorConfig

    def __init__(self,name) -> None:
        self.name = name
        self.config = CollectorConfig(name)

    @abstractmethod
    def init_collector(self):
        raise NotImplementedError()
    
    
    def make_request(self, final_url="",params={},data={}):
        raise NotImplementedError()


    @cached_property
    def secrets(self) -> dict:
       return self.config.read_secrets()
    
class FeedCollector(Collector):

    @abstractmethod
    def collect(self) -> dict:
        raise NotImplementedError()
    
class TargetCollector(Collector):

    @abstractmethod
    def collect_target(self) -> dict:
        raise NotImplementedError()

