from abc import ABC, abstractmethod


class LibraryTests(ABC):

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def query1(self):
        pass

    @abstractmethod
    def query2(self):
        pass

    @abstractmethod
    def query3(self):
        pass

    @abstractmethod
    def query4(self):
        pass

    def __init__(self):
        self.queries = [self.query1, self.query2, self.query3, self.query4]
