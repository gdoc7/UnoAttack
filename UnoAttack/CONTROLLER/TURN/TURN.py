
class TURN():
    Sequence=()

# ---------METODOS------------------------------------

    # ESTE METODO AGREGA UN JUGADOR A LA SECUENCIA DE TURNOS
    def AddGamer(self, Gamer):
        Lista=list(self.Sequence)
        Lista.append(Gamer)
        self.Sequence=tuple(Lista)

    # ESTE METODO RETORNA UNA INSTANCIA DEL 1ER JUGADOR DE LA SECUENCIA
    def GetGamerInstance(self):
        Sequence=list(self.Sequence)
        Gamer=Sequence.pop(0)
        Sequence.insert(0,Gamer)
        self.Sequence=tuple(Sequence)
        return Gamer

    # ESTE METODO RETORNA UNA INSTANCIA DEL ULTIMO JUGADOR DE LA SECUENCIA
    def GetLastGamerInstance(self):
        Sequence = list(self.Sequence)
        Gamer = Sequence.pop()
        Sequence.append(Gamer)
        self.Sequence = tuple(Sequence)
        return  Gamer


    # ESTE METODO RETORNA EL JUGADOR DE LA SECUENCIA QUE CUMPLA LA CONDICION DE FILTRO
    def GetGamer(self,Filter):
        Sequence = list(self.Sequence)
        Gamer = Sequence.pop(0)
        Sequence.append(Gamer)
        self.Sequence= tuple(Sequence)
        if(Filter.Apply(Gamer)):
            return Gamer
        return self.GetGamer(Filter)

    def GetLastGamer(self):
        Sequence = list(self.Sequence)
        Gamer = Sequence.pop()
        self.Sequence = tuple(Sequence)
        return  Gamer

    # ESTE METODO INVIERTE LA SECUENCIA DE TURNOS
    def Revert(self):
        Lista = list(self.Sequence)
        Lista.reverse()
        self.Sequence=tuple(Lista)

    # ESTE METODO RETORNA LOS JUGADORES DE LA SECUENCIA DE TURNOS
    def GetGamers(self):
        return  self.Sequence