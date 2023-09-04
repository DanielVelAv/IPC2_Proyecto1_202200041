
import xml.etree.ElementTree as ET

import Grafica
from ListaSimple import ListaSimple
from Amplitud import *
from Tiempo import *
from Senal import *
from Grafica import *
import copy

class LecturaXML():
    def __init__(self, path):
        self.raiz = ET.parse(path).getroot()
        self.ListasS = ListaSimple()
        self.ListasB = ListaSimple()

    def getSenal(self):

        Senales = self.ListasS

        for i in self.raiz.findall('senal'):
            nombreS = i.get('nombre')
            tiempoMax = int(i.get('t'))
            amplitudMax = i.get('a')
            tiempos = ListaSimple()

            for j in range(1, tiempoMax + 1):
                amplitudes = ListaSimple()
                for k in i.findall("dato"):
                    if int(k.attrib['t']) == j:

                        nuevaA = Amplitud(k.get('A'), k.text)
                        amplitudes.agregar(nuevaA)

                nuevo_t = Tiempo(j, amplitudes)
                tiempos.agregar(nuevo_t)
            nueva_S = Senal(nombreS, tiempoMax, amplitudMax, tiempos)
            Senales.agregar(nueva_S)
        return Senales

    def imprimir(self):

        Senales = self.ListasS

        for i in range(Senales.getSize()):
            actualSenal = Senales.buscarID(i)
            print("-------Senal: ",actualSenal.getNombre(),"-------")
            tiempos = actualSenal.getTiempos()
            for j in range(tiempos.getSize()):
                actualTiempo = tiempos.buscarID(j)
                print("Tiempo:   ",actualTiempo.getNombre())
                amplitudes = actualTiempo.getListaAmplitud()
                for k in range(amplitudes.getSize()):
                    actualAmplitud = amplitudes.buscarID(k)
                    print("Amplitud: ",actualAmplitud.getNAmplitud(),"Dato", actualAmplitud.getDato())




    def list_bin(self):

        Senales = self.ListasS
        SenalesBinarios = ListaSimple()

        for i in range(Senales.getSize()):
            ListaEtiquetasBin = ListaSimple()
            actualSenal = Senales.buscarID(i)
            tiempos = actualSenal.getTiempos()
            for j in range(tiempos.getSize()):
                strEtiqueta = ""
                actualTiempo = tiempos.buscarID(j)
                amplitudes = actualTiempo.getListaAmplitud()
                for k in range(amplitudes.getSize()):
                    actualAmplitud = amplitudes.buscarID(k)
                    if int(actualAmplitud.getDato()) > 0:
                        strEtiqueta += "1"
                    else:
                        strEtiqueta += "0"
                SenalStr = Etiqueta(actualTiempo.getNombre(), strEtiqueta)
                print("La lista convertida a binaria es: ",strEtiqueta)
                ListaEtiquetasBin.agregar(SenalStr)
            SenalBin = SenalBinaria(actualSenal.getNombre(),ListaEtiquetasBin)
            SenalesBinarios.agregar(SenalBin)
            SenalBin.compararT(ListaEtiquetasBin)
            compar = SenalBin.getListas()
            self.ListasB.agregar(SenalBin.getListas())

            #Apartado para suma de los datos y almacenamiento

            for i in range(compar.getSize()):
                actual = compar.buscarID(i)
                print("-----Str igual: ",actual.getEtiquetaA(),"En tiempo A: ",actual.getTiempoA(),"y B: ",actual.getTiempoB()," en el senal ",actual.getNombreSenal())
            comp = compar.buscarID(i)
            times = actualSenal.getTiempos()  # busco los tiempos que tengo guardados en la lista original
            for j in range(times.getSize()):  # un ciclo por cada uno de los tiempos para compararlos
                tt = tiempos.buscarID(j)  # el dato del tiempo como tal}
                '''print("...",comp.getTiempoA(),comp.getTiempoB(),tt.getNombre())'''
                if tt.getNombre() == comp.getTiempoA():  # si el tiempo de la lista original es igual al primer tiempo donde hay coincidencias
                    print("Se encontro el primer tiempo requerido: ", tt.getNombre())
                    tiempo1 = tt.getNombre()
                    listaA1 = tt.getListaAmplitud()
                    tiempo2 = ""
                    listaA2 = None
                if tt.getNombre() == comp.getTiempoB():
                    print("Se encontro el segundo tiempo requerido: ", tt.getNombre())
                    tiempo2 = tt.getNombre()
                    listaA2 = tt.getListaAmplitud()
                print("Tiempo uno: ", tiempo1, " Tiempo dos: ", tiempo2)
            print("tiempitos: ", tiempo1, tiempo2, listaA1, listaA2)
        suma = Reducida(tiempo1, tiempo2, listaA1, listaA2, listaA2)
        '''if comp.getSiguiente() is not None:
            comp = comp.getSiguiente()
        else:
            print("Finalizamos")'''



    def Grupos(self):


        Senales = self.ListasS
        datosModificados = copy.deepcopy(self.ListasS)
        Binarios = self.ListasB

        tmp = Binarios.getInicio().getDato().getInicio()

        '''if tmp is not None:
            print("tamaño: ", tmp.getDato().getSize())
            print(Binarios.getInicio().getDato().getInicio().getDato().getTiempoA()," ._. ",tmp.getDato().getInicio().getTiempoB())
            tmp = Binarios.getInicio().getSiguiente()'''

        for i in range(Senales.getSize()):
            actualSenal = Senales.buscarID(i)
            print("-------Senal: ",actualSenal.getNombre(),"-------")
            tiempos = actualSenal.getTiempos()
            if tmp is not None:
                for j in range(tiempos.getSize()):
                    tt = tiempos.buscarID(j)
                    print(tmp.getDato().getTiempoA(),"",tmp.getDato().getTiempoB())
                    if tt.getNombre() is not None and tmp.getDato().getTiempoA() is not None:
                        if tt.getNombre() == tmp.getDato().getTiempoA():
                            '''print("Se encontro el primer tiempo requerido: ",tt.getNombre())'''
                            tiempo1 = tt.getNombre()
                            listaA1 = tt.getListaAmplitud()
                            tiempo2 = ""
                            listaA2 = None
                        if tt.getNombre() == tmp.getDato().getTiempoB():
                            '''print("Se encontro el segundo tiempo requerido: ",tt.getNombre())'''
                            tiempo2 = tt.getNombre()
                            listaA2 = tt.getListaAmplitud()
                        '''print("Tiempo uno: ",tiempo1," Tiempo dos: ",tiempo2)'''
                    '''print("tiempitos: ",tiempo1,tiempo2,listaA1,listaA2)'''
                suma = Reducida(tiempo1,tiempo2,listaA1,listaA2,datosModificados)
                tmp = tmp.getSiguiente()



archiv = LecturaXML('c:/Users/Dolyad/Desktop/ArchivosP IPC2/entrada.xml')
archiv.getSenal()
archiv.imprimir()
archiv.list_bin()
SenalBinaria
'''archiv.Grupos()'''


