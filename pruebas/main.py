import requests as req

datos = req.get("http://api.openweathermap.org/data/2.5/weather?lat={19.3371}&lon={-99.566}&appid={-API_KEY-}")

print(datos.json())
