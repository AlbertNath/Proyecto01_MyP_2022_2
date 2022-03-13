from reporteClima import *
from gui.interfaz import *

class Salida:
    
    def salida(self, datos):
        """Método para recorrer un diccionario e imprimir sus valores"""
        for elementos  in datos.items():
            print(elementos)
            
    def sal(self, dic, reporte,gui):
        for key in dic:
            coordenadas = dic[key]
            resp = reporte.solicita_datos(float(coordenadas[0]),
                                          float(coordenadas[1]))
            dep = reporte.depura_respuesta(resp)
            puerto = aereopuerto(dep,key)
            gui.datos(puerto)
            

            
