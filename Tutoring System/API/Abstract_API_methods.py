from abc import abstractmethod

class Abstracts:
    """
    This class creates abstract methods for all the APIs to inherit
    """
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def post(self,*args):
        pass

    @abstractmethod
    def get_by_id(self, *args):
        pass

