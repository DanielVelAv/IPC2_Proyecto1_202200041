import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple
from Senal import Senal
import copy



archivo = ET.parse("c:/Users/Dolyad/Desktop/ArchivosP IPC2/entrada.xml").getroot()

class Lectura():
    def __init__(self,ubicacion):
        self.ubicacion = ubicacion
        self.listaSenales = ListaSimple()
        self.listaDato = ListaSimple()
    def getSenal(self):
        for elementos in archivo:
            NombreSenal = elementos.get('nombre')
            tiempoMax = int(elementos.get('t'))
            amplitudMax = int(elementos.get('A'))
            if tiempoMax>0 and tiempoMax <= 3600:
                if amplitudMax >0 and amplitudMax<=130:
                    for senal in elementos.findall('dato'):
                        dato = int(senal.text)
                        self.listaDato.agregar(dato)
                else:
                    print("El Senal "+NombreSenal+" Fue rechazado por la amplitud: "+amplitudMax+"")
            else:
                print("El Senal "+NombreSenal+" Fue rechazada por el tiempo: "+tiempoMax+"")
            senalActual = Senal(NombreSenal, tiempoMax, amplitudMax)
            self.listaSenales.agregar(senalActual)
        return self.listaSenales




archiv = Lectura(archivo)
archiv.getSenal()