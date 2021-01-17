
class PARTIDA():

    #ESTE METODO PERMITE ASIGNAR LOS TURNOS DE LA PARTIDA
    def AssignTurn(self,Turn):
        self.Turn = Turn

    def GetGamerOfTurn(self):
        return self.Turn.GetGamerInstance()

    # INICIO DE LA PARTIDA
    def Start(self):
        pass