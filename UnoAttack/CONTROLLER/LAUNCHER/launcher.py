
from random import randrange
from UnoAttack.MODEL.DECK import STACK
from UnoAttack.MODEL.GAMER import GAMER

class Launcher():
    def __init__(self):
        pass

    def lanzar_carta (self, evento):
        if evento:
            for x in randrange(10):
                card = STACK.STACK.GetCard(0)
                GAMER.GAMER.AssignHand(card)




