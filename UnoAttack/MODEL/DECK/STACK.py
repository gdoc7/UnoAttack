from UnoAttack.MODEL.DECK.DECK import DECK

class STACK(DECK):

# ---------METODOS------------------------------------

    # ESTE METODO AGREGA UNA CARTA A LA PILA DE CARTAS
    def AddCard(self, Card):
        Lista=list(self.Cards)
        Lista.insert(0, Card)
        self.Cards=tuple(Lista)

    # ESTE METODO RETORNA LA CARTA QUE ESTA EN EL TOPE DE LA PILA
    def GetCard(self, position = 0):
        Lista=list(self.Cards)
        Card= Lista.pop(position)
        self.Cards = tuple(Lista)
        return Card

