import sys
sys.path.insert(1, '../../Proyecto01_MyP_2022_2/src/main')

from salida import *
from entrada import *
from reporteClima import *
from gui.interfaz import *
from aereopuerto import *
from tkinter import *


class main:

    """Instanciando clases"""
    entrada = Entrada()
    reporte = reporteClima()
    salida  = Salida() 
    ventana_principal = Tk()
    gui = Interfaz(ventana_principal)
    """Lectura de csv de entrda"""
    dic =  entrada.ejecutar_entrada()
    """Ejecutamos GUI"""
    gui.ejecutar(dic,ventana_principal,reporte,salida)
   
