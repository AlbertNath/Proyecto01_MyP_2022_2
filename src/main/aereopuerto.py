class aereopuerto:
    """
    Clase para represenar un aereopuerto.
    """
    def __init__(self, respDepurada:dict, codigo:str):
        """
        Constructor de clase
        """
        self.codigo_IATA = codigo
        self.clima = respDepurada['clima']
        self.descripcion = respDepurada['descripcion']
        self.temperatura = respDepurada['temperatura']
        self.sensacion_term = respDepurada['sensacion_term']
        self.viento_vel = respDepurada['sensacion_term']
        self.nubosidad = respDepurada['nubosidad']
