from ListaSimple import ListaSimple
from Tiempo import Tiempo
from MatrizReducida import *

class Senal:
    def __init__(self, nombre, tiempoMax, amplitudMax,tiempos):
       self.nombre = nombre
       self.tiempoMax = tiempoMax
       self.amplitudMax = amplitudMax
       self.tiempos = tiempos

    def getId(self):
        return self.nombre

    def setID(self,id):
        self.id = id

    def getDato(self):
        return self.nombre
        return self.tiempoMax
        return self.amplitudMax

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre = nombre
    
    def getTiempoMax(self):
        return self.tiempoMax

    def setTiempoMax(self,tiempoMax):
        self.tiempoMax = tiempoMax
    
    def getAmplitudMax(self):
        return self.amplitudMax

    def setAmplitudMax(self,amplitudMax):
        self.amplitudMax = amplitudMax

    def getTiempos(self):
        return self.tiempos

    def setTiempos(self,tiempos):
        self.tiempos = tiempos

class SenalBinaria:
    def __init__(self, nombre, listaEtiquetas):
        self.nombre = nombre
        self.listaEtiquetas = listaEtiquetas
        self.listGrupos = ListaSimple()


    def getnombreSenal(self):
        return self.nombre

    def getListaEtiquetas(self):
        return self.listaEtiquetas

    def getDatosCoincidentes(self):
        return self.listGrupos

    def compararT(self,listaEtiquetas):

        list = listaEtiquetas
        li = listaEtiquetas.getInicio()

        '''while list:
            list2 = list.getSiguiente()
            print("lista: ", list.getDato().getEtiqueta())
            while list2:
                if list.getDato().getEtiqueta() == list2.getDato().getEtiqueta():
                    print("Elementos iguales: ", list.getDato().getEtiqueta()," ",list2.getDato().getEtiqueta())
                    Grupo = CoincidenciasBin(list.getDato().getEtiqueta(), list2.getDato().getEtiqueta(), self.nombre,list.getDato().getTiempo(), list2.getDato().getTiempo(), ll.getSize())
                    self.listGrupos.agregar(Grupo)
                list2 = list2.getSiguiente()
            list = list.getSiguiente()
            return Grupo'''

        '''for i in range(listaEtiquetas.getSize()):
            eti = list.buscarID(i)
            print(eti.getEtiqueta())'''


        for i in range(listaEtiquetas.getSize()):
            for j in range(i+1,listaEtiquetas.getSize()):
                etiquetaA = list.buscarID(i)
                etiquetaB = list.buscarID(j)
                '''print("-------para if---------", etiquetaA.getEtiqueta())
                print("-------para if---------", etiquetaB.getEtiqueta())'''
                if etiquetaA.getEtiqueta() is not None and etiquetaB.getEtiqueta() is not None:
                    if etiquetaA.getEtiqueta() == etiquetaB.getEtiqueta():
                        #print("nombre Senal: ",self.nombre,"tiempo de la lista: ",etiquetaAc.getTiempo(),"String generado: "+etiquetaAc.getEtiqueta())
                        print("El patron: ",etiquetaA.getEtiqueta()," Del senal: ",self.nombre," En el tiempo: ",etiquetaA.getTiempo()," y ",etiquetaB.getTiempo(),"Son iguales")
                        Grupo = CoincidenciasBin(etiquetaA.getEtiqueta(),etiquetaB.getEtiqueta(),self.nombre,etiquetaA.getTiempo(),etiquetaB.getTiempo(),list.getSize())
                        self.listGrupos.agregar(Grupo)

    def getListas(self):
        return self.listGrupos


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
