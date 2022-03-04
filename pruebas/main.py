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
