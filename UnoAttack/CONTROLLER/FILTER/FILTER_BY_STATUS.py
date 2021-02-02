from UnoAttack.CONTROLLER.ENUMERATE.TYPE import TYPE
from UnoAttack.CONTROLLER.FILTER.FILTER import FILTER

class FILTER_BY_STATUS(FILTER):

    # ESTE METODO VERIFICA SI EL ESTADO DEL JUGADOR ES DISPONIBLE
    def Apply(self,Element):
        if(Element.GetStatusType() == TYPE.Available.name):
           return True
        Element.DecrementStatusTime()
        Element.ChangeStatus(TYPE.Available,Element.GetStatusTime())
        return False

