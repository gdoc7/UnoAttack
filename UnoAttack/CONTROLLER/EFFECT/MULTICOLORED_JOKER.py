from UnoAttack.CONTROLLER.EFFECT.EFFECT import EFFECT
from UnoAttack.CONTROLLER.ENUMERATE.COLOR import COLOR


class MULTICOLORED_JOKER(EFFECT):

    # ESTE METODO APLICA EL EFECTO DE UNA CARTA SOBRE UN ELEMENTO
    def Apply(self,Element):

        Stack = Element.GetStack()
        Card = Stack.GetCard(0)
        Card.SetProperty(COLOR.Blue) #AQUI SE DEBE PASAR EL COLOR ELEGIDO POR EL JUGADOR
        Stack.AddCard(Card)



