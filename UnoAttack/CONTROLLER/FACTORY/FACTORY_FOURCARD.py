from UnoAttack.CONTROLLER.EFFECT.FOURTOUCH import TWOTOUCH
from UnoAttack.CONTROLLER.FACTORY.FACTORY_CARD import FACTORY_CARD
from UnoAttack.MODEL.CARD.CARD import CARD



class FACTORY_FOURCARD(FACTORY_CARD):

    def Create(self, Cant):
        Cards = []
        for x in range(Cant):
            Cards.append(CARD(None, None, TWOTOUCH()))

        return Cards

