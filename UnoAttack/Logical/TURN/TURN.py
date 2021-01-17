
class TURN():
    Sequence=()

# ---------METODOS------------------------------------

# ESTE METODO AGREGA UN JUGADOR A LA SECUENCIA DE TURNOS
    def AddGamer(self, Gamer):
        Lista=list(self.Sequence)
        Lista.append(Gamer)
        self.Sequence=Lista

# ESTE METODO RETORNA UNA INSTANCIA DEL 1ER JUGADOR DE LA SECUENCIA
    def GetGamerInstance(self):
        Sequence=list(self.Sequence)
        Gamer=Sequence.pop(0)
        Sequence.insert(0,Gamer)
        self.Sequence=Sequence
        return Gamer

    # ESTE METODO RETORNA EL JUGADOR DE LA SECUENCIA QUE CUMPLA LA CONDICION DE FILTRO
    def GetGamer(self,Filter):
        Sequence = list(self.Sequence)
        Gamer = Sequence.pop(0)
        Sequence.append(Gamer)
        self.Sequence= tuple(Sequence)
        if(Filter.Apply(Gamer)):
            return Gamer
        return self.GetGamer(Filter)

# ESTE METODO INVIERTE LA SECUENCIA DE TURNOS
    def Revert(self):
        Lista = list(self.Sequence)
        self.Sequence=Lista.reverse()