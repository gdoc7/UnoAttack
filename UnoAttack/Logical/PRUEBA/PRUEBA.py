from UnoAttack.Data.CARD.CARD import CARD
from UnoAttack.Data.ENUMERATE.COLOR import COLOR
from UnoAttack.Data.DECK.HAND import HAND
from UnoAttack.Data.DECK.STACK import STACK
from UnoAttack.Data.ENUMERATE.NUMBER import NUMBER
from UnoAttack.Data.ENUMERATE.TYPE import TYPE
from UnoAttack.Data.GAMER.GAMER import GAMER
from UnoAttack.Logical.EFFECT.EFFECT import EFFECT
from UnoAttack.Logical.EFFECT.JUMP import JUMP
from UnoAttack.Logical.EFFECT.REVERSE import REVERSE
from UnoAttack.Logical.FILTER.FILTER_BY_STATUS import FILTER_BY_STATUS
from UnoAttack.Logical.PARTIDA.PARTIDA import PARTIDA
from UnoAttack.Logical.STATUS.STATUS import STATUS
from UnoAttack.Logical.TURN.TURN import TURN

hand = HAND()
stack = STACK()
turn =TURN()

status = STATUS(TYPE.Available)
status2 = STATUS(TYPE.Available)
status3 = STATUS(TYPE.Available)

#Effect = REVERSE()
Effect = JUMP()

Gamer1 = GAMER("Jose",status)
Gamer2 = GAMER("Martin",status2)
Gamer3 = GAMER("Rosmary",status3)
Card1 = CARD(COLOR.Blue, NUMBER.Cero)
Card2 = CARD(COLOR.Green, NUMBER.Dos)
Card3 = CARD(COLOR.Red, NUMBER.Nueve)
Card4 = CARD(COLOR.Blue, NUMBER.Dos)
Card5 = CARD(COLOR.Blue, None)

Card5.AssignEffect(Effect)
hand.AddCard(Card5)
hand.AddCard(Card1)
hand.AddCard(Card2)

Gamer1.AssignHand(hand)

print(Gamer1.Name)
print(Gamer2.Name)
print(Gamer3.Name)
turn.AddGamer(Gamer1)
turn.AddGamer(Gamer2)
turn.AddGamer(Gamer3)

Partida = PARTIDA()
Partida.AssignTurn(turn)
Partida.Start(FILTER_BY_STATUS())


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

