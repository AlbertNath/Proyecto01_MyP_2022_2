import csv

# Uso del método open() para abrir el archivo csv del proyecto
archivo = open("dataset1.csv", "r")

# Uso del objeto csv.DictReader para leer el archivo a un Diccionario
lector = csv.reader(archivo)

# Variable contador para verificar el número de tickets
lineas = 0

# Creación de una lista para leer la primera linea que es el encabezado
encabezado = []
encabezado = next(lector)
encabezado

# Creación de una lista para leer los 3000 tickets
tickets = []
for i in lector:
    tickets.append(i)
    lineas += 1
tickets

# Cerrar el archivo una vez terminado la lectura
archivo.close()

# Método para cargar un caché de origen o destino.
def carga_cache(datos:list):
    cache = {}
    for i in range(len(datos)):
        if datos[i][0] in cache.keys():
            continue
        else:
            cache[datos[i][0]] = datos[i][2:4]
        if datos[i][1] in cache.keys():
            continue
        else:
            cache[datos[i][1]] = datos[i][4:6]
    return cache

# Asignación diccionario que contendrá latitud y longitud de cada ciudad
cache = carga_cache(tickets)


#print(cache.keys())
#print(cache)



