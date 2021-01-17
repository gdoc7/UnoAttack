from UnoAttack.Data.CARD.CARD import CARD
from UnoAttack.Data.ENUMERATE.COLOR import COLOR
from UnoAttack.Data.DECK.HAND import HAND
from UnoAttack.Data.DECK.STACK import STACK
from UnoAttack.Data.ENUMERATE.NUMBER import NUMBER
from UnoAttack.Data.ENUMERATE.TYPE import TYPE
from UnoAttack.Data.GAMER.GAMER import GAMER
from UnoAttack.Logical.FILTER.FILTER_BY_STATUS import FILTER_BY_STATUS
from UnoAttack.Logical.STATUS.STATUS import STATUS
from UnoAttack.Logical.TURN.TURN import TURN

hand = HAND()
stack = STACK()
turn =TURN()
status = STATUS(TYPE.Available)
status2 = STATUS(TYPE.Available)
status3 = STATUS(TYPE.Available)

Gamer1 = GAMER("Jose",status)
Gamer2 = GAMER("Martin",status2)
Gamer3 = GAMER("Rosmary",status3)
Card1 = CARD(COLOR.Blue, NUMBER.Cero)
Card2 = CARD(COLOR.Green, NUMBER.Dos)
Card3 = CARD(COLOR.Red, NUMBER.Nueve)
Card4 = CARD(COLOR.Blue, NUMBER.Dos)

#print(Gamer1)
#print(Gamer2)
#print(Gamer3)
#turn.AddGamer(Gamer1)
#turn.AddGamer(Gamer2)
#turn.AddGamer(Gamer3)
#print(turn.GetGamer(FILTER_BY_STATUS()))





#stack.AddCard(Card1)
#stack.AddCard(Card2)
#hand.AddCard(Card1)
#hand.AddCard(Card2)


#card.SetNumber(NUMBER.Nueve)


#print(Card1)
#print(Card2)
#print(stack.Cards)




#Mah = MATCH_PROPERTY()
#Meh = MATCH_NUMBER()
#Mah.Add_Match(Meh)
#print(Mah.Verificate(Card2,Card4))

