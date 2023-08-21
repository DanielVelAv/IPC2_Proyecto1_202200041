from Funciones import *

def menu_Principal():
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
        carga_inicial()
    elif(opcion=="2"):
        procesador_archivos()
    elif(opcion=="3"):
        archivo_salida()
    elif(opcion=="4"):
        datos_estudiante()
    elif(opcion=="5"):
        generar_grafica
    elif(opcion=="6"):
        inicializar_sistema()
    elif(opcion=="7"):
        quit()
    else:
        print("porfavor seleccione una opcion valida")
        

    
menu_Principal()