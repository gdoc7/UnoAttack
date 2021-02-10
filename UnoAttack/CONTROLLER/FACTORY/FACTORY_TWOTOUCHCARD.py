
from UnoAttack.CONTROLLER.EFFECT.TWOTOUCH import TWOTOUCH
from UnoAttack.CONTROLLER.FACTORY.FACTORY_CARD import FACTORY_CARD
from UnoAttack.MODEL.CARD.CARD import CARD
from UnoAttack.CONTROLLER.ENUMERATE.COLOR import COLOR


class FACTORY_TWOTOUCHCARD(FACTORY_CARD):

    def Create(self, Cant):
        Cards = []
        for color in COLOR:
            Cards.extend(self.Twotouch(color, Cant))
        return Cards

    def Twotouch(self, color, cant):
        Cards_twotouch = []
        for x in range(cant):
            Cards_twotouch.append(CARD(color, None, TWOTOUCH()))
        return Cards_twotouch

