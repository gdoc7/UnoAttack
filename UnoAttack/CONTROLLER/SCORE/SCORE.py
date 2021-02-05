class SCORE():

# --------CONSTRUCTORES-------------------------------
    def __init__(self):
        self.SetValue(0)

# ---------METODOS------------------------------------

    # ESTE METODO RETORNA EL PUNTAJE
    def GetValue(self):
        return self.Value

    # ESTE METODO PERMITE CAMBIAR EL PUNTAJE
    def SetValue(self, Value):
        if(Value >= 0):
            self.Value = Value

    # ESTE METODO INCREMENTA EL PUNTAJE
    def Increment(self,Value):
        if (Value >= 0):
            self.Value+=Value

    # ESTE METODO DECREMENTA EL PUNTAJE
    def Decrement(self,Value):
        if(Value >= 0):
            self.Value-=Value