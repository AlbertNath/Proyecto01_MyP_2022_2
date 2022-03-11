import csv
class Entrada:
    
    def entrada(self, archivo):
        r = open(archivo, "r")
        lector = csv.reader(r)
        ticket = [] 
        linea  = 0
        for i in lector:
            ticket.append(i)
            linea += 1
        r.close()
        return ticket
    
    
    def carga_cache(self, datos:list):
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
    
    def ejecutar_entrada(self):
        cache = self.carga_cache((self.entrada("./csv/dataset1.csv")))
        return cache

