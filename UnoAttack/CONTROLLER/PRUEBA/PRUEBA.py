from UnoAttack.MODEL.CARD.CARD import CARD
from UnoAttack.MODEL.ENUMERATE.COLOR import COLOR
from UnoAttack.MODEL.DECK.HAND import HAND
from UnoAttack.MODEL.DECK.STACK import STACK
from UnoAttack.MODEL.ENUMERATE.NUMBER import NUMBER
from UnoAttack.MODEL.ENUMERATE.TYPE import TYPE
from UnoAttack.MODEL.GAMER.GAMER import GAMER
from UnoAttack.CONTROLLER.EFFECT.EFFECT import EFFECT
from UnoAttack.CONTROLLER.EFFECT.JUMP import JUMP
from UnoAttack.CONTROLLER.EFFECT.REVERSE import REVERSE
from UnoAttack.CONTROLLER.FILTER.FILTER_BY_STATUS import FILTER_BY_STATUS
from UnoAttack.CONTROLLER.MATCH.MATCH_NUMBER import MATCH_NUMBER
from UnoAttack.CONTROLLER.MATCH.MATCH_PROPERTY import MATCH_PROPERTY
from UnoAttack.CONTROLLER.PARTIDA.PARTIDA import PARTIDA
from UnoAttack.CONTROLLER.SCORE.SCORE import SCORE
from UnoAttack.CONTROLLER.STATUS.STATUS import STATUS
from UnoAttack.CONTROLLER.TURN.TURN import TURN



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

