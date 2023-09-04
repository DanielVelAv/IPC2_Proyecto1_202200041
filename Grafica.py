import graphviz

class Graphics():
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        self.d = graphviz.Digraph(filename=f'{self.nombreArchivo}.gv')

    def add(self):
        with self.d.subgraph() as s:
            s.attr(rank='same')
            s.node('Prueba1')

        self.d.node('C')

        with self.d.subgraph() as s:
            s.attr(rank='same')
            s.node('B')
            s.node('D')
            s.node('Y')

        self.d.edges(['CB'])


    def generar(self):
        self.d.render(outfile=f'img/{self.nombreArchivo}.png').replace('\\', '/')
        f'img/{self.nombreArchivo}.png'