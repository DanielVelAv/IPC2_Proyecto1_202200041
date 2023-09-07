
import xml.etree.ElementTree as ET

import Grafica
from ListaSimple import ListaSimple
from Amplitud import *
from Tiempo import *
from Senal import *
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
        print(">Guardando los datos...")
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
        NuevaL = ListaSimple()
        reducida = Reducida()

        print(">Convirtiendo los datos a binario...")
        print(">Realizando sumas de datos Binarios...")
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
                '''print("La lista convertida a binaria es: ",strEtiqueta)'''
                ListaEtiquetasBin.agregar(SenalStr)
            SenalBin = SenalBinaria(actualSenal.getNombre(),ListaEtiquetasBin)
            SenalesBinarios.agregar(SenalBin)
            SenalBin.compararT(ListaEtiquetasBin)
            compar = SenalBin.getListas()
            self.ListasB.agregar(SenalBin.getListas())


            #Apartado para suma de los datos y almacenamiento

            '''for l in range(compar.getSize()):
                actual = compar.buscarID(l)
                print("-----Str igual: ",actual.getEtiquetaA(),"En tiempo A: ",actual.getTiempoA(),"y B: ",actual.getTiempoB()," en el senal ",actual.getNombreSenal())
            com = compar.buscarID(l)'''
            tiempo1 = ""
            tiempo2 = ""
            primero = False
            segundo = False
            '''print(comp.getTiempoA(),"._.",comp.getTiempoB(),compar.getSize())'''
            times = actualSenal.getTiempos()  # busco los tiempos que tengo guardados en la lista original

            for m in range(compar.getSize()):
                for j in range(times.getSize()):  # un ciclo por cada uno de los tiempos para compararlos
                    comp = compar.buscarID(m)
                    tt = times.buscarID(j)  # el dato del tiempo como tal
                    '''print("lista Amplitud",tt.getListaAmplitud())'''
                    if tt.getNombre() == comp.getTiempoA():  # si el tiempo de la lista original es igual al primer tiempo donde hay coincidencias
                        '''print("Se encontro el primer tiempo requerido: ", tt.getNombre())'''
                        tiempo1 = tt.getNombre()
                        listaA1 = tt.getListaAmplitud()
                        tiempo2 = ""
                        primero = True
                    if tt.getNombre() == comp.getTiempoB():
                        '''print("Se encontro el segundo tiempo requerido: ", tt.getNombre())'''
                        tiempo2 = tt.getNombre()
                        listaA2 = tt.getListaAmplitud()
                        segundo = True
                '''for b in range(times.getSize()):
                    comparar = times.buscarID(b)
                    if tt.getNombre() != comparar.getTiempoA() and tt.getNombre() != comparar.getTiempoB() and primero == False and segundo == False:
                        # aqui se guardara en la misma lista los datos que no coincidan
                        print("sin coincidencia: ", tt.getNombre())'''

                if primero == True and segundo == True:
                    suma = reducida.SumarTiempos(tiempo1, tiempo2, listaA1, listaA2)
                    NuevaL.agregar(reducida.getListasSumas())

                    '''for o in range(reducida.getListasSumas().getSize()):
                        tmp = reducida.getListasSumas().buscarID(o)
                        dat = tmp.getnnNombre()
                        dot = tmp.getLlist()
                        print("nombrecito: ",dat)
                        for d in range(dot.getSize()):
                            var = dot.buscarID(d)
                            amplitudSum = var.getSumados()
                            print(amplitudSum)
                        print('verification',reducida.getLL().getInicio().getDato().getNuevoNombre())
                    listado = Sumados(reducida.getLL().getInicio().getDato().getNuevoNombre())
                    #aqui se guardara a una lista los datos que coincidan
                if primero == False or segundo == False:
                    #aqui se guardara en la misma lista los datos que no coincidan
                    print("sin coincidencia: ",tt.getNombre)'''







    def Grupos(self):
        pass


'''archiv = LecturaXML('c:/Users/Dolyad/Desktop/ArchivosP IPC2/entrada.xml')
archiv.getSenal()
archiv.list_bin()
SenalBinaria'''
'''archiv.Grupos()'''


