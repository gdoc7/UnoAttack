from UnoAttack.Data.DECK.DECK import DECK

class STACK(DECK):

    def Add_Card(self,Card):
        Lista=list(self.Cards)
        Lista.insert(0, Card)
        self.Cards=Lista

    def Get_Card(self,position):
        Lista=list(self.Cards)
        Card= Lista.pop(0)
        self.Cards=Lista
        return Card