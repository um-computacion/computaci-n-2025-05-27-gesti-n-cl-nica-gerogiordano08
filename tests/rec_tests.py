import unittest
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append('./src')
from cli_interfaz.main import *
from src.historia_clinica import HistoriaClinica

class RecetasTest(unittest.TestCase):
    def setUp(self):
        la_clinica.__pacientes__.clear()
        la_clinica.__medicos__.clear()
        la_clinica.__historias_clinicas__.clear()
    @patch('builtins.input', side_effect=['999', '888', '2', 'Aspirina', 'Paracetamol'])
    @patch('builtins.print')
    def test_emitir_receta_exitoso(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__medicos__['888'] = Medico('Test Medico', '888', [Especialidad('Cardiología', ['lunes'])])
        la_clinica.__pacientes__['999'] = Paciente('Test Paciente', '999', '2001-01-01')
        la_clinica.__historias_clinicas__['999'] = HistoriaClinica(la_clinica.__pacientes__['999'], [], [])
        emitir_receta()
        mock_print.assert_any_call('Receta emitida con exito: ')
    @patch('builtins.input', side_effect=['999', '888', '2', 'Aspirina', 'Paracetamol'])
    @patch('builtins.print')
    def test_emitir_receta_medico_no_existente(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__pacientes__['999'] = Paciente('Test Paciente', '999', '2001-01-01')
        emitir_receta()
        mock_print.assert_any_call('El médico no esta registrado en el sistema. ')
    @patch('builtins.input', side_effect=['999', '888', '2', 'Aspirina', 'Paracetamol'])
    @patch('builtins.print')
    def test_emitir_receta_paciente_no_existente(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__medicos__['888'] = Medico('Test Medico', '888', [Especialidad('Cardiología', ['lunes'])])
        emitir_receta()
        mock_print.assert_any_call('El paciente no esta registrado en el sistema.')
    @patch('builtins.input', side_effect=['999', '888', '2', '', 'Paracetamol'])
    @patch('builtins.print')
    def test_emitir_receta_medicamento_vacio(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__medicos__['888'] = Medico('Test Medico', '888', [Especialidad('Cardiología', ['lunes'])])
        la_clinica.__pacientes__['999'] = Paciente('Test Paciente', '999', '2001-01-01')
        emitir_receta()
        mock_print.assert_any_call('Debe ingresar un nombre de medicamento valido. ')
    @patch('builtins.input', side_effect=['999', '888', '0',])
    @patch('builtins.print')
    def test_emitir_receta_cantidad_medicamentos_cero(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__medicos__['888'] = Medico('Test Medico', '888', [Especialidad('Cardiología', ['lunes'])])
        la_clinica.__pacientes__['999'] = Paciente('Test Paciente', '999', '2001-01-01')
        emitir_receta()
        mock_print.assert_any_call('Debe ingresar un numero mayor a 0. ')
if __name__ == '__main__':
    unittest.main()