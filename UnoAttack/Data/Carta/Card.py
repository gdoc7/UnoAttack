
class Card():

    def __init__(self, Property,Number):
        self.SetProperty(Property)
        self.SetNumber(Number)

    def GetNumber(self):
        return self.Number.name

    def SetNumber(self, Number):
        self.Number = Number

    def GetProperty(self):
        return self.Property.name

    def SetProperty(self, Property):
        self.Property=Property




