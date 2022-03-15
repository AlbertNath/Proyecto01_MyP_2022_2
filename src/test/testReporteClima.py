"""
Un truco para que el archivo a evaluar en otro directorio
sea accesible por el intérprete.
"""
import sys
import os
"""
SCRIPT_DIR = os.path.dirname(os.path.abspath('reporteClima'))
sys.path.append(os.path.dirname(SCRIPT_DIR))
"""
import unittest
from main.reporteClima import *

class TestReporteClima(unittest.TestCase):
    
    def test_argumentos_solicita_datos(self):
        self.assertRaises(TypeError, solicita_datos, 'eggs', 12)

    def test_depura_respuesta(self):
        self.assertRaises(TypeError, depura_respuesta, [])
        self.assertRaises(ValueError, depura_respuesta, {})
