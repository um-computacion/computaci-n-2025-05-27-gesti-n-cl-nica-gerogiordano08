class Especialidad:
    def __init__(self, tipo:str, dias: list[str]):
        self.__tipo__ = tipo
        self.__dias__ = dias
    def obtener_especialidad(self):
        return self.__tipo__
    def verificar_dia(self, dia:str):
        if dia.lower() in self.__dias__: 
            return True
        else:
            return False
    def __str__(self):
        return self.__tipo__.capitalize() + ' \n (Días: ' + ', '.join(self.__dias__) + ')'
