from abc import abstractmethod, ABCMeta

from UnoAttack.CONTROLLER.FACTORY.FACTORY import FACTORY


class FACTORY_CARD(FACTORY):

    # ESTE METODO APLICA EL EFECTO DE UNA CARTA SOBRE UN ELEMENTO
    @abstractmethod
    def Create(self, Cant):
        pass
