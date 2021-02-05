from UnoAttack.CONTROLLER.ENUMERATE.COLOR import COLOR
from UnoAttack.CONTROLLER.ENUMERATE.NUMBER import NUMBER
from UnoAttack.CONTROLLER.FACTORY.FACTORY_CARD import FACTORY_CARD
from UnoAttack.MODEL.CARD.CARD import CARD


class FACTORY_SIMPLECARD(FACTORY_CARD):


    # ESTE METODO APLICA EL EFECTO DE UNA CARTA SOBRE UN ELEMENTO
    def Create(self, Cant):
        Cards = []
        for color in COLOR:
            Cards.extend(self.AllColor(color,Cant))
        return Cards


    def AllColor(self,Color,Cant):
        CardsColor = []
        for x in range(Cant):
            if(x <=10):
                CardsColor.append(CARD(Color, NUMBER.Cero.GetNumber(x),None))
            else:
                CardsColor.extend(self.AllColor(Color,Cant-10))
                break
        return CardsColor
