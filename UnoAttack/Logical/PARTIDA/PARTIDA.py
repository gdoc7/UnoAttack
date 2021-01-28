
class PARTIDA():

    #ESTE METODO PERMITE ASIGNAR LOS TURNOS DE LA PARTIDA
    def AssignTurn(self,Turn):
        self.Turn = Turn

    def GetTurn(self):
       return self.Turn

    def GetGamerOfTurn(self):
        return self.Turn.GetGamerInstance()

    # INICIO DE LA PARTIDA
    def Start(self,Filter):
        Gamer = self.Turn.GetGamer(Filter)
        Card = Gamer.SelectHandCard(0)
        Card.ApplyEffect(self)

