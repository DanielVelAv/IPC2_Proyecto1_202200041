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


    def buscarID(self, dato):
        tmp = self.nodoInicio
        while tmp:
            if tmp.getId() == dato:
                return tmp.getDato()
            tmp = tmp.getSiguiente()
        return None

    def eliminarD(self,dato):
        tmp = self.nodoInicio
        anterior = None
        while tmp:
            if tmp.getDato() == dato:
                if anterior is None:
                    self.primero = tmp.getSiguiente()
                    tmp.getSiguiente = None
                else:
                    anterior.getSiguiente

