import unittest
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cli_interfaz.main import *
from src.historia_clinica import HistoriaClinica

class HistoriaClinicaTests(unittest.TestCase):
    def setUp(self):
        la_clinica.__pacientes__.clear()
        la_clinica.__medicos__.clear()
        la_clinica.__historias_clinicas__.clear()

    @patch('builtins.input', side_effect=['999', '888', '2', 'Aspirina', 'Paracetamol'])
    @patch('builtins.print')
    def test_receta_registrada_correctamente_en_historia(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__pacientes__['999'] = Paciente('Test Paciente', '999', '2001-01-01')
        la_clinica.__medicos__['888'] = Medico('Test Medico', '888', [Especialidad('Cardiología', ['lunes'])])
        la_clinica.__historias_clinicas__['999'] = HistoriaClinica(la_clinica.__pacientes__['999'], [], [])
        emitir_receta()
        self.assertEqual(la_clinica.obtener_historia_clinica('999').obtener_recetas()[0].__medicamentos__, ['Aspirina', 'Paracetamol'])
        self.assertEqual(la_clinica.obtener_historia_clinica('999').obtener_recetas()[0].__paciente__.__dni__, '999')
        self.assertEqual(la_clinica.obtener_historia_clinica('999').obtener_recetas()[0].__medico__.__matricula__, '888')
    @patch('builtins.input', side_effect=['999', '888', 'Cardiología', '2025-06-30 10:00'])
    @patch('builtins.print')
    def test_turno_registrado_correctamente_en_historia(self, mock_print, mock_input):
        self.setUp()
        la_clinica.__pacientes__['999'] = Paciente('Test Paciente', '999', '2001-01-01')
        la_clinica.__historias_clinicas__['999'] = HistoriaClinica(la_clinica.obtener_paciente_por_dni('999'), [], [])
        la_clinica.__medicos__['888'] = Medico('Test Medico', '888', [Especialidad('Cardiología', ['lunes'])])
        agendar_turno()
        self.assertEqual(la_clinica.obtener_historia_clinica('999').obtener_turnos()[0].__paciente__.__dni__, '999')
        self.assertEqual(la_clinica.obtener_historia_clinica('999').obtener_turnos()[0].__medico__.__matricula__, '888')
    @patch('builtins.input', side_effect=['999'])
    @patch('builtins.print')
    def test_historia_clinica_no_existe(self, mock_print, mock_input):
        self.setUp()
        ver_historia_clinica()
        mock_print.assert_any_call('El paciente no esta registrado en el sistema de la clínica.')
if __name__ == '__main__':
    unittest.main()