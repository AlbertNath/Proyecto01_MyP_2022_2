import entrada, reporteClima
from entrada import *
from reporteClima import *

class main:

    entrada = Entrada()

    def datos_tickets(lst):
        for i in range(len(tickets)):
            origen = tickets[i][0] # Nombres de Ciudad de 3 caracteres
            destino = tickets[i][1]
            origenKey = cache[origen] # Llave de la ciudad
            destinoKey = cache[destino]
            datosOrigen = solicita_datos(float(origenKey[0]), float(origenKey[1])) 
            datosDestino = solicita_datos(float(destinoKey[0]), float(destinoKey[1]))
            respuestaOrigen = depura_respuesta(datosOrigen) # Respuestas
            respuestaDestino = depura_respuesta(datosDestino)
        
