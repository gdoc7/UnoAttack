from UnoAttack.CONTROLLER.EFFECT.EFFECT import EFFECT
from UnoAttack.CONTROLLER.ENUMERATE.COLOR import COLOR


class TWOTOUCH(EFFECT):

    # ESTE METODO APLICA EL EFECTO DE UNA CARTA SOBRE UN ELEMENTO
    def Apply(self,Element):

        Turn = Element.GetTurn()
        Gamer = Turn.GetGamerInstance()
        PunishmentCards = Element.GetLauncherCards()
        PunishmentCards.extend(Element.GetLauncherCards())

        for card in PunishmentCards:
            Gamer.AddCardToHand(card)
