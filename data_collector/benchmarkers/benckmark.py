import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class Benchmark(ABC):
    
    name: str

    def __init__(self,name) -> None:
        self.name = name

    @abstractmethod
    def monitor_benchmark(self):
        pass