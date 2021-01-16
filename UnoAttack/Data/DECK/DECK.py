from abc import ABCMeta, abstractmethod

class DECK(metaclass=ABCMeta):
    Cards=()

    @abstractmethod
    def Add_Card(self,Card):
        pass

    @abstractmethod
    def Get_Card(self,position):
        pass

    def Get_Cards(self):
        return self.Cards
