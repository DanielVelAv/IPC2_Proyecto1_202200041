import graphviz
from LecturaXML import LecturaXML
from ListaSimple import ListaSimple


class Graf:
    def ejecutar_GrafSenal(self,ubicacion):
        archiv = LecturaXML(ubicacion)
        archiv.getSenal().getInicio().getDato().getNombre()
        archiv.ListasS

        print(">Realizando la Graficas...")
        for i in range(archiv.ListasS.getSize()):

            archiv.ListasS.getInicio().getDato().getAmplitudMax()

            senales = archiv.ListasS

            for k in range(senales.getSize()):
                actualSenal = senales.buscarID(k)

                dot = graphviz.Digraph(actualSenal.getNombre(), format='png')

                dot.node('Title',actualSenal.getNombre())
                dot.node('Time',"Tiempo Max: "+str(actualSenal.getTiempoMax()))
                dot.node('Amplitud', actualSenal.getAmplitudMax())
                dot.edge('Title','Time')
                dot.edge('Title', 'Amplitud')

                tiempos = actualSenal.getTiempos()

                for l in range(tiempos.getSize()):
                    actualTiempo = tiempos.buscarID(l)
                    '''print("Tiempos: ",actualTiempo.getNombre())'''
                    amplitudes = actualTiempo.getListaAmplitud()
                    for m in range(amplitudes.getSize()):
                        actualAmplitu = amplitudes.buscarID(m)
                        if l == 0:
                            dot.node('Amplitud_' + str(i) + str(l) + str(m), actualAmplitu.getDato())
                            dot.edge('Title', 'Amplitud_' + str(i) + str(l) + str(m))
                        else:
                            dot.node('Amplitud_' + str(i) + str(l) + str(m), actualAmplitu.getDato())
                            dot.edge('Amplitud_' + str(i) + str(l-1) + str(m),'Amplitud_' + str(i) + str(l) + str(m))

                dot.render('grafica' + actualSenal.getNombre())

    def ejecutar_grafReducido(self, listaNL):
        pass
        '''dot = graphviz.Digraph('matriz reducida', format='png')

        dot.node('Title', )
        dot.node('Amplitud', actualSenal.getAmplitudMax())'''








