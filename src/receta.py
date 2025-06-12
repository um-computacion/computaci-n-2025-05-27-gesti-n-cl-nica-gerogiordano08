from src.paciente import Paciente
from src.medico import Medico
from datetime import datetime
class Receta:
    def __init__(self, paciente:Paciente, medico:Medico, medicamentos:list[str], fecha:datetime):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos
        self.__fecha__ = fecha
    def __str__(self):
        return '\n Medicamentos: ' + ','.join(self.__medicamentos__) + '. \nPaciente ' + self.__paciente__.obtener_nombre().capitalize() + '. \nFecha ' + datetime.strftime(self.__fecha__, '%Y-%m-%d')  + '\nMédico ' + self.__medico__.obtener_nombre().capitalize() + '.\n '
