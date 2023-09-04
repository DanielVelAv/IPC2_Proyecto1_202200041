from ListaSimple import ListaSimple
from Amplitud import Amplitud

class Tiempo:

    def __init__(self, nombre, amplitud):
        self.nombre = nombre
        self.amplitud = amplitud
        self.listaAmplitudes = ListaSimple()

    def getNombre(self):
        return self.nombre
    
    def getListaAmplitud(self):
        return self.amplitud
    
    def llenarListadoAmplitudes(self):
        for i in range(1, int(self.amplitud)+1):
            tmpAmplitud = Amplitud(i)
            self.listaAmplitudes.agregar(tmpAmplitud)
