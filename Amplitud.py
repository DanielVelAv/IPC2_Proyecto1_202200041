
class Amplitud:
    def __init__(self, Namplitud, dato = 0):
        self.Namplitud = Namplitud
        self.dato = dato
        '''self.print()'''

    def getNAmplitud(self):
        return self.Namplitud
    
    def getDato(self):
        return self.dato
    
    def print(self):
        print("---------Lista de datos---------")
        print("Tiempo: ",self.Namplitud,"Dato Guardado: ",self.dato)