from UnoAttack.Data.DECK.DECK import DECK

class HAND(DECK):

    def Add_Card(self,Card):
        Lista=list(self.Cards)
        Lista.append(Card)
        self.Cards=Lista

    def Get_Card(self,position):
        Lista=list(self.Cards)
        Card= Lista.pop(position)
        self.Cards=tuple(Lista)
        return Card

    def Get_CardInstance(self,position):
        i=0
        card = None
        for x in self.Cards:
            if(i == position):
                card= x
            i+=1
        return  card

    def Get_Cards_Property(self, Property):
        Lista=list(self.Cards)
        Requests=[]
        for card in self.Cards:
            if (card.GetProperty().name == Property.name):
                Requests.append(card)
                Lista.remove(card)
        self.Cards=tuple(Lista)
        return Requests

