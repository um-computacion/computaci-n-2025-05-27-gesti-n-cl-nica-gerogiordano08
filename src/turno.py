from src.paciente import Paciente
from src.medico import Medico
from datetime import datetime

class Turno:
    def __init__(self, paciente :Paciente, medico: Medico, fecha_hora: datetime , especialidad: str):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__fecha_hora__ = fecha_hora
        self.__especialidad__ = especialidad
    def obtener_medico(self):
        return self.__medico__
    def obtener_fecha_hora(self):
        return self.__fecha_hora__
    def __str__(self):
        return '\n Paciente: ' + self.__paciente__.obtener_nombre().capitalize() + '. \n Fecha: ' + datetime.strftime(self.__fecha_hora__, '%Y-%m-%d %H:%M') + '. \n Medico: ' + self.__medico__.obtener_nombre().capitalize() + '. \n Especialidad: ' + self.__especialidad__.capitalize() + '.\n'
