import csv, re

# Uso del método open() para abrir el archivo csv del proyecto
archivo = open('dataset1.csv')

# Uso del objeto csv.reader para leer el archivo
lector = csv.reader(archivo)

# Creación de una lista para leer la primera linea que es el encabezado
encabezado = []
encabezado = next(lector)
encabezado

# Prueba de que el encabezado sea del formato correcto
"""
def checar_encabezado(encabezado):
    for i in range(0,5):
        if 'origin' or 'destination' or 'origin_latitude' or 'origin_longitude' or 'destination_latitude' or 'destination_longitude' not in encabezado[i]:
            return False
        else:
            return True
# Salió AssertionError (Mar 5)
assert(checar_encabezado(encabezado))
"""

# Creación de una lista para leer los 3000 tickets
tickets = []
for i in lector:
    tickets.append(i)
tickets

# Prueba de que los tickets sean del formato correcto
def checar_ticket(tickets):
    for i in range(0,1):
        assert(re.search('[A-Z]{3}', tickets[i]))
    for i in range(2,5):
        assert(re.search('[+-]?[0-9]+\.[0-9]+', tickets[i]))
for i in range(len(tickets)):
    checar_ticket(tickets[i])


# Cerrar el archivo una vez terminado la lectura
archivo.close()

print(encabezado)

"""
Método para cargar un caché de origen.
Guardamos en un diccionario el código IATA y las coordenadas
de la ciudad.
NOTE (7/mar/22): ¿es impráctico hacer dos cachés, uno de
origen y otro de destino?
"""
def carga_cache(datos:list):
    cache = {}
    for i in range(len(datos)):
        if datos[i][0] in cache.keys():
            continue
        else:
            cache[datos[i][0]] = datos[i][2:4]
    return cache

prueba = carga_cache(tickets)
# Imprime llaves
print(prueba.keys())
# Imprime el diccionario
print(prueba)

# Nombre de ciudad
origen = tickets[0][0]
# Llave de ciudad
key = prueba[origen]
# Imprimir latitud y longitud de TLC
print(key[0], key[1])



"""
==PROBLEM==
Informe de clima de la ciudad de salida y la ciudad de llegada para 3,000 tickets
from dataset1.csv file

==INPUT==
Origin format :: 3 Characters (TLC, MTY, MEX)
Destination format :: 3 Characters (TLC, MTY, MEX)
origin_latitude :: 19.0000 ~ 25.9999
origin_longitude :: -99.0000 ~ -100.9999
destination_latitude :: 19.0000 ~ 25.9999
destination_longitude :: -99.0000 ~ -100.9999

==CSV will Look like this==
origin,destination,origin_latitude,origin_longitude,destination_latitude,destination_longitude
TLC,MTY,19.3371,-99.566,25.7785,-100.107
... 2998 lines...
GDL,MEX,20.5218,-103.311,19.4363,-99.0721

"""

from requests.models import HTTPError, Response
import requests as req
import sys

"""
Checamos por el código de respuesta; verificamos que no
se nos sean regresados códigos de error conocidos en la documentación:
https://openweathermap.org/faq#:~:text=of%20City%20IDs%3F-,API%20errors,-API%20calls%20return

requests ya tiene funciones para manejar malas respuestas:
https://docs.python-requests.org/en/latest/user/quickstart/#:~:text=Response%20Status%20Codes
"""
def comprueba_respuesta(respuesta:Response):
    if(respuesta.status_code != req.codes.ok):
        respuesta.raise_for_status()


"""
Una llmada simple a la API con la coordenadas de TLC.
NOTA: retirar los corchetes de los parámteros xd.
NOTA2: lo siguiente es lo equivalente a la línea comentada (de la primera prueba)
pero más bonito.
"""
url   = "http://api.openweathermap.org/data/2.5/weather"
param = {'lat': 19.3371, 'lon': -99.566, 'appid': '-APIKEY-', 'lang': 'es'}
datos = req.get(url, params=param)
#datos = req.get("http://api.openweathermap.org/data/2.5/weather?lat=19.3371&lon=-99.566&appid=-APIKEY-")


try:
    comprueba_respuesta(datos)
    #Cachar con Exception está muy sucio.
    #DONE: buscar una forma más específica de cachar el error.
except HTTPError:
    print("Respuesta errónea de la API; abortar. \nCódigo de error: {}".format(datos.status_code))
    sys.exit(1)


#print(datos.json())
datos = datos.json()
# JSON nos otroga un diccionario de diccionarios; en este caso weather es una lista
# con un único elemento (un diccionario) por lo que debemos cuidar cómo accedemos a
# sus elementos.
print(datos['weather'][0]['description'])

