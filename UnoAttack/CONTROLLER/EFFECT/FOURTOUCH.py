from UnoAttack.CONTROLLER.EFFECT.EFFECT import EFFECT
from UnoAttack.CONTROLLER.ENUMERATE.COLOR import COLOR


class TWOTOUCH(EFFECT):

    # ESTE METODO APLICA EL EFECTO DE UNA CARTA SOBRE UN ELEMENTO
    def Apply(self,Element):

        # SE ASIGANAN LAS CARTAS DE PENALIZACION
        PunishmentCards = []
        Turn = Element.GetTurn()
        Gamer = Turn.GetGamerInstance()

        for x in range(4):
            PunishmentCards.extend(Element.GetLauncherCards())

        for card in PunishmentCards:
            Gamer.AddCardToHand(card)

        #SE ASIGNA EL COLOR DE LA CARTA DEL STACK
        Stack = Element.GetStack()
        Card = Stack.GetCard(0)
        Card.SetProperty(COLOR.Blue)  # AQUI SE DEBE PASAR EL COLOR ELEGIDO POR EL JUGADOR
        Stack.AddCard(Card)
