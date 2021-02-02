from UnoAttack.CONTROLLER.ENUMERATE.TYPE import TYPE
from UnoAttack.CONTROLLER.EFFECT.EFFECT import EFFECT

class JUMP(EFFECT):

    # ESTE METODO APLICA EL EFECTO DE UNA CARTA SOBRE UN ELEMENTO
    def Apply(self,Element):
        Gamer = Element.GetGamerOfTurn()
        Gamer.ChangeStatus(TYPE.Locked, 1)

