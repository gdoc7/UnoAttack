from UnoAttack.Data.Color import Color
from UnoAttack.Logical.MATCH.MATCH import MATCH

class MATCH_PROPERTY(MATCH):

    def Verificate(self, Element1, Element2):
        if (Element1.GetProperty() == Element2.GetProperty() or Element1.GetProperty() == None):
            return True
        if (self.Match):
            return self.Match.Verificate(Element1, Element2)
        return False