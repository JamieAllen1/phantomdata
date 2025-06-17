from abc import ABC, abstractmethod


class SchemaReader(ABC):
    """
    Abstract base class for data writers.
    """

    @abstractmethod
    def read(self, path):
        pass
