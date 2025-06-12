class Paciente:
    def __init__(self, nombre:str, dni:str, fecha_nacimiento:str):
        self.__nombre__ = nombre
        self.__dni__ = dni
        self.__fecha_nacimiento__ = fecha_nacimiento
    def obtener_dni(self):
        return self.__dni__
    def obtener_nombre(self):
        return self.__nombre__
    def __str__(self):
        return '\n Nombre: ' + self.__nombre__.capitalize() + '. \n Dni: ' + self.__dni__ + '. \n Fecha de nacimiento: ' + str(self.__fecha_nacimiento__) + '. \n'
