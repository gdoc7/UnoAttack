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

    #ESTE METODO PERMITE ASIGNAR EL ESTADO AL JUGADOR
    def AssignStatus(self,Status):
        self.Status=Status

    #ESTE METODO RETORNA EL ESTADO DEL JUGADOR
    def GetStatusType(self):
        return self.Status.GetType()

    # ESTE METODO DERECMENTA EL TIEMPO QUE DURARA EL ESTADO
    def DecrementStatusTime(self):
        self.Status.DecrementTime()

    #ESTE METODO PERMITE CAMBIAR EL ESTADO DEL JUGADOR
    def ChangeEstatus(self,type,time):
        self.Status.SetType(type)
        self.Status.SetTime(time)

    #ESTE METODO PERMITE ASIGNAR LA PUNTUACION AL JUGADOR
    def AssignScore(self,Score):
        self.Score=Score

    #ESTE METODO PERMITE INCREMENTAR LA PUNTUACION DEL JUGADOR
    def IncrementScore(self,Value):
        self.Score.Increment()

    #ESTE METODO PERMITE ASIGNAR LA MANO DE CARTAS DEL JUGADOR
    def AssignHand(self,Hand):
        self.Hand =Hand

    #ESTE METODO PERMITE AGREGAR UNA CARTA A LA MANO DEL JUGADOR
    def AddCardToHand(self,Card):
        self.Hand.AddCard(Card)

    #ESTE METODO PERMITE SELECCIONAR UNA CARTA DE LA MANO, SEGUN SU POSICION
    def SelectHandCard(self,Position):
        self.Hand.GetCard(Position)