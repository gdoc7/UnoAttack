class GAMER():

 #--------CONSTRUCTOR-------------------------------

    def __init__(self,Name,Status):
        self.ChangeEstatus(Status)
        self.SetName(Name)

 #---------METODOS------------------------------------

    #ESTE METODO RETORNA EL NOMBRE DEL JUGADOR
    def GetName(self):
        return self.Name

    #ESTE METODO PERMITE CAMBIAR EL NOMBRE DEL JUGADOR
    def SetName(self,Name):
        self.Name=Name

    #ESTE METODO RETORNA EL ESTADO DEL JUGADOR
    def GetStatusType(self):
        return self.Status.GetType()


    # ESTE METODO DERECMENTA EL TIEMPO QUE DURARA EL ESTADO
    def DecrementStatusTime(self):
        self.Status.DecrementTime()

    #ESTE METODO PERMITE CAMBIAR EL ESTADO DEL JUGADOR
    def ChangeEstatus(self,Status):
        self.Status=Status

    #ESTE METODO PERMITE ASIGNAR LA PUNTUACION AL JUGADOR
    def AssignScore(self,Score):
        self.Score=Score

    #ESTE METODO PERMITE INCREMENTAR LA PUNTUACION DEL JUGADOR
    def IncrementScore(self,Value):
        self.Score.Increment()