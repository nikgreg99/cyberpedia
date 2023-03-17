from abc import ABCMeta, abstractmethod
from data_collector.dataclasses import CollectorConfig

from django.utils.functional import cached_property


class Collector():

    name: str
    _config : CollectorConfig

    def init_collector(self):
        raise NotImplementedError()
    
   
    def collect(self):
        raise NotImplementedError()
    
    
    def collect_target(self,target):
        raise NotImplementedError()
    
    @cached_property
    def _secrets(self) -> dict:
       self._config.read_secrets()




    
