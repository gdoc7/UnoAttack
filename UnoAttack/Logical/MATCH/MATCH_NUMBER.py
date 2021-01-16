from UnoAttack.Logical.MATCH.MATCH import MATCH

class MATCH_NUMBER(MATCH):

    def Verificate(self, Element1, Element2):
        if (Element1.GetNumber() == Element2.GetNumber()):
            return True
        if (self.Match):
            return self.Match.Verificate(Element1, Element2)
        return False