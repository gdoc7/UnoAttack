from UnoAttack.Data.Carta.Card import Card
from UnoAttack.Data.Color import Color
from UnoAttack.Data.DECK.HAND import HAND
from UnoAttack.Data.DECK.STACK import STACK
from UnoAttack.Data.NUMBER import NUMBER
from UnoAttack.Logical.MATCH.MATCH_NUMBER import MATCH_NUMBER
from UnoAttack.Logical.MATCH.MATCH_PROPERTY import MATCH_PROPERTY


hand = HAND()
stack = STACK()
Card1 = Card(Color.Blue,NUMBER.Cero)
Card2 = Card(Color.Green,NUMBER.Dos)
Card3 = Card(Color.Red,NUMBER.Nueve)
Card4 = Card(Color.Blue,NUMBER.Dos)

stack.Add_Card(Card1)
stack.Add_Card(Card2)
hand.Add_Card(Card1)
hand.Add_Card(Card2)
card = hand.Get_CardInstance(1)
#card.SetNumber(NUMBER.Nueve)

for x in hand.Cards:
    print(x.GetNumber())


#print(Card1)
#print(Card2)
#print(stack.Cards)




#Mah = MATCH_PROPERTY()
#Meh = MATCH_NUMBER()
#Mah.Add_Match(Meh)
#print(Mah.Verificate(Card2,Card4))

