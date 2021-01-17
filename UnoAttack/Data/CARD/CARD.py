
class CARD():

# --------CONSTRUCTORES-------------------------------
    def __init__(self, Property,Number):
        self.SetProperty(Property)
        self.SetNumber(Number)

 #---------METODOS------------------------------------

    #ESTE METODO RETORNA EL NUMERO DE LA CARTA
    def GetNumber(self):
        return self.Number.name

    #ESTE METODO PERMITE CAMBIAR EL NUMERO DE LA CARTA
    def SetNumber(self, Number):
        self.Number = Number

    #ESTE METODO RETORNA LA PROPIEDAD DE LA  CARTA (EN EL CASO DE UNO EL COLOR)
    def GetProperty(self):
        return self.Property.name

    #ESTE METODO PERMITE CAMBIAR LA PROPIEDAD DE LA CARTA
    def SetProperty(self, Property):
        self.Property=Property

    #ESTE METODO LE ASIGNA EL EFECTO A LA CARTA
    def AssignEffect(self, Effect):
        self.Effect = Effect

    #ESTE METODO APLICA EL EFECTO DE LA CARTA EN EL ITEM PASADO POR PARAMETRO
    def AplicateEffect(self,Item) :
        self.Effect.Aplicate(Item)

    #ESTE METODO PERMITE ASIGNAR LA PUNTUACION A LA CARTA
    def AssignScore(self,Score):
        self.Score=Score

