from ListaSimple import ListaSimple
from Amplitud import Amplitud

class Tiempo:

    def __init__(self, tiempo, amplitud):
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.listaAmplitudes = ListaSimple()
        self.llenarListadoAmplitudes()
        self.imprimir()

    def getTiempo(self):
        return self.tiempo
    
    def getAmplitud(self):
        return self.amplitud
    
    def llenarListadoAmplitudes(self):
        for i in range(1, int(self.amplitud)+1):
            tmpAmplitud = Amplitud(i)
            self.listaAmplitudes.agregarFinal(tmpAmplitud)

    def imprimir(self):
        print("-------Amplitudes para el tiempo-------", self.getTiempo())
        objeto = self.listaAmplitudes.getInicio()
        while objeto != None:
            print(objeto.getDato().getAmplitud())
            objeto = objeto.getSiguiente()