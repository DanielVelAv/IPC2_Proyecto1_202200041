from Funciones import *
from LecturaXML import *
from Grap import *

ubicacion = ""

def menu_Principal():
    global ubicacion
    print("\nMenú Principal")
    print("     1.Cargar archivo")
    print("     2.Procesador archivo")
    print("     3.Escribir archivo de salida")
    print("     4.Mostrar datos del estudiante")
    print("     5.generar gráfica")
    print("     6.Inicializar sistema")
    print("     7.salida\n")

    opcion = input("Seleccione una opción: ")

    if(opcion=="1"):
        print("\nOpcion Cargar archivo: ")
        ubicacion = input("Ingrese la ruta del archivo:")
        input("pulse cualquier tecla para volver al menu principal")
        menu_Principal()
    elif(opcion=="2"):
        archiv = LecturaXML(ubicacion)
        archiv.getSenal()
        archiv.list_bin()
        SenalBinaria
        input("pulse cualquier tecla para volver al menu principal")
        menu_Principal()
    elif(opcion=="3"):
        archivo_salida()
    elif(opcion=="4"):
        print("Opcion Datos del estudiante\n")
        print("> Daniel Eduardo Velásquez Avila\n> 202200041 \n> Introducción a la Programación y computación 2 sección: N\n> Ingenieria en Ciencias y Sistemas\n> 4to Semestre\n")
        input("Pulse cualquier tecla para volver al menu principal")
        menu_Principal()
    elif(opcion=="5"):
        grafo = Graf()
        grafo.ejecutar_GrafSenal(ubicacion)
        input(">hecho :)")
        menu_Principal()
    elif(opcion=="6"):
        inicializar_sistema()
    elif(opcion=="7"):
        quit()
    else:
        print("porfavor seleccione una opcion valida")
        menu_Principal()
        

    
menu_Principal()