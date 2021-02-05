from UnoAttack.CONTROLLER.EFFECT.EFFECT import EFFECT
from UnoAttack.CONTROLLER.ENUMERATE.COLOR import COLOR


class COLORTHROW(EFFECT):

    # ESTE METODO APLICA EL EFECTO DE UNA CARTA SOBRE UN ELEMENTO
    def Apply(self,Element):

        Turn = Element.GetTurn()
        Gamer = Turn.GetLastGamerInstance()
        Cards = Gamer.GetHandCardsProperty(COLOR.Blue) #AQUI SE DEBE PASAR EL COLOR ELEGIDO POR EL JUGADOR
        Stack = Element.GetStack()

        for Card in Cards:
            Stack.AddCard(Card)
