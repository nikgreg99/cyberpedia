from abc import ABCMeta, abstractmethod
from data_collector.dataclasses import CollectorConfig

from django.utils.functional import cached_property


class Collector(object):

    name: str
    _config : CollectorConfig

    def __init__(self,name) -> None:
        self.name = name
        self._config = CollectorConfig(name)

    def init_collector(self):
        raise NotImplementedError()
    
   
    def collect(self):
        raise NotImplementedError()
    
    
    def collect_target(self,target):
        raise NotImplementedError()
    
    @cached_property
    def _secrets(self) -> dict:
       return self._config.read_secrets()




    
