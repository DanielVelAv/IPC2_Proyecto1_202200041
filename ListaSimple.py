from Nodo import Nodo
from Graphviz import Graph

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
        graph = Graph(nombreArchivo)
        tmp = self.nodoInicio
        while tmp != None:
            graph.add(tmp, tmp.getSiguiente())
            tmp = tmp.getSiguiente()
        graph.generar()

    def convertirBin(self):
        tmp = self.nodoInicio
        while tmp != None:
            if(int(tmp.getDato())>=1):
                tmp.setDato(1)
            tmp = tmp.getSiguiente()

    def buscarID(self, dato):
        tmp = self.nodoInicio
        while tmp:
            if tmp.getId() == dato:
                return tmp.getDato()
            tmp = tmp.getSiguiente()
        return None

    def Imprimir(self):
        tmp = self.nodoInicio
        while tmp != None:
            print(tmp.getDato())
            tmp = tmp.getSiguiente()
