from UnoAttack.CONTROLLER.EFFECT.REVERSE import REVERSE
from UnoAttack.CONTROLLER.ENUMERATE.COLOR import COLOR
from UnoAttack.CONTROLLER.FACTORY.FACTORY_CARD import FACTORY_CARD
from UnoAttack.MODEL.CARD.CARD import CARD


class FACTORY_REVERSECARD(FACTORY_CARD):

    def Create(self, Cant):
        Cards = []
        for color in COLOR:
            Cards.extend(self.Reverse(color, Cant))
        return Cards

    def Reverse(self, color, cant):
        Cards_Reverse = []
        for x in range(cant):
            Cards_Reverse.append(CARD(color, None, REVERSE()))
        return Cards_Reverse
