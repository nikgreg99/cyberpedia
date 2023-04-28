from abc import abstractmethod
from data_collector.dataclasses import CollectorConfig
from functools import cached_property
from data_collector.utils import compute_md5, computer_sha1, compute_sha256,compute_ssdeep, compute_imphash



class Collector(object):

    name: str
    enabled: bool
    config : CollectorConfig

    def __init__(self,name) -> None:
        self.name = name
        self.config = CollectorConfig(name)

    @abstractmethod
    def init_collector(self):
        raise NotImplementedError()
    
   
    def collect(self):
        raise NotImplementedError()
    
    
    def collect_target(self,target):
        raise NotImplementedError()
    
    
    @cached_property
    def secrets(self) -> dict:
       return self.config.read_secrets()
    


class FileAnalyzer(object):

    filename: str
    mimetype: str
    
    def read_file_content(self):
        with open(self.filename,"rb") as f:
            data = f.read()
        return data
    
    @cached_property
    def md5(self):
        return compute_md5(self.content)
    
    @cached_property
    def sha1(self):
        return computer_sha1(self.content)
    
    @cached_property
    def sha256(self):
        return compute_sha256(self.content)
    
    @cached_property
    def ssdeep(self):
        return compute_ssdeep(self.content)
    
    @cached_property
    def impash(self):
        return compute_imphash(self.content)
    
    @abstractmethod
    def run_analysis(self,file):
        raise NotImplemented()
        


        



    
