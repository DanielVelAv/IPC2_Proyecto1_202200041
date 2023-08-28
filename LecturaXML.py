import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple
from Amplitud import *
from Tiempo import *
from Senal import *

class LecturaXML():
    def __init__(self, path):
        self.raiz = ET.parse(path).getroot()

    def getSenal(self):

        Senales = ListaSimple()

        for i in self.raiz.findall('senal'):
            nombreS = i.get('nombre')
            tiempoMax = int(i.get('t'))
            amplitudMax = i.get('a')
            tiempos = ListaSimple()

            for j in range(1,tiempoMax):
                amplitudes = ListaSimple()
                for k in i.findall('dato'):
                    #k.text hace referencia a el valor de dato
                    nuevaA = Amplitud(k,k.text)
                    amplitudes.agregar(nuevaA)
                nuevo_t = Tiempo(j,amplitudes)
                tiempos.agregar(nuevo_t)
            nueva_S = Senal(nombreS,tiempoMax,amplitudMax,tiempos)
            Senales.agregar(nueva_S)
        return Senales


archiv = LecturaXML('c:/Users/Dolyad/Desktop/ArchivosP IPC2/entrada.xml')
archiv.getSenal()

