from ListaSimple import ListaSimple


class Reducida:
    def __init__(self):
        self.listaSumas = ListaSimple()
        self.ll = ListaSimple()


    def SumarTiempos(self,tiempo1,tiempo2,listaA1,listaA2):
        tiempo1 = tiempo1
        tiempo2 = tiempo2
        listaA1 = listaA1
        listaA2 = listaA2

        nuevoNombre = str(tiempo1)+","+str(tiempo2)

        llist = ListaSimple()

        for i in range(listaA1.getSize()):

            Amplitud = listaA1.buscarID(i)
            AmplitudB = listaA2.buscarID(i)
            Amplitud.getDato()
            suma = int(Amplitud.getDato())+int(AmplitudB.getDato())
            sumatoria = Sumados(suma)
            llist.agregar(sumatoria)
            '''print(Amplitud.getDato(),AmplitudB.getDato())
            print(nuevoNombre," -> ",suma)'''
            '''print("verificacion de guardado: ",llist.getInicio().getDato().getNuevoNombre())'''

        dato = MatR(nuevoNombre, llist)
        self.listaSumas.agregar(dato)

    def getLL(self):
        return self.ll

    def getListasSumas(self):
        return self.listaSumas

class CoincidenciasBin:
    def __init__(self,etiquetaA,etiquetaB,nombreSenal,TiempoA,TiempoB,size):
        self.etiquetaA = etiquetaA
        self.etiquetaB = etiquetaB
        self.nombreSenal = nombreSenal
        self.tiempoA = TiempoA
        self.tiempoB = TiempoB
        self.size = size

    def getSize(self):
        return self.size

    def getEtiquetaA(self):
        return self.etiquetaA

    def getEtiquetaB(self):
        return self.etiquetaB

    def getNombreSenal(self):
        return self.nombreSenal

    def getTiempoA(self):
        return self.tiempoA

    def getTiempoB(self):
        return self.tiempoB



class Sumados:
    def __init__(self,suma):
        self.suma = suma

    def getSumados(self):
        return self.suma


class MatR:

    def __init__(self, nuevoNombre, llist):
        self.nuevoNombre = nuevoNombre
        self.llist = llist

    def getnnNombre(self):
        return self.nuevoNombre

    def getLlist(self):
        return self.llist

