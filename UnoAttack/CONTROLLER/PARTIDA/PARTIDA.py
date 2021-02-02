
class PARTIDA():

    #ESTE METODO PERMITE ASIGNAR LOS TURNOS DE LA PARTIDA
    def AssignTurn(self,Turn):
        self.Turn = Turn

    def GetTurn(self):
       return self.Turn

    def AssignStack(self,Stack):
        self.Stack = Stack

    #RETORNA UNA INSTANCIA DEL JUGADOR EN EL PRESENTE TURNO
    def GetGamerOfTurn(self):
        return self.Turn.GetGamerInstance()

    #VERIFICA SI UN JUGADOR GANO LA PARTIDA
    def VerificateWin(self):
        for Gamer in self.Turn.GetGamers():
            if(Gamer.QuantityCards() == 0):
                self.SumScore(Gamer)
                return True
        return False

    def SumScore(self,Winner):
        for gamer in self.Turn.GetGamers():
            if(Winner != gamer):
                Winner.IncrementScore(gamer.SumScoreOfCards())


    #INICIO DE LA PARTIDA
    def Start(self,Filter,Match):

        if(not self.VerificateWin()):
            Gamer = self.Turn.GetGamer(Filter)
            GamerCard = Gamer.SelectHandCard(0)
            StackCard = self.Stack.GetCard(0)

            if(Match.Verificate(GamerCard,StackCard)):
                self.Stack.AddCard(GamerCard)
                GamerCard.ApplyEffect(self)


