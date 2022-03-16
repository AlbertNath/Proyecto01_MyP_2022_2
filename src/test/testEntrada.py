import unittest
from main.entrada import *

class TestEntrada(unittest.TestCase):
    """Prueba unittest para Entradas"""

    def test_tickets(self):
        """Prueba de que los tickets sean del formato correcto"""
        clase = Entrada()
        archivo = "./csv/dataset1.csv"
        tickets = clase.leer_entrada(archivo)[0]
        for i in range(1,len(tickets)):
            self.assertRegex(tickets[i][0], '[A-Z]{3}', 'El formato de la ciudad es incorrecta')
            self.assertRegex(tickets[i][1], '[A-Z]{3}', 'El formato de la ciudad es incorrecta')
        for i in range(1,len(tickets)):
            self.assertRegex(tickets[i][2], '[+-]?[0-9]+\.[0-9]+', 'El formato de longitud o latitud es incorrecta')
            self.assertRegex(tickets[i][3], '[+-]?[0-9]+\.[0-9]+', 'El formato de longitud o latitud es incorrecta')
            self.assertRegex(tickets[i][4], '[+-]?[0-9]+\.[0-9]+', 'El formato de longitud o latitud es incorrecta')
            self.assertRegex(tickets[i][5], '[+-]?[0-9]+\.[0-9]+', 'El formato de longitud o latitud es incorrecta')

    def test_lineas(self):
        """Prueba que el número de tickets sean 3000"""
        clase = Entrada()
        archivo = "./csv/dataset1.csv"
        lineas = clase.leer_entrada(archivo)[1]
        self.assertEqual(lineas, 3000, 'El número de tickets no son 3000')
