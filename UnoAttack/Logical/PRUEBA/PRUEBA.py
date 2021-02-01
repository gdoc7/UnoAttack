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
from UnoAttack.Logical.MATCH.MATCH_NUMBER import MATCH_NUMBER
from UnoAttack.Logical.MATCH.MATCH_PROPERTY import MATCH_PROPERTY
from UnoAttack.Logical.PARTIDA.PARTIDA import PARTIDA
from UnoAttack.Logical.SCORE.SCORE import SCORE
from UnoAttack.Logical.STATUS.STATUS import STATUS
from UnoAttack.Logical.TURN.TURN import TURN



stack = STACK()
turn =TURN()

hand = HAND()
han2 = HAND()
han3 = HAND()

#DECLARACION DE LOS MATCH
Match = MATCH_NUMBER()
Match2 = MATCH_PROPERTY()
Match.Add_Match(Match2)

#DECLARACION DE LOS ESTATUS
status = STATUS(TYPE.Available)
status2 = STATUS(TYPE.Available)
status3 = STATUS(TYPE.Available)

#DECLARACION DE LAS PUNTUACINES
Score1 = SCORE()
Score2 = SCORE()
Score3 = SCORE()


#Effect = REVERSE()
Effect = JUMP()

#DECLARACION DE LOS JUGADORES
Gamer1 = GAMER("Jose",status)
Gamer2 = GAMER("Martin",status2)
Gamer3 = GAMER("Rosmary",status3)

#DECLARACION DE LAS CARTAS
Card1 = CARD(COLOR.Blue, NUMBER.Cero)
Card2 = CARD(COLOR.Green, NUMBER.Dos)
Card3 = CARD(COLOR.Red, NUMBER.Nueve)
Card4 = CARD(COLOR.Blue, NUMBER.Dos)
Card5 = CARD(COLOR.Blue, None)
Card6 = CARD(COLOR.Blue, NUMBER.Cero)


#ASIGNACION DE LOS EFECTOS A LAS CARTAS
Card5.AssignEffect(Effect)

#AGREGAR LAS CARTAS A LA MANO DEL JUGADOR 1
hand.AddCard(Card5)
hand.AddCard(Card1)
hand.AddCard(Card2)
Gamer1.AssignHand(hand)

#ASIGNAR PUNTUACIONES
Gamer1.AssignScore()
Gamer1.IncrementScore(100)
Gamer2



stack.AddCard(Card6)


#ASIGNACION DE LOS TURNOS
turn.AddGamer(Gamer1)
turn.AddGamer(Gamer2)
turn.AddGamer(Gamer3)

Partida = PARTIDA()
Partida.AssignTurn(turn)
Partida.AssignStack(stack)
Partida.Start(FILTER_BY_STATUS(),Match)


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

