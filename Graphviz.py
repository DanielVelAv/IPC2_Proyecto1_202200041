import graphviz

class Graph():
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        self.dot = graphviz.Digraph('structs', filename=f'{self.nombreArchivo}.gv',
                                    node_attr={'shape': 'record', 'fontname': 'Helvetica'})

    def add(self, nodoInicio,nodoSiguiente):
            self.dot.node(str(nodoInicio),str(nodoSiguiente))
            self.dot.node(str(nodoSiguiente),str(nodoSiguiente))
            self.dot.edge(str(nodoInicio),str(nodoSiguiente))

    def generar(self):
        self.dot.render(outfile=f'img/{self.nombreArchivo}.png').replace('\\', '/')
        f'img/{self.nombreArchivo}.png'
