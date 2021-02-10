from UnoAttack.CONTROLLER.EFFECT.JUMP import JUMP
from UnoAttack.CONTROLLER.ENUMERATE.COLOR import COLOR
from UnoAttack.CONTROLLER.FACTORY.FACTORY_CARD import FACTORY_CARD
from UnoAttack.MODEL.CARD.CARD import CARD


class FACTORY_JUMPCARD(FACTORY_CARD):

    def Create(self, Cant):
        Cards = []
        for color in COLOR:
            Cards.extend(self.Jump(color, Cant))
        return Cards

    def Jump(self, color, cant):
        CardsJump = []
        for x in range(cant):
            CardsJump.append(CARD(color, None, JUMP()))
        return CardsJump
