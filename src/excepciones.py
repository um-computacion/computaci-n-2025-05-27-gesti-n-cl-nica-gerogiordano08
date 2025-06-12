
class PacienteNoEncontrado(Exception):
    def __init__(self, message='El paciente requerido NO existe.'):
        super().__init__(message)
class MedicoNoDisponible(Exception):
    def __init__(self, message='El médico solicitado no esta disponible.'):
        super().__init__(message)
class TurnoOcupado(Exception):
    def __init__(self, message='El turno solicitado ya esta ocupado.'):
        super().__init__(message)
class RecetaInvalida(Exception):
    def __init__(self, message='La receta ingresada es invalida.'):
        super().__init__(message)
class TurnoExiste(Exception):
    def __init__(self, message='El turno que intentas ingresar ya existe.'):
        super().__init__(message)
class FormatoIncorrecto(Exception):
    def __init__(self, message= 'El formato de la fecha fue ingresado incorrectamente'):
        super().__init__(message)
class ValorIncorrecto(Exception):
    def __init__(self, message='Debes introducir un número!'):
        super().__init__(message)