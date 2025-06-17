from abc import ABC, abstractmethod


class DataWriter(ABC):
    """
    Abstract base class for data writers.
    """

    @abstractmethod
    def write(self, data, path):
        pass
