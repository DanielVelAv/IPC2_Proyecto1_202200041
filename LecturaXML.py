import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple
from Senal import Senal


class LecturaXML():

    def __init__(self, path):
        self.raiz = ET.parse(path).getroot()

    def getSenal(self):
        #se crea una lista simple para guardar los archivos
        listSenales = ListaSimple()
        #se buscam los elemento que estan en la etiqueta senal
        for elementos in self.raiz.findall('senal'):
            nombreSenal = elementos.get('nombre')
            tiempoMax = elementos.get('t')
            amplitudMax = elementos.get('A')
            #se guardara en una lista
            
            #se envian los datos
            tmpSenal = Senal(nombreSenal, tiempoMax, amplitudMax)
            '''listSenales.agregarFinal(tmpSenal)'''

            #print(nombreSenal,tiempoMax,amplitudMax)

            
            print("----Lista de Senales----")
            senalGuardada = listSenales.getInicio()
            while senalGuardada != None:
                print(senalGuardada.getDato().getNombre())
                senalGuardada = senalGuardada.getSiguiente()

    #se busca que lea cada uno de los datos y actualizar el nodo
    def getDatos():
        pass