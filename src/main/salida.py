import sys
sys.path.insert(1, '../../Proyecto01_MyP_2022_2/src')

from reporteClima import *
from gui.interfaz import *

class Salida:
   
   def saca_gui(self, dic, reporte,gui, tv):
      """
      Método sca_gui, permite general la interfaz gráfica, insertando
      cada objeto en la tabla, depues de dar formato a cada elemento del 
      diccionario.
      @param dic,reporte,gui,tv. dic: diccionario a recorrer, reporte:
      objeto clase reporteClima, gui: objeto clase Interfaz, tv:  objeto treeview.
      """
      for key in dic:
         coordenadas = dic[key]
         resp = reporte.solicita_datos(float(coordenadas[0]),
                                       float(coordenadas[1]))
         dep = reporte.depura_respuesta(resp)
         puerto = aereopuerto(dep,key)
         gui.insertar(puerto,tv)

     
            

            
