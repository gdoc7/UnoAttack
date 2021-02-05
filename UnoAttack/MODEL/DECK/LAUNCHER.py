from UnoAttack.MODEL.DECK.DECK import DECK
import random


class Launcher(DECK):

    def AddCard(self, card):
        lista = list(self.Cards)
        lista.insert(0, card)
        self.cards = lista

    def GetCard(self, position):
        list_cards = list(self.Cards)
        lista = list()

        for range_throw in random.randrange(0, 9):
            card = list_cards.pop(0)
            lista.pop(card)

        self.Cards = tuple(lista)
        return self.Cards
