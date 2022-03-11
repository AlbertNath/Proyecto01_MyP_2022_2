import unittest
from main.entrada import *

 # Prueba unittest para Entradas
class TestEntrada(unittest.TestCase):
    # Prueba de que los tickets sean del formato correcto
    def test_tickets(self):
        for i in range(len(tickets)):
            self.assertRegex(tickets[i][0], '[A-Z]{3}', 'El formato de la ciudad es incorrecta')
            self.assertRegex(tickets[i][1], '[A-Z]{3}', 'El formato de la ciudad es incorrecta')
        for i in range(len(tickets)):
            self.assertRegex(tickets[i][2], '[+-]?[0-9]+\.[0-9]+', 'El formato de longitud o latitud es incorrecta')
            self.assertRegex(tickets[i][3], '[+-]?[0-9]+\.[0-9]+', 'El formato de longitud o latitud es incorrecta')
            self.assertRegex(tickets[i][4], '[+-]?[0-9]+\.[0-9]+', 'El formato de longitud o latitud es incorrecta')
            self.assertRegex(tickets[i][5], '[+-]?[0-9]+\.[0-9]+', 'El formato de longitud o latitud es incorrecta')
    # Prueba que el número de tickets sean 3000
    def test_lineas(self):
        self.assertEqual(lineas, 3000, 'El número de tickets no son 3000')
