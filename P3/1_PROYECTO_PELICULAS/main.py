'''Proyecto 1 .
 crear un proyecto que permita gestionar(administrar) peliculas;colocar un menu de opciones para agregar, borrar, 
 modificar, consultar, buscara y vaciar peliculas
 Notas : 1.- utilizar funciones y mandara allamar deesde otro archivo 
         2.- Utilizar una diccionarios para almacenar los atributos o caracteristicas de un apelicula
'''
import peliculas

opciones = [
    "Crear",
    "Borrar",
    "Mostrar",
    "Buscar",
    "Modificar",
    "SALIR"
]

while True:
        
    peliculas.borrarpantalla()
    print("\t\t..::Bienvenido a pelimundo::..")
    print("\t..::Un sistema para gestionar peliculas::..\n")
    
    for i in range(len(opciones)):
            print(f"\t\t{i+1}) {opciones[i]}")
        
    opc = input("\n\tQue opcion deseas elegir? ").strip()
    if opc == "1":
            peliculas.crearpelicula()
            peliculas.esperatecla()
    elif opc == "2":
            peliculas.mostrarpelicula()
            peliculas.esperatecla()
    elif opc == "3":
            peliculas.buscarpeliculas()
            peliculas.esperatecla()
    elif opc == "4":
            peliculas.modificarPeliculas()
            peliculas.esperatecla()
    elif opc == "5":
            peliculas.borrarPeliculas()
            peliculas.esperatecla()
    elif opc == "6":
            print("\n\tSaliendo del programa...")
            break
    else:
            print("\n\tOpción no válida.")
            peliculas.esperatecla()

print("El programa ha finalizado")