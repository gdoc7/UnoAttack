import multiprocessing


class PARTIDA():

    #ESTE METODO PERMITE ASIGNAR LOS TURNOS DE LA PARTIDA
    def AssignTurn(self,Turn):
        self.Turn = Turn

    # ESTE METODO RETORNA LOS TURNOS DE LA PARTIDA
    def GetTurn(self):
        return self.Turn

    # ESTE METODO PERMITE ASIGNAR EL STACK DE LA PARTIDA
    def AssignStack(self,Stack):
        self.Stack = Stack

    # ESTE METODO RETORNA EL STACK DE LA PARTIDA
    def GetStack(self):
        return self.Stack

    # ESTE METODO PERMITE ASIGNAR EL LANZADOR DE CARTAS LA PARTIDA
    def AssignLauncher(self, Launcher):
        self.Launcher = Launcher

    # ESTE METODO RETORNA UNA CANTIDAD ALEATORIA DE CARTAS DEL LANZADOR (0-10)
    def GetLauncherCards(self):
        return self.Launcher.GetCard()


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

    #SUMA LA PUNTUACION DE TODOS LOS JUGADORES, EL VALOR OBTENIDO SE LO SUMA AL PUNTAJE DEL GANADOR
    def SumScore(self,Winner):
        for gamer in self.Turn.GetGamers():
            if Winner != gamer:
                Winner.IncrementScore(gamer.SumScoreOfCards())


    #INICIO DE LA PARTIDA
    def Start(self,Filter,Match):

        if not self.VerificateWin():
            Gamer = self.Turn.GetGamer(Filter)
            GamerCard = Gamer.SelectHandCard(0) #NECESITA LA CARTA SLECCIONADA POR EL JUGADOR EN LA PARTE GRAFICA
            StackCard = self.Stack.GetCard(0)

            if Match.Verificate(GamerCard,StackCard):
                self.Stack.AddCard(GamerCard)
                GamerCard.ApplyEffect(self)


    #REVISA SI AUN QUEDAN CARTAS EN LANZADOR Y CARGA SI HACE FALTA DEL STACK
    def Verifylauncher(self, stack, launcher):
        daemon = multiprocessing.current_process()
        stack = self.Stack
        launcher = self.Launcher
        if len(launcher.Get_Cards()) <= 10:
            for x in reversed(stack.Get_Cards()-1):
                carta = stack.GetCard(x)
                launcher.AddCard(carta)





