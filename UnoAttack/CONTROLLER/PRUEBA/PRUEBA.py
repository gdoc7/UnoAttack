import multiprocessing

import daemon as daemon

from UnoAttack.CONTROLLER.FACTORY.FACTORY_CARD import FACTORY_CARD
from UnoAttack.CONTROLLER.FACTORY.FACTORY_SIMPLECARD import FACTORY_SIMPLECARD
from UnoAttack.MODEL.CARD.CARD import CARD
from UnoAttack.CONTROLLER.ENUMERATE.COLOR import COLOR
from UnoAttack.MODEL.DECK.HAND import HAND
from UnoAttack.MODEL.DECK.STACK import STACK
from UnoAttack.CONTROLLER.ENUMERATE.NUMBER import NUMBER
from UnoAttack.CONTROLLER.ENUMERATE.TYPE import TYPE
from UnoAttack.MODEL.GAMER.GAMER import GAMER
from UnoAttack.CONTROLLER.EFFECT.JUMP import JUMP
from UnoAttack.CONTROLLER.MATCH.MATCH_NUMBER import MATCH_NUMBER
from UnoAttack.CONTROLLER.MATCH.MATCH_PROPERTY import MATCH_PROPERTY
from UnoAttack.CONTROLLER.PARTIDA.PARTIDA import PARTIDA
from UnoAttack.CONTROLLER.SCORE.SCORE import SCORE
from UnoAttack.CONTROLLER.STATUS.STATUS import STATUS
from UnoAttack.CONTROLLER.TURN.TURN import TURN
from UnoAttack.MODEL.DECK.LAUNCHER import Launcher
from random import Random


stack = STACK()
turn =TURN()

hand = HAND()
hand2 = HAND()
hand3 = HAND()

#DECLARACION DE LOS MATCH
Match = MATCH_NUMBER()
Match2 = MATCH_PROPERTY()
Match.Add_Match(Match2)

#DECLARACION DE LOS ESTATUS
status = STATUS(TYPE.Available)
status2 = STATUS(TYPE.Available)
status3 = STATUS(TYPE.Available)

#DECLARACION DE LAS PUNTUACINES DE LOS GAMERS
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
Card1 = CARD(COLOR.Blue, NUMBER.Cero,None)
Card2 = CARD(COLOR.Green, NUMBER.Dos,None)
Card3 = CARD(COLOR.Red, NUMBER.Nueve,None)
Card4 = CARD(COLOR.Blue, NUMBER.Dos,None)
Card5 = CARD(COLOR.Blue, None,Effect)
Card6 = CARD(COLOR.Blue, NUMBER.Cero,None)
Card7 = CARD(COLOR.Green, NUMBER.Dos,None)
Card8 = CARD(COLOR.yellow, NUMBER.Cinco,None)
Card9 = CARD(COLOR.Green, NUMBER.Seis,None)

#ASIGNACION LOS SCORE DE LAS CARTAS
Score4 = SCORE()
Score4.SetValue(20)
Card1.AssignScore(Score4)

Score5 = SCORE()
Score5.SetValue(20)
Card2.AssignScore(Score5)

Score6 = SCORE()
Score6.SetValue(50)
Card3.AssignScore(Score6)

Score7 = SCORE()
Score7.SetValue(10)
Card4.AssignScore(Score7)

Score8 = SCORE()
Score8.SetValue(60)
Card5.AssignScore(Score8)

Score9 = SCORE()
Score9.SetValue(50)
Card6.AssignScore(Score9)

Score10 = SCORE()
Score10.SetValue(30)
Card7.AssignScore(Score10)

Score11 = SCORE()
Score11.SetValue(20)
Card8.AssignScore(Score11)

Score12 = SCORE()
Score12.SetValue(80)
Card9.AssignScore(Score12)


#AGREGAR LAS CARTAS A LA MANO DEL JUGADOR 1
hand.AddCard(Card5)
hand.AddCard(Card1)
hand.AddCard(Card2)
Gamer1.AssignHand(hand)

hand2.AddCard(Card3)
hand2.AddCard(Card4)
hand2.AddCard(Card6)
Gamer2.AssignHand(hand2)

#hand3.AddCard(Card7)
#hand3.AddCard(Card8)
#hand3.AddCard(Card9)
Gamer3.AssignHand(hand3)


#ASIGNAR PUNTUACIONES
Gamer1.AssignScore(Score1)
Gamer2.AssignScore(Score2)
Gamer3.AssignScore(Score3)

stack.AddCard(Card6)


#ASIGNACION DE LOS TURNOS
turn.AddGamer(Gamer1)
turn.AddGamer(Gamer2)
turn.AddGamer(Gamer3)

Partida = PARTIDA()
Partida.AssignTurn(turn)
Partida.AssignStack(stack)


Launcher = Launcher()
Launcher.AddCard(CARD(COLOR.Blue, NUMBER.Cero,None))
Launcher.AddCard(CARD(COLOR.Green, NUMBER.Cero,None))
Launcher.AddCard(CARD(COLOR.Red, NUMBER.Cero,None))
Launcher.AddCard(CARD(COLOR.yellow, NUMBER.Cero,None))
Launcher.AddCard(CARD(COLOR.Blue, NUMBER.Seis,None))
Launcher.AddCard(CARD(COLOR.Green, NUMBER.Siete,None))
Launcher.AddCard(CARD(COLOR.Red, NUMBER.Tres,None))
Launcher.AddCard(CARD(COLOR.yellow, NUMBER.Dos,None))
Launcher.AddCard(CARD(COLOR.Blue, NUMBER.Ocho,None))
Launcher.AddCard(CARD(COLOR.Green, NUMBER.Cuatro,None))
Launcher.AddCard(CARD(COLOR.Red, NUMBER.Uno,None))
Launcher.AddCard(CARD(COLOR.yellow, NUMBER.Siete,None))


#INICIALIZA EL DEMONIO QUE VERIFICA LA CANTIDAD DE CARTAS RESTANTES EN EL LAUNCHER
d = multiprocessing.Process(
        name='daemon',
        target=daemon,
)
d.daemon = True
d.start()
d.join()

#print(Launcher.GetCard())
#print(Launcher.Cards)

#(Partida.VerificateWin())

#Factory = FACTORY_SIMPLECARD()
#Cards=Factory.Create(10)
#for x in Cards:
#    print("Carta", x.GetNumber(), x.GetProperty().name)


#for x in Partida.Turn.GetGamers():
#    print(x.GetScore())

#Partida.Start(FILTER_BY_STATUS(),Match)


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

