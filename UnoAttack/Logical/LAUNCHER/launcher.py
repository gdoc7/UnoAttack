from Unoattack.Data import *
from random import randrange

class Launcher(evento):
    def __init__(self):
        pass

    def lanzar_carta (self, evento):
        if evento == true:
            for x in randrange(10):
                carta = GetCard(1)
        return GAMER.AddCardToHand(carta)



