from abc import ABCMeta, abstractmethod

class FACTORY(metaclass=ABCMeta):

    # ESTE METODO APLICA EL EFECTO DE UNA CARTA SOBRE UN ELEMENTO
    @abstractmethod
    def Create(self, Cant):
        pass
