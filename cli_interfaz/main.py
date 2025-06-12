import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.paciente import Paciente
from src.medico import Medico
from src.especialidad import Especialidad
from src.clinica import Clinica
from datetime import datetime
import sys
from src.excepciones import *

pacientes = {}
medicos = {}
turnos = []
historias_clinicas = {}
la_clinica = Clinica(pacientes, medicos, turnos, historias_clinicas)


def menu_principal():
     return int(input('--Menú Clínica--\n 1) Agregar paciente \n 2) Agregar médico \n 3) Agendar turno \n 4) Agregar especialidad \n 5) Emitir receta \n 6) Ver historia clínica \n 7) Ver todos los turnos \n 8) Ver todos los pacientes \n 9) Ver todos los médicos \n 0) Salir \n'))

def agregar_paciente():
    dni = input('Ingrese el DNI del paciente que quiere agregar: ')
    if dni == '':
        print('Debe ingresar un DNI valido. ')
    else:
        if la_clinica.validar_existencia_paciente(dni) == False:
            nombre = input('Ingrese su nombre: ')
            if nombre == '':
                print('Debe ingresar un nombre valido. ')
            else:
                fecha_string = input('Cual es su fecha de nacimiento? (aaaa-mm-dd): ' )
                if fecha_string == '':
                    print('Debe ingresar una fecha valida. ')
                else:
                    la_clinica.agregar_paciente(Paciente(nombre, dni, fecha_string))
                    print('Gracias. El paciente fue registrado en el sistema de la clínica. ')
        else:
            print('El paciente ya esta registrado en el sistema. ')

def agregar_medico():
    matricula = input('Ingrese la matricula del médico que quiere agregar: ')
    if matricula == '':
        print('Debe ingresar una matricula valida. ')
    else:
        if la_clinica.validar_existencia_medico(matricula) == False:
            nombre = input('Ingrese su nombre: ')
            if nombre == '':
                print('Debe ingresar un nombre valido. ')
            else:
                especialidades = []
                try:
                    numero_de_especialidades = int(input('Ingrese la cantidad de especialidades del médico. '))
                except ValueError:
                    raise ValorIncorrecto
                for x in range(numero_de_especialidades):
                    dias = []
                    esp = input('Ingrese una especialidad. ')
                    try:
                        numero_de_dias = int(input('Ingrese cuantos dias a la semana se antendera esta especialidad por el medico: '))
                    except ValueError:
                        raise ValorIncorrecto
                    for x in range(numero_de_dias):
                        try:
                            dia_semana = input('Ingrese un día de la semana: ')
                        except ValueError:
                            raise ValorIncorrecto
                        dias.append(dia_semana)
                    especialidades.append(Especialidad(esp, dias)) 
                la_clinica.agregar_medico(Medico(nombre, matricula, especialidades))
                print('Gracias. El médico fue registrado en el sistema de la clínica. ')
        else: 
            print('El médico ya esta registrado en el sistema. ')

def agendar_turno():
    dni = input('Ingrese el DNI del paciente: ')
    if la_clinica.validar_existencia_paciente(dni) == True:
        matricula = input('Ingrese la matricula del médico: ')
        if la_clinica.validar_existencia_medico(matricula) == True:
            especialidad = input('Ingrese la especialidad de la consulta: ')
            try:
                fecha_hora = datetime.strptime(input('Ingrese la fecha y hora del turno (aaaa-mm-dd hh:min): '), '%Y-%m-%d %H:%M')
            except ValueError:
                raise FormatoIncorrecto()

            if la_clinica.validar_especialidad_en_dia(la_clinica.obtener_medico_por_matricula(matricula), especialidad, la_clinica.obtener_dia_semana_en_espanol(fecha_hora).lower()) == True:
                if la_clinica.validar_turno_no_duplicado(matricula, fecha_hora) == 'no ex':
                    la_clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
                    print('Turno agendado con exito.')
                elif la_clinica.validar_turno_no_duplicado(matricula, fecha_hora) == 'ex':
                    print('El turno no se puede agendar porque ya existe ese mismo turno. ')
            else:
                print('Esa especialidad no esta disponible ese dia. ')
        else:
            print('El médico no esta registrado en el sistema. ')
    else:
        print('El paciente no esta registrado en el sistema. ')

