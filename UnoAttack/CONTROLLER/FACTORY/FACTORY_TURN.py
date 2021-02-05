from UnoAttack.CONTROLLER.FACTORY.FACTORY import FACTORY
from UnoAttack.CONTROLLER.TURN.TURN import TURN


class FACTORY_TURN(FACTORY):

    # ESTE METODO APLICA EL EFECTO DE UNA CARTA SOBRE UN ELEMENTO
    def Create(self, Cant):
        Turns = []
        for x in range(Cant):
            Turns.append(TURN())
