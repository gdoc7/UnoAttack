from UnoAttack.MODEL.DECK.DECK import DECK
import random


class Launcher(DECK):

    def AddCard(self, card):
        lista = list(self.Cards)
        lista.insert(0, card)
        self.cards = lista

    def GetCard(self, position):
        list_cards = list(self.Cards)
        lista = []
        randomc = random.randrange(9)

        for range_throw in randomc:
            card = list_cards.pop(0)
            lista.push(card)

        self.Cards = tuple(list_cards)
        return lista


