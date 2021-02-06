from UnoAttack.MODEL.DECK.DECK import DECK
from random import Random


class Launcher(DECK):

    # --------CONSTRUCTORES-------------------------------
    def __init__(self):
        self.Random = Random()

    def AddCard(self, card):
        lista = list(self.Cards)
        lista.insert(0, card)
        self.Cards = tuple(lista)

    def GetCard(self, position = 0):
        list_cards = list(self.Cards)
        lista = list()

        for x in range(0,self.Random.randrange(1, 10)):
            if(len(list_cards) > 0):
                card = list_cards.pop(0)
                lista.append(card)

        self.Cards = tuple(list_cards)
        return lista

