from ListaSimple import ListaSimple
from Tiempo import Tiempo

class Senal:

    def __init__(self,nombre, tiempoMax, amplitudMax):
       self.nombre = nombre
       self.tiempoMax = tiempoMax
       self.amplitudMax = amplitudMax
       #en senal se tiene una lista de tiempos
       self.tiempos = ListaSimple()
       self.crearListaTiempos()
       self.imprimir()

    def getNombre(self):
        return self.nombre
    
    def getTiempoMax(self):
        return self.tiempoMax
    
    def getAmplitudMax(self):
        return self.amplitudMax
    
    #
    def crearListaTiempos(self):
        for i in range(0,int(self.tiempoMax)+1):
            objeto = Tiempo(i,self.amplitudMax)
            self.tiempos.agregarFinal(objeto)

    def imprimir(self):
        print("--------Tiempos para senal----------",self.getNombre())
        tmpTiempo = self.tiempos.getInicio()
        while tmpTiempo != None:
            print(tmpTiempo.getDato().getTiempo())
            #se avanza hacia el siguiente dato
            tmpTiempo = tmpTiempo.getSiguiente()