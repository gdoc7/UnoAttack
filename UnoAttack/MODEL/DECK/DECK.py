from abc import ABCMeta, abstractmethod

class DECK(metaclass=ABCMeta):
    Cards=()

# ---------METODOS------------------------------------

# ESTE METODO AGREGA UNA CARTA AL ATRIBUTO "CARDS"
    @abstractmethod
    def AddCard(self, Card):
        pass

# ESTE METODO SACA UNA CARTA DEL ATRIBUTO "CARDS"
    @abstractmethod
    def GetCard(self, position):
        pass

# ESTE METODO RETORNA EL ATRIBUTO "CARDS"
    def Get_Cards(self):
        return self.Cards
