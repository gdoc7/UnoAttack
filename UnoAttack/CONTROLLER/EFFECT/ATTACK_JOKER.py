from UnoAttack.CONTROLLER.EFFECT.EFFECT import EFFECT
from UnoAttack.CONTROLLER.EFFECT.TWOTOUCH import TWOTOUCH
from UnoAttack.CONTROLLER.ENUMERATE.TYPE import TYPE
from UnoAttack.CONTROLLER.PRUEBA.PRUEBA import turn



class ATTACKJOKER(EFFECT):
    def __init__(self):
        self.SetEffect(TWOTOUCH)

    def Apply(self, Element):
        Element = turn.GetGamers()

        for player in Element:
            Element(player).ChangeStatus(TYPE.Locked, 1)



## Aqui deberia ir el doble manotazo















