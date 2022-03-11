import csv #Necesario para procesar los csv

class Entrada:
    """Clase para manejo de entrada"""

    def entrada(self, archivo):
        """
        Método para analizar un archivo csv y extraer una
        lista de listas con la información del archivo.
        """
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
        """"
        Método para crear un caché con todas las ciudades del
        csv sin repeticiones
        """
        cache = {}
        for i in range(2,len(datos)):
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
        """
        Método para leer y cargar en el caché la información del
        archivo csv
        """
        cache = self.carga_cache((self.entrada("./csv/dataset1.csv")))
        return cache

