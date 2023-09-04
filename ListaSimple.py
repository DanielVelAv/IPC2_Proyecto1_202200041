from Nodo import Nodo
import graphviz
import Grafica

class ListaSimple():
    id = 0

    def __init__(self):
        self.primero = None
        self.nodoInicio = None
        self.nodoFinal = None
        self.size = 0

    def getInicio(self):
        return self.nodoInicio

    def getSize(self):
        return self.size
    
    def estaVacia(self):
        return self.nodoInicio == None
    
    def agregar(self, dato):
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.estaVacia():
            self.nodoInicio = nuevo
            self.nodoFinal = nuevo
        else:
            self.nodoFinal.setSiguiente(nuevo)
            self.nodoFinal = nuevo
        self.size += 1

    def graficar(self, nombreArchivo):

        graph = Grafica.Graphics(nombreArchivo)

        for i in range(self.getSize()):
            tmp = self.buscarID(i)
            tiempos = tmp.getTiempos()
            for j in range(tiempos.getSize()):
                actualT = tiempos.buscarID(j)
                amplitudes = actualT.getListaAmplitud()
                for k in range(amplitudes.getSize()):
                    actualA = amplitudes.buscarID(k)
        graph.add()
        graph.generar()


    def buscarID(self, dato):
        tmp = self.nodoInicio
        while tmp:
            if tmp.getId() == dato:
                return tmp.getDato()
            tmp = tmp.getSiguiente()
        return None

