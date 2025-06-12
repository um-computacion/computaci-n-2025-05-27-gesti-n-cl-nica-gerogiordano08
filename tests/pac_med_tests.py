import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch
from cli_interfaz.main import *

class PacientesMedicosTest(unittest.TestCase):
    def setUp(self):
        la_clinica.__pacientes__.clear()
        la_clinica.__medicos__.clear()
        la_clinica.__historias_clinicas__.clear()
    @patch('builtins.input', side_effect=['999', 'Test Paciente', '2001-01-01'])
    @patch('builtins.print')
    def test_registro_paciente_exitoso(self, mock_print, mock_input):
        self.setUp()
        agregar_paciente()
        self.assertIn('999', la_clinica.__pacientes__)
        self.assertIn('999', la_clinica.__historias_clinicas__)
        mock_print.assert_any_call('Gracias. El paciente fue registrado en el sistema de la clínica. ')

    @patch('builtins.input', side_effect=['888', 'Test Medico', '1', 'Cardiología', '1', 'lunes'])
    @patch('builtins.print')
    def test_registro_medico_exitoso(self, mock_print, mock_input):
        self.setUp()
        agregar_medico()
        self.assertIn('888', la_clinica.__medicos__)
        mock_print.assert_any_call('Gracias. El médico fue registrado en el sistema de la clínica. ')
    
    @patch('builtins.input', side_effect=['999', 'Otro Paciente', '1990-05-05'])
    @patch('builtins.print')
    def test_no_registro_paciente_duplicado(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__pacientes__['999'] = Paciente('Otro Paciente', '999', '1990-05-05')
        agregar_paciente()
        mock_print.assert_any_call('El paciente ya esta registrado en el sistema. ')

    @patch('builtins.input', side_effect=['888', 'Otro Medico', '1', 'Clínica', '1', 'martes'])
    @patch('builtins.print')
    def test_no_registro_medico_duplicado(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__medicos__['888'] = Medico('Otro Medico', '888', [Especialidad('Clínica', ['martes'])]) 
        agregar_medico()
        mock_print.assert_any_call('El médico ya esta registrado en el sistema. ')
    
    @patch('builtins.input', side_effect=['', 'Test Paciente', '2001-01-01'])
    @patch('builtins.print')
    def test_registro_paciente_dni_vacio(self, mock_print, mock_input):
        self.setUp()
        agregar_paciente()
        self.assertNotIn('1000', la_clinica.__pacientes__)


    @patch('builtins.input', side_effect=['1000', '', '2001-01-01'])
    @patch('builtins.print')
    def test_registro_paciente_nombre_vacio(self, mock_print, mock_input):
        self.setUp()
        agregar_paciente()
        self.assertNotIn('1000', la_clinica.__pacientes__)

    @patch('builtins.input', side_effect=['1001', 'Test Paciente', ''])
    @patch('builtins.print')
    def test_registro_paciente_fecha_invalida(self, mock_print, mock_input):
        self.setUp()
        agregar_paciente()
        self.assertNotIn('1001', la_clinica.__pacientes__)

    @patch('builtins.input', side_effect=['', 'Test Medico', '1', 'Cardiología', '1', 'lunes'])
    @patch('builtins.print')
    def test_registro_medico_matricula_vacia(self, mock_print, mock_input):
        self.setUp()
        agregar_medico()
        self.assertNotIn('2000', la_clinica.__medicos__)

    @patch('builtins.input', side_effect=['2000', '', '1', 'Cardiología', '1', 'lunes'])
    @patch('builtins.print')
    def test_registro_medico_nombre_vacio(self, mock_print, mock_input):
        self.setUp()
        agregar_medico()
        self.assertNotIn('2000', la_clinica.__medicos__)

    @patch('builtins.input', side_effect=['2001', 'Test Medico', 'uno', 'Cardiología', '1', 'lunes'])
    @patch('builtins.print')
    def test_registro_medico_especialidades_invalido(self, mock_print, mock_input):
        self.setUp()
        with self.assertRaises(Exception):
            agregar_medico()




if __name__ == '__main__':
    unittest.main()