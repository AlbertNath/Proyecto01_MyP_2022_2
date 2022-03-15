"""
Un truco para que el archivo a evaluar en otro directorio
sea accesible por el intérprete.
"""
import sys
import os

#SCRIPT_DIR = os.path.dirname(os.path.abspath('reporteClima'))
#sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest
from  main.reporteClima import *

class TestReporteClima(unittest.TestCase):
    """"Test para los métodos de la clase reporteClima"""

    def test_argumentos_solicita_datos(self):
        """Verifica que los argumentos sean correctos."""
        self.assertRaises(TypeError, reporteClima.solicita_datos, 'eggs', 12)

    def test_depura_respuesta(self):
        """
        Verifica que el argumento sea de tipo dict y que
        no sea vacío.
        """
        self.assertRaises(TypeError, reporteClima.depura_respuesta, [])
        self.assertRaises(ValueError, reporteClima.depura_respuesta, 'respuesta', {})
