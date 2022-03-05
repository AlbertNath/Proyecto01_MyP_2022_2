import csv


archivo = open('dataset1.csv')


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
https://docs.python-requests.org/en/latest/user/quickstart/#:~:text=Response%20Status%20Codes%C2%B6
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

