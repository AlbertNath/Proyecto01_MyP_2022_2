from tkinter import *
from tkinter import ttk
import sys
sys.path.insert(1, '../../Proyecto01_MyP_2022_2/src/main')
from aereopuerto import *
from salida import *

class Interfaz:
    def __init__(self, ventana):
        """
        Inicializamos la ventana dando formato, título tamaño, color
        """
        self.ventana = ventana
        self.ventana.title("Reporte Clima")
        self.ventana.resizable(0,0)
        self.ventana['bg'] ='lavender'
    
    def create(self,ventana):
        """
        Método create. Damos tamaño,nombre a las columnas de nuestra ventana.
        @param ventana, ventana principal.
        @return tv, tv treeview
        """
        tv = ttk.Treeview(ventana, columns=("col1","col2", "col3",
                                            "col4", "col5", "col6"))
        tv.column("#0", width=142, anchor=CENTER)
        tv.column("col1",width=142,anchor=CENTER)
        tv.column("col2",width=142,anchor=CENTER)
        tv.column("col3",width=142,anchor=CENTER)
        tv.column("col4",width=170,anchor=CENTER)
        tv.column("col5",width=170,anchor=CENTER)
        tv.column("col6",width=142,anchor=CENTER)
        
        tv.heading("#0", text= "Aeropuerto",anchor=CENTER)
        tv.heading("col1",text= "Clima",anchor=CENTER)
        tv.heading("col2",text= "Descripción",anchor=CENTER)
        tv.heading("col3",text= "Tempertura C°",anchor=CENTER)
        tv.heading("col4",text= "Sensación térmica C°",anchor=CENTER)
        tv.heading("col5",text= "Velocidad viento m/s",anchor=CENTER)
        tv.heading("col6",text= "Nubosidad %",anchor=CENTER)
        tv.pack()
        return tv
    
    def insertar(self,aero, tv):
        """
        Método insertar. Permite insertar cada objeto con sus atributo correspondiente en 
        cada columna.
        @param. aero,tv. aero objeto de aeropuerto, tv, treeview
        """
        tv.insert("", END, text = aero.codigo_IATA,values = (aero.clima,
                                                             aero.descripcion,
                                                             aero.temperatura,
                                                             aero.sensacion_term,
                                                             aero.viento_vel,
                                                             aero.nubosidad) )

                                                             
    def ejecutar(self,dic,ventana_principal, reporte, salida):
        """
        Método ejecutar. Permite generar la GUI
        @param. dic, ventana_principal,eporte,salida
        """
        tv = self.create(ventana_principal)
        salida.saca_gui(dic,reporte, self, tv)
        ventana_principal.mainloop()
