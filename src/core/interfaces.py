from abc import ABC, abstractmethod
from typing import List, Any

class BaseSource(ABC):
    @abstractmethod
    def connect(self): pass
    @abstractmethod
    def start_streaming(self, callback): pass

class BaseSink(ABC):
    @abstractmethod
    def write(self, event: Any): pass
    @abstractmethod
    def batch_write(self, events: List[Any]): pass
    @abstractmethod
    def close(self): pass