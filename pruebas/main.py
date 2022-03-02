import requests as req

"""
Una llmada simple a la API con la coordenadas de TLC.
NOTA: retirar los corchetes de los parámteros xd.
"""
datos = req.get("http://api.openweathermap.org/data/2.5/weather?lat=19.3371&lon=-99.566&appid=7dde62e26895fcefea7a7aceb8e4c96d")

print(datos.json())
