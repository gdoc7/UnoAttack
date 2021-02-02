from UnoAttack.CONTROLLER.EFFECT.EFFECT import EFFECT

class REVERSE(EFFECT):

    # ESTE METODO APLICA EL EFECTO DE UNA CARTA SOBRE UN ELEMENTO
    def Apply(self,Element):
        Turn = Element.GetTurn()
        Gamer = Turn.GetLastGamer()
        Turn.Revert()
        Turn.AddGamer(Gamer)

