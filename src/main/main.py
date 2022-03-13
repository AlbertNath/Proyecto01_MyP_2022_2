from salida import *

#from entrada import *
#from reporteClima import *
#from gui.interfaz import *
#from aereopuerto import *


class main:

    # Intanciando clases
    entrada = Entrada()
    reporte = reporteClima()
    salida  = Salida() 
    gui = Interfaz()

    dic =  entrada.ejecutar_entrada() # Esto lee el csv de entrada
    gui.ejecutar(salida.sal(dic, reporte, gui))
    
    """
    Con el diccionaro limpio del csv, solicitamos datos a la API
    y depuramos respuestas para crear objetos e imprimir la información
    reelevante.
    """
    """
    for key in dic:
        coordenadas = dic[key]
        resp = reporte.solicita_datos(float(coordenadas[0]),float(coordenadas[1]))
        dep = reporte.depura_respuesta(resp)

        puertito = aereopuerto(dep,key)

        print(puertito.toString())
"""
