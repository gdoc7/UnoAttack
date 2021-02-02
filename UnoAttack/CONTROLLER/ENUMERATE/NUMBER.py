from enum import Enum, auto

class NUMBER(Enum):
     Cero=auto()
     Uno=auto()
     Dos=auto()
     Tres=auto()
     Cuatro=auto()
     Cinco=auto()
     Seis=auto()
     Siete=auto()
     Ocho=auto()
     Nueve=auto()

     def GetNumber(self,number):

          if(number == 0):
               return self.Cero
          elif(number == 1):
               return self.Uno
          elif(number == 2):
               return self.Dos
          elif(number == 3):
               return self.Tres
          elif(number == 4):
               return self.Cuatro
          elif(number == 5):
               return self.Cinco
          elif(number == 6):
               return self.Seis
          elif(number == 7):
               return self.Siete
          elif(number == 8):
               return self.Ocho
          elif(number == 9):
               return self.Nueve