def agregar_especialidad_a_medico():
    matricula = input('Ingresar matricula del médico: ')
    if la_clinica.validar_existencia_medico(matricula):
        especialidad_nombre = input('Ingresar nombre de la especialidad: ')
        if especialidad_nombre in la_clinica.obtener_medico_por_matricula(matricula).print_especialidades():
            print('El médico ya tiene esa especialidad registrada. ')
        else:
            dias = []
            try:
                numero_de_dias = int(input('Ingrese cuantos dias a la semana se antendera esta especialidad por el medico: '))
            except ValueError:
                raise ValorIncorrecto
            for x in range(numero_de_dias):
                dia_semana = input('Ingrese un día de la semana: ')
                if dia_semana.lower() != 'lunes' and dia_semana != 'martes' and dia_semana != 'miercoles' and dia_semana != 'jueves' and dia_semana != 'viernes' and dia_semana != 'sabado' and dia_semana != 'domingo':
                    print('Debe ingresar un dia de la semana valido. ')
                    return
                else:
                    dias.append(dia_semana)
            la_clinica.obtener_medico_por_matricula(matricula).agregar_especialidad(Especialidad(especialidad_nombre, dias))
            print('La especialidad fue agregada al perfil del medico.')
    else:
            print('El medico no esta registrado en el sistema!')

def emitir_receta():
    dni = input('Ingrese DNI del paciente: ')
    if la_clinica.validar_existencia_paciente(dni):
        matricula = input('Ingrese matricula del médico: ')
        if la_clinica.validar_existencia_medico(matricula):
            medicamentos = []
            try:
                numero_de_medicamentos = int(input('Ingrese la cantidad de medicamentos que iran en la receta: '))
            except ValueError:
                raise ValorIncorrecto
            if numero_de_medicamentos <= 0:
                print('Debe ingresar un numero mayor a 0. ')
                return
            for x in range(numero_de_medicamentos):
                med = input('Ingrese el nombre del medicamento: ')
                medicamentos.append(med)
                if med == '':
                    print('Debe ingresar un nombre de medicamento valido. ')
                    return
            print('Receta emitida con exito: ')  
            print(la_clinica.emitir_receta(dni, matricula, medicamentos))
        else:
            print('El médico no esta registrado en el sistema. ')
    else: 
        print('El paciente no esta registrado en el sistema.')
def ver_historia_clinica():
    dni = input('Ingrese el DNI del paciente: ')
    if la_clinica.validar_existencia_paciente(dni) == True:
        print(la_clinica.obtener_historia_clinica(dni))
    else:
        print('El paciente no esta registrado en el sistema de la clínica.')

def ver_todos_los_turnos():
    for turno in la_clinica.obtener_turnos():
        print(turno)
def ver_todos_los_pacientes():
    for paciente in la_clinica.obtener_pacientes():
        print(paciente)
def ver_todos_los_medicos():
    for medico in la_clinica.obtener_medicos():
        print(medico)
def salir():
    sys.exit()

def main():
    while True:
        try:
            opcion = menu_principal()
        except ValueError:
            raise ValorIncorrecto
        if opcion == 1:
            agregar_paciente()
            opcion = -1
        elif opcion == 2:
            agregar_medico()
            opcion = -1
        elif opcion == 3:
            agendar_turno()
            opcion = -1
        elif opcion == 4:
            agregar_especialidad_a_medico()
            opcion = -1
        elif opcion == 5:
            emitir_receta()
            opcion = -1
        elif opcion == 6:
            ver_historia_clinica()
            opcion = -1
        elif opcion == 7:
            ver_todos_los_turnos()
            opcion = -1
        elif opcion == 8:
            ver_todos_los_pacientes()
            opcion = -1
        elif opcion == 9:
            ver_todos_los_medicos()
            opcion = -1
        elif opcion == 0:
            salir()
            break


if __name__ == "__main__":
    main()