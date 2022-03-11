import csv
class Entrada:
    
    def entrada(archivo):
        lector = csv.reader(open(archivo, "r"))
        archivo.close()
        return lector
    
    def tickets(lst):
        ticket = []
        linea  = 0
        for i in lst:
            ticket.append(i)
            linea += 1
        return ticket
    
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
    
    def ejecutar_entrada():
        cache = carga_cache(tickets(entrada("./csv/dataset1.csv")))
        return cache

