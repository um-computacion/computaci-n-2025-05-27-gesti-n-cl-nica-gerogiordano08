import unittest
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append('./src')
from cli_interfaz.main import *
from src.historia_clinica import HistoriaClinica
class TurnosTest(unittest.TestCase):
    def setUp(self):
        self.la_clinica = la_clinica
        self.la_clinica.__pacientes__.clear()
        self.la_clinica.__historias_clinicas__.clear()
        self.la_clinica.__medicos__.clear()
        self.la_clinica.__turnos__.clear()
    @patch('builtins.input', side_effect=['999', '888', 'cardiologia', '2025-06-30 14:30'])
    @patch('builtins.print')
    def test_agendar_turno_exitoso(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__pacientes__['999'] = Paciente('Test Paciente', '999', '2001-01-01')
        la_clinica.__historias_clinicas__['999'] = HistoriaClinica(la_clinica.obtener_paciente_por_dni('999'), [], [])
        la_clinica.__medicos__['888'] = Medico('Test Medico', '888', [Especialidad('cardiologia', ['lunes'])])
        agendar_turno()
        mock_print.assert_any_call('Turno agendado con exito.')
    
    @patch('builtins.input', side_effect=[ '999', '888', 'cardiologia', '2025-06-30 14:30', '999', '888', 'cardiologia', '2025-06-30 14:30'])
    @patch('builtins.print')
    def test_agendar_turno_duplicado(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__pacientes__['999'] = Paciente('Test Paciente', '999', '2001-01-01')
        la_clinica.__historias_clinicas__['999'] = HistoriaClinica(la_clinica.obtener_paciente_por_dni('999'), [], [])
        la_clinica.__medicos__['888'] = Medico('Test Medico', '888', [Especialidad('cardiologia', ['lunes'])])
        agendar_turno()
        agendar_turno()
        mock_print.assert_any_call('El turno no se puede agendar porque ya existe ese mismo turno. ')
    @patch('builtins.input', side_effect=['999', '888', 'cardiologia', '2025-06-30 14:30'])
    @patch('builtins.print')
    def test_agendar_turno_paciente_no_existente(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__medicos__['888'] = Medico('Test Medico', '888', [Especialidad('cardiologia', ['lunes'])])
        agendar_turno()
        mock_print.assert_any_call('El paciente no esta registrado en el sistema. ')
    @patch('builtins.input', side_effect=['999', '888', 'cardiologia', '2025-06-30 14:30'])
    @patch('builtins.print')
    def test_agendar_turno_medico_no_existente(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__pacientes__['999'] = Paciente('Test Paciente', '999', '2001-01-01')
        la_clinica.__historias_clinicas__['999'] = HistoriaClinica(la_clinica.obtener_paciente_por_dni('999'), [], [])
        agendar_turno()
        mock_print.assert_any_call('El médico no esta registrado en el sistema. ')
    @patch('builtins.input', side_effect=['999', '888', 'cardiologia', '2025-06-30 14:30'])
    @patch('builtins.print')
    def test_agendar_turno_especialidad_no_disponible(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__pacientes__['999'] = Paciente('Test Paciente', '999', '2001-01-01')
        la_clinica.__historias_clinicas__['999'] = HistoriaClinica(la_clinica.obtener_paciente_por_dni('999'), [], [])
        la_clinica.__medicos__['888'] = Medico('Test Medico', '888', [Especialidad('dermatologia', ['lunes'])])
        agendar_turno()
        mock_print.assert_any_call('Esa especialidad no esta disponible ese dia. ')
if __name__ == '__main__':
    unittest.main()