import requests as req
from requests.models import HTTPError
import sys
sys.path.insert(1, '../../Proyecto01_MyP_2022_2/src/main')
import constantes as cons


class reporteClima:
        """
        Clase para realizar peticiones a la API de
        OpenWeatherMap. Recibimos un diccionario como datos limpios
        de entrada y procesamos.
        """
        
        def solicita_datos(self, latitud, longitud):
                """
                Método para pedir los datos de una localidad
                con base en sus coordenadas.
                Arroja los errores TypError si los argumentos
                no son float y HTTPError si el código de respuesta es de error.
                """
                try:
                        url = "http://api.openweathermap.org/data/2.5/weather"
                        if type(latitud) != float or type(longitud) != float:
                                raise TypeError('Formato de coordenadas inválido.')

                        parametros = {'lat'  : latitud,
                                      'lon'  : longitud,
                                      'appid': cons.LLAVES[0],
                                      'lang' : 'es',
                                      'units': 'metric'}
                        respuesta = req.get(url, params=parametros)

                        if(respuesta.status_code != req.codes.ok):
                                respuesta.raise_for_status()

                        respuesta = respuesta.json()
                        return respuesta
                except HTTPError:
                        print('Error al tratar de contactar a la API\nAbortando')
                        sys.exit(1)

        
        def depura_respuesta(self, respuesta):
                """
                Método para extraer los datos más reelevantes de una
                respuesta de la API.
                Arroja los errores TypeError si la respuesta no es un
                diccionario y ValueError si la respuesta está vacía.
                """
                if type(respuesta) != dict:
                        raise TypeError('Argumento inválido')
                
                if not bool(respuesta):
                        raise ValueError('Respuesta vacía')

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
