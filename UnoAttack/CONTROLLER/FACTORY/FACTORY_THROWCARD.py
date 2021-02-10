from UnoAttack.CONTROLLER.EFFECT.COLORTHROW import COLORTHROW
from UnoAttack.CONTROLLER.ENUMERATE.COLOR import COLOR
from UnoAttack.CONTROLLER.FACTORY.FACTORY_CARD import FACTORY_CARD
from UnoAttack.MODEL.CARD.CARD import CARD


class FACTORY_THROWCARD(FACTORY_CARD):

    def Create(self, Cant):
        Cards = []
        for color in COLOR:
            Cards.extend(self.ThrowColor(color, Cant))
        return Cards

    def ThrowColor(self, color, cant):
        Cards_throw = []
        for x in range(cant):
            Cards_throw.append(CARD(color, None, COLORTHROW()))
        return Cards_throw
