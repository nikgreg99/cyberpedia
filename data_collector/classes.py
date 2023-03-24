from abc import ABCMeta, abstractmethod
from data_collector.dataclasses import CollectorConfig
from functools import cached_property


class Collector(object):

    name: str
    enabled: bool
    config : CollectorConfig

    def __init__(self,name) -> None:
        self.name = name
        self.config = CollectorConfig(name)

    
    def init_collector(self):
        raise NotImplementedError()
    
   
    def collect(self):
        raise NotImplementedError()
    
    
    def collect_target(self,target):
        raise NotImplementedError()
    
    @cached_property
    def secrets(self) -> dict:
       return self.config.read_secrets()



    
