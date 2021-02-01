from abc import ABCMeta, abstractmethod

class MATCH(metaclass=ABCMeta):

    def __init__(self):
        self.Match=None

    def Add_Match(self,Match):
        self.Match=Match

    @abstractmethod
    def Verificate(self, Element1, Element2):
        pass