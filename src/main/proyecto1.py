import entrada, reporteClima
from entrada import *
from reporteClima import *


# Ejecución del archivo entrada.py para leer el archivo csv y guardar datos
exec('entrada')

# Ciclo para obtener los datos de todos los 3000 tickets
for i in range(len(tickets)):
    # Nombres de Ciudad de 3 caracteres
    origen = tickets[i][0]
    destino = tickets[i][1]
    # Llave de la ciudad
    origenKey = cache[origen]
    destinoKey = cache[destino]
    # Solicitud de datos con latitud y longitud 
    datosOrigen = solicita_datos(float(origenKey[0]), float(origenKey[1]))
    datosDestino = solicita_datos(float(destinoKey[0]), float(destinoKey[1]))
    # Respuestas
    respuestaOrigen = depura_respuesta(datosOrigen)
    respuestaDestino = depura_respuesta(datosDestino)
"""
Error mio en primer intento tratando de acceder latitud y longitud con origen[0] y origen[1]
Segundo error por meter parametros en la función solicita_datos sin convertirlos a float.
"""
