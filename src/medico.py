
from src.especialidad import Especialidad

class Medico:
    def __init__(self, nombre:str, matricula:str, especialidades: list[Especialidad]):
        self.__nombre__ = nombre
        self.__matricula__ = matricula
        self.__especialidades__ = especialidades
    def agregar_especialidad(self, especialidad: Especialidad):
        self.__especialidades__.append(especialidad)
    def obtener_matricula(self):
        return self.__matricula__
    def obtener_especialidad_para_dia(self, dia:str):
        for especialidad in self.especialidades:
            if especialidad in dia:
                return list(set(self.especialidades) & set(dia))
        else:
            return None
    def obtener_nombre(self):
        return self.__nombre__
    def print_especialidades(self):
        lista = []
        for x in self.__especialidades__:
            lista.append(x.__tipo__)
        return lista
    def __str__(self):
        return '\n Nombre: ' + self.__nombre__.capitalize() + '. \n Matrícula: ' + self.__matricula__ + '. \n Especialidades: ' + ', '.join(self.print_especialidades()) + '. \n'
