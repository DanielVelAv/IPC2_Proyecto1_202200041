import graphviz

def grafica(listaSenales):

    listaSenales = listaSenales

    dot = graphviz.Digraph(listaSenales.getNombreSenal())

    dot.render(outfile='img/{}.svg'.format(tmp_senal.get_name())).replace('\\', '/')
    'img/{}.svg'.format(tmp.get_name())