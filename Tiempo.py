from ListaSimple import ListaSimple
from Amplitud import Amplitud

class Tiempo:

    def __init__(self, nombre, amplitud):
        '''self.tiempo = tiempo'''
        self.nombre = nombre
        self.amplitud = amplitud
        self.listaAmplitudes = ListaSimple()
        '''self.llenarListadoAmplitudes()'''
        '''self.imprimir()'''
        #get nombre
        #self-amplitudes = Amplitudes() para tenerla definida, y evitar errores

    def getNombre(self):
        return self.nombre
    
    def getListaAmplitud(self):
        return self.amplitud
    
    def llenarListadoAmplitudes(self):
        for i in range(1, int(self.amplitud)+1):
            tmpAmplitud = Amplitud(i)
            self.listaAmplitudes.agregar(tmpAmplitud)

    def imprimir(self):
        print("------Tiempo/amplitud: ---------")
        objeto = self.amplitud.getInicio()
        while objeto != None:
            timp = objeto.getDato().getNAmplitud()
            print("Amplitud",timp,"id",self.nombre)
            objeto = objeto.getSiguiente()