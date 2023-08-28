from ListaSimple import ListaSimple
from Tiempo import Tiempo

class Senal:

    def __init__(self, nombre, tiempoMax, amplitudMax,tiempos):
       self.nombre = nombre
       self.tiempoMax = tiempoMax
       self.amplitudMax = amplitudMax
       self.tiempos = tiempos
       self.imprimir()

    def getId(self):
        return self.nombre

    def getNombre(self):
        return self.nombre
    
    def getTiempoMax(self):
        return self.tiempoMax
    
    def getAmplitudMax(self):
        return self.amplitudMax

    def getTiempos(self):
        return self.tiempos

    def imprimir(self):
        print("--------lista de Senales-----------")
        tmpl = self.tiempos.getInicio()
        while tmpl != None:
            print(self.nombre)
            tmpl = tmpl.getSiguiente()

        for i in range(3):
            print(self.nombre)