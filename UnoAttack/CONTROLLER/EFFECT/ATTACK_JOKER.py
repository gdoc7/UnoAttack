from UnoAttack.CONTROLLER.EFFECT.EFFECT import EFFECT
from UnoAttack.CONTROLLER.EFFECT.TWOTOUCH import TWOTOUCH
from UnoAttack.CONTROLLER.ENUMERATE.TYPE import TYPE

class ATTACKJOKER(EFFECT):

    def __init__(self):
        self.SetEffect(TWOTOUCH())

    def Apply(self, Element):
        Turns = Element.GetTurn()
        Gamers = Turns.GetGamers()
        #GamerAttack = GetGamerAttack()

        #for Gamer in range(0,len(Gamers)):
         #   if(Gamer == GamerAttack):


        #    Gamer.ChangeStatus(TYPE.Locked, 1)


















