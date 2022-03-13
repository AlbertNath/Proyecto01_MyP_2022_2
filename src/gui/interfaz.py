from tkinter import *
from tkinter import ttk
from main.aeropuerto import *
from main.salida import *

class Interfaz:
    def __init__(self, ventana):
        #Inicializamos la ventana con un títilo
        self.ventana = ventana
        self.ventana.title("Reporte Clima")
        self.ventana.geometry('1000x300')
        self.ventana['bg'] ='lavender'
        
    def treev(self,ventana):
        tv = ttk.Treeview(ventana, columns=("col1","col2", "col3",
                                            "col4", "col5", "col6"))
        tv.column("#0", width=142, anchor=CENTER)
        tv.column("col1",width=142,anchor=CENTER)
        tv.column("col2",width=142,anchor=CENTER)
        tv.column("col3",width=142,anchor=CENTER)
        tv.column("col4",width=144,anchor=CENTER)
        tv.column("col5",width=143,anchor=CENTER)
        tv.column("col6",width=142,anchor=CENTER)
        tv.heading("#0", text= "Aeropuerto",anchor=CENTER)
        tv.heading("col1",text= "Clima",anchor=CENTER)
        tv.heading("col2",text= "Descripción",anchor=CENTER)
        tv.heading("col3",text= "Tempertura",anchor=CENTER)
        tv.heading("col4",text= "Sensación térmica",anchor=CENTER)
        tv.heading("col5",text= "Velocidad viento",anchor=CENTER)
        tv.heading("col6",text= "Nubosidad",anchor=CENTER)
        tv.pack()

    def datos(self, aero):
        tv.insert("", END, text = aero.codigo_IATA,values = (aero.clima,
                                                             aero.descripcion,
                                                             aero.temperatura,
                                                             aero.sensacion_term,
                                                             aero.viento_vel,
                                                             aero.nubosidad) )
    def ejecutar(dic):
        ventana_principal = Tk()
        reporte_clima =Interfaz(ventana_principal)
        treev(ventana_principal)
        salida(dic)
        ventana_principal.mainloop()

