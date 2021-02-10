from UnoAttack.CONTROLLER.EFFECT.MULTICOLORED_JOKER import MULTICOLORED_JOKER
from UnoAttack.CONTROLLER.FACTORY.FACTORY_CARD import FACTORY_CARD
from UnoAttack.MODEL.CARD.CARD import CARD


class FACTORY_MULTICOLORCARD(FACTORY_CARD):

    def Create(self, Cant):
        Cards = []
        for x in range(Cant):
            Cards.append(CARD(None, None, MULTICOLORED_JOKER()))

        return Cards

