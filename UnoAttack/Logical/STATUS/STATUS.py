
class STATUS():

# --------CONSTRUCTOR-------------------------------
     def __init__(self,Type):
          self.SetTime(0)
          self.SetType(Type)

# ---------METODOS------------------------------------

     # ESTE METODO RETORNA EL TIEMPO QUE DURARA EL ESTADO
     def GetTime(self):
          return self.Time

     # ESTE METODO PERMITE CAMBIAR EL NUMERO DE LA CARTA
     def SetTime(self, Time):
          if (Time > 0):
               self.Time = Time


     # ESTE METODO INCREMENTA EL TIEMPO DEL ESTADO
     def IncrementTime(self,Time):
               self.Time += Time

     # ESTE METODO DECREMENTA EL TIEMPO DEL ESTADO
     def DecrementTime(self):
               self.Time -= 1

     # ESTE METODO RETORNA EL TIPO DE ESTADO
     def GetType(self):
          return self.Type.name

     # ESTE METODO CAMBIA EL TIPO DE ESTADO
     def SetType(self, Type):
          self.Type = Type



