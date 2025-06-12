from src.paciente import Paciente
from src.turno import Turno
from src.receta import Receta
class HistoriaClinica:
    def __init__(self, paciente:Paciente, turnos:list[Turno], recetas:list[Receta]):
        self.__paciente__ = paciente
        self.__turnos__ = turnos
        self.__recetas__ = recetas
    def agregar_turno(self, turno:Turno):
        self.__turnos__.append(turno)
    def agregar_receta(self, receta:Receta):
        self.__recetas__.append(receta)
    def obtener_turnos(self):
        return self.__turnos__
    def obtener_recetas(self):
        return self.__recetas__
    def print_turnos(self):
        lista_turnos_str = []
        for x in self.__turnos__:
            lista_turnos_str.append(x.__str__())
        return lista_turnos_str
    def print_recetas(self):
        lista_recetas_str = []
        for x in self.__recetas__:
            lista_recetas_str.append(x.__str__())
        return lista_recetas_str 

    def __str__(self):
        return '\n El paciente ' + self.__paciente__.obtener_nombre().capitalize() + ' tiene los siguientes turnos: \n' + ', '.join(self.print_turnos())+ '\n y se le han emitido las siguientes recetas: \n' + ', '.join(self.print_recetas()) + '.'
