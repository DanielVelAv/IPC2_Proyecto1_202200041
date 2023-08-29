import xml.etree.ElementTree as ET

import Grafica
from ListaSimple import ListaSimple
from Amplitud import *
from Tiempo import *
from Senal import *
from Grafica import *

class LecturaXML():
    def __init__(self, path):
        self.raiz = ET.parse(path).getroot()
        self.ListasS = ListaSimple()

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
                # aqui se podria crear una clase donde los parametros sean tiempo y strEtiqueta, se instancia y esa se agregaria a la lista etiquetas
                SenalStr = Etiqueta(actualTiempo.getNombre(), strEtiqueta)
                #print(actualTiempo.getNombre(),strEtiqueta) #funciona correctamente !no tocar
                ListaEtiquetasBin.agregar(SenalStr)
            #aqui se crea una clase senal binaria que guarde el nombre de la senal actual y setee la lista etiquetas
            SenalBin = SenalBinaria(actualSenal.getNombre(),ListaEtiquetasBin)
            #print(actualSenal.getNombre(),ListaEtiquetasBin)
            SenalesBinarios.agregar(SenalBin)
            # luego se agrega esa senal binaria a la lista creada al principio (SenalesBinarios)
        return SenalesBinarios





archiv = LecturaXML('c:/Users/Dolyad/Desktop/ArchivosP IPC2/entrada.xml')
archiv.getSenal()
archiv.imprimir()
archiv.list_bin()
SenalBinaria

