from abc import ABCMeta, abstractmethod

class EFFECT(metaclass=ABCMeta):

    # ESTE METODO APLICA EL EFECTO DE UNA CARTA SOBRE UN ELEMENTO
    @abstractmethod
    def Apply(self,Element):
        pass
