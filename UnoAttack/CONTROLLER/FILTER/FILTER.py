from abc import ABCMeta, abstractmethod

class FILTER(metaclass=ABCMeta):

    # ESTE METODO VERIFICA SI EL ELEMENTO CUMPLIO CON EL FILTRO
    @abstractmethod
    def Apply(self,Element):
        pass