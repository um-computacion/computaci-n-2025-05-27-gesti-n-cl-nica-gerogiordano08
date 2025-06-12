import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch
import sys
sys.path.append('./src')
from cli_interfaz.main import *
class EspecialidadesTest(unittest.TestCase):
    @patch('builtins.input', side_effect=['2000', 'oculista', '1', 'lunes'])
    @patch('builtins.print')
    def test_agregar_especialidad_exitoso(self, mock_print, mock_input):
        la_clinica.__medicos__['2000'] = Medico('Test Medico', '2000', [])
        agregar_especialidad_a_medico()
        self.assertIn('oculista', la_clinica.obtener_medico_por_matricula('2000').print_especialidades())
    @patch('builtins.input', side_effect=['2000', 'oculista', '1', 'lunes'])
    @patch('builtins.print')
    def test_no_especialidad_duplicada(self, mock_print, mock_input):
        la_clinica.__medicos__['2000'] = Medico('Test Medico', '2000', [Especialidad('oculista', ['lunes'])])
        agregar_especialidad_a_medico()
        mock_print.assert_any_call('El médico ya tiene esa especialidad registrada. ')
    @patch('builtins.input', side_effect=['2000', 'oculista', '1', ''])
    @patch('builtins.print')
    def test_dia_semana_invalido(self, mock_print, mock_input):
        la_clinica.__medicos__['2000'] = Medico('Test Medico', '2000', [])
        agregar_especialidad_a_medico()
        mock_print.assert_any_call('Debe ingresar un dia de la semana valido. ')
    @patch('builtins.input', side_effect=['3000', 'oculista', '1', 'lunes'])
    @patch('builtins.print')
    def test_medico_no_existente(self, mock_print, mock_input):
        agregar_especialidad_a_medico()
        mock_print.assert_any_call('El medico no esta registrado en el sistema!')



if __name__ == '__main__':
    unittest.main()