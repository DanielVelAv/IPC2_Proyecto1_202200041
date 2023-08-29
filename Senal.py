from ListaSimple import ListaSimple
from Tiempo import Tiempo

class Senal:

    def __init__(self, nombre, tiempoMax, amplitudMax,tiempos):
       self.nombre = nombre
       self.tiempoMax = tiempoMax
       self.amplitudMax = amplitudMax
       self.tiempos = tiempos

    def getId(self):
        return self.nombre

    def getDato(self):
        return self.nombre
        return self.tiempoMax
        return self.amplitudMax
    def getNombre(self):
        return self.nombre
    
    def getTiempoMax(self):
        return self.tiempoMax
    
    def getAmplitudMax(self):
        return self.amplitudMax

    def getTiempos(self):
        return self.tiempos

class SenalBinaria:
    def __init__(self, nombre, listaEtiquetas):
        self.nombre = nombre
        self.listaEtiquetas = listaEtiquetas
        self.compararT()

    def compararT(self):
        listGrupos = ListaSimple()

        list = self.listaEtiquetas
        for i in range(self.listaEtiquetas.getSize()):
            for j in range(i+1,self.listaEtiquetas.getSize()):
                etiquetaA = list.buscarID(i)
                etiquetaB = list.buscarID(j)
                '''print("-------para if---------",etiquetaA.getEtiqueta())
                print("-------para if---------", etiquetaB.getEtiqueta())'''
                if etiquetaA.getEtiqueta() == etiquetaB.getEtiqueta():
                    #print("nombre Senal: ",self.nombre,"tiempo de la lista: ",etiquetaAc.getTiempo(),"String generado: "+etiquetaAc.getEtiqueta())
                    print("El patron: ",etiquetaA.getEtiqueta()," Del senal: ",self.nombre," En el tiempo: ",etiquetaA.getTiempo()," y ",etiquetaB.getTiempo(),"Son iguales")





class Etiqueta:
    def __init__(self,tiempo, etiqueta):
        self.tiempo = tiempo
        self.etiqueta = etiqueta
        '''self.getTiempoListado()'''

    def getTiempo(self):
        return self.tiempo

    def getEtiqueta(self):
        return self.etiqueta

    def getTiempoListado(self):
        print("--------------------------------")
        print("Tiempo: ", self.tiempo,"String patron: ", self.etiqueta)
        print("--------------------------------")

    def comparar(self):
        pass



