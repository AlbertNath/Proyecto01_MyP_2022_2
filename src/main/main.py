from aereopuerto import *
from salida import *
from entrada import *
from reporteClima import *

class main:

    # Intanciando clases
    entrada = Entrada()
    reporte = reporteClima()

    dic =  entrada.ejecutar_entrada() # Esto lee el csv de entrada
    respuestas = {}

    """
    Con el diccionaro limpio del csv, solicitamos datos a la API
    y depuramos respuestas para crear objetos e imprimir la información
    reelevante.
    """
    for key in dic:
        coordenadas = dic[key]
        resp = reporte.solicita_datos(float(coordenadas[0]),float(coordenadas[1]))
        dep = reporte.depura_respuesta(resp)

        puertito = aereopuerto(dep,key)

        print(puertito.toString())
