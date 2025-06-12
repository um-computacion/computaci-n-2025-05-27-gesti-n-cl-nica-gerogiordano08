from src.historia_clinica import HistoriaClinica
from src.turno import Turno
from src.receta import Receta
from src.medico import Medico
from src.paciente import Paciente
import datetime
class Clinica:
    def __init__(self, pacientes:dict[str, Paciente], medicos:dict[str, Medico], turnos:list[Turno], historias_clinicas:dict[str, HistoriaClinica]):
        self.__pacientes__ = pacientes
        self.__medicos__ = medicos
        self.__turnos__ = turnos
        self.__historias_clinicas__ = historias_clinicas
    def agregar_paciente(self, paciente:Paciente):
        turnos = []
        recetas = []
        self.__pacientes__[paciente.__dni__] = paciente
        self.__historias_clinicas__[paciente.__dni__] = HistoriaClinica(paciente, turnos, recetas)

    def agregar_medico(self, medico:Medico):
        self.__medicos__[medico.__matricula__] = medico
    def obtener_pacientes(self): 
        return self.__pacientes__.values()
    def obtener_medicos(self):
        return self.__medicos__.values()
    def obtener_medico_por_matricula(self, matricula:str):
        return self.__medicos__[matricula]
    def obtener_paciente_por_dni(self, dni:str):
        return self.__pacientes__[dni]
    def agendar_turno(self, dni:str, matricula:str, especialidad:str, fecha_hora:datetime):
        turno = Turno(self.obtener_paciente_por_dni(dni), self.obtener_medico_por_matricula(matricula), fecha_hora, especialidad)
        self.__turnos__.append(turno)
        self.obtener_historia_clinica(dni).agregar_turno(turno)
    def obtener_turnos(self):
        return self.__turnos__
    def emitir_receta(self, dni:str, matricula:str, medicamentos:list[str]):
        receta = Receta(self.obtener_paciente_por_dni(dni), self.obtener_medico_por_matricula(matricula), medicamentos, datetime.date.today())
        self.obtener_historia_clinica(dni).agregar_receta(receta)
        return receta
    
    def obtener_historia_clinica(self, dni:str): 
        return self.__historias_clinicas__[dni]
    def validar_existencia_paciente(self, dni:str):
        if dni in self.__pacientes__:
            return True
        else:
            return False
    def validar_existencia_medico(self, matricula:str):
        if matricula in self.__medicos__.keys():
            return True
        else:
            return False
    def validar_turno_no_duplicado(self, matricula:str, fecha_hora:datetime):
        turnos = {}
        i = 0
        for x in self.__turnos__:
            turnos[x.obtener_medico().obtener_matricula()] = x.__fecha_hora__
        for x in turnos.keys():
            if matricula == x:
                if turnos[matricula] == fecha_hora:
                    i += 1
        if i > 1:
            return 'dup'
        elif i == 1:
            return 'ex'
        elif i == 0:
            return 'no ex'
    def obtener_dia_semana_en_espanol(self, fecha: datetime):
        dias_espanol = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        return dias_espanol[fecha.weekday()]
    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str):
        especialidades = []
        for espec in medico.__especialidades__:
            if dia_semana in espec.__dias__:
                especialidades.append(espec)
        return especialidades
    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str):
        for esp in medico.__especialidades__:
            if especialidad_solicitada == esp.__tipo__:
                if esp.verificar_dia(dia_semana):
                    return True
        return False