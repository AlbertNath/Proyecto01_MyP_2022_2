import requests as req
import sys
import os
import constantes as cons
"""
SCRIPT_DIR = os.path.dirname(os.path.abspath('constantes'))
sys.path.append(os.path.dirname(SCRIPT_DIR))
"""
class reporteClima:
    
    url = "http://api.openweathermap.org/data/2.5/weather" # String general para declararlo solo una vez
    """
    Métodos para solicitar una petición a la API de
    OpenWeatherMap. Recibimos un {?} como datos limpios
    de entrada y procesamos
    """


    def solicita_datos(latitud, longitud):
        if type(latitud) != float or type(longitud) != float:
            raise TypeError('Formato de coordenadas inválido.')
        # Comprobamos que los argumentos sean de tipo flotante
        # pues la API requiere este tipo en las coordenadas.

        parametros = {'lat'  : latitud,
                      'lon'  : longitud,
                      'appid': cons.LLAVES[0],
                      'lang' : 'es',
                      'units': 'metric'}
        respuesta = req.get(url, params=parametros)        
        if(respuesta.status_code != req.codes.ok):
            respuesta.raise_for_status()
            """
            Checamos por el código de respuesta; verificamos que no
            se nos sean regresados códigos de error conocidos en la documentación:
            https://openweathermap.org/faq#:~:text=of%20City%20IDs%3F-,API%20errors,-API%20calls%20return
            requests ya tiene funciones para manejar malas respuestas:
            https://docs.python-requests.org/en/latest/user/quickstart/#:~:text=Response%20Status%20Codes
            """
        respuesta = respuesta.json() # Una vez que comprobamos que la respuesta sea válida, la transformamos en un formato JSON.
        return respuesta
        """
        Método para pedir los datos de una localidad
        con base en sus coordenadas.
        @Throws: TypError si los argumentos no son float.
        HTTPError si el código de respuesta es de error.
        """


    def depura_respuesta(respuesta):
        if type(respuesta) != dict:
            raise TypeError('Argumento inválido')
       
        if not bool(respuesta):
            raise ValueError('Respuesta vacía')
        # Seleccionamos los datos de la respuesta para la salida.
        try:
            informacion_clima = {
                'clima'          : respuesta['weather'][0]['main'],
                'descripcion'    : respuesta['weather'][0]['description'],
                'temperatura'    : respuesta['main']['temp'],
                'sensacion_term' : respuesta['main']['feels_like'],
                'viento_vel'     : respuesta['wind']['speed'],
                'nubosidad'      : respuesta['clouds']['all']
            }
        except KeyError:
            print('Error al depurar datos\nAbortando...')
            sys.exit(1)
            
        return informacion_clima

    """
    Método para extraer los datos más reelevantes de una
    respuesta de la API.
    """
