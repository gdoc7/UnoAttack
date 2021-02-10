from UnoAttack.CONTROLLER.ENUMERATE.TYPE import TYPE

from UnoAttack.MODEL.GAMER.GAMER import GAMER


class FACTORY_GAMER():
    def Create(self, Cant, nombres):
        gamer = []
        for x in range(Cant):
            nombre = nombres.pop(x)
            gamer.append(GAMER(nombre, TYPE.Available))
        return gamer