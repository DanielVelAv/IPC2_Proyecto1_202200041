


class Reducida:
    def __init__(self,tiempo1,tiempo2,listaA1,listaA2,datosModificados):
        self.tiempo1 = tiempo1
        self.tiempo2 = tiempo2
        self.listaA1 = listaA1
        self.listaA2 = listaA2
        self.datosModificados = datosModificados
        self.SumarTiempos()


    def SumarTiempos(self):

        nuevoNombre = str(self.tiempo1)+","+str(self.tiempo2)

        print(self.listaA1)
        for i in range(self.listaA1.getSize()):
            Amplitud = self.listaA1.buscarID(i)
            AmplitudB = self.listaA2.buscarID(i)
            Amplitud.getDato()
            suma = int(Amplitud.getDato())+int(AmplitudB.getDato())
            print(Amplitud.getDato(),AmplitudB.getDato())
            print(nuevoNombre," -> ",suma)



    def getMatReducida(self):
        pass

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
