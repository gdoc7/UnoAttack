from UnoAttack.Data.ENUMERATE.TYPE import TYPE
from UnoAttack.Logical.EFFECT.EFFECT import EFFECT

class JUMP(EFFECT):

    # ESTE METODO APLICA EL EFECTO DE UNA CARTA SOBRE UN ELEMENTO
    def Apply(self,Element):
        Gamer = Element.GetGamerOfTurn()
        Gamer.ChangeEstatus(TYPE.Locked,1)