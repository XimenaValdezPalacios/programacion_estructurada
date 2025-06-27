#PROYECTO 1
#Crear un proyecto que permita gestionar (administrar) peliculas; colocar un menu 
#de opciones para agregar, borrar, modidifcar, consultar, buscar y vaciar peliculas
#NOTAS: 
#1.-Utilizar funciones y mnadar llamar desde otro archivo
#2.- Utilizar una lista para almacenar los nombres de las peliculas
import os
from peliculas import agregar_pelicula, borrar_pelicula, modificar_pelicula, consultar_peliculas, buscar_pelicula, vaciar_peliculas, peliculas
os.system('cls')

def menu():
    salir = False

    while not salir:
        print("\n--- MENÚ DE PELÍCULAS ---\n1. Agregar película" \
        "\n2. Borrar película\n3. Modificar película\n4. Consultar películas" \
        "\n5. Buscar película\n6. Vaciar lista de películas\n7. Salir")
        opcion = input("Elige una opción: ")
        os.system('cls')
        if opcion == "1":
            nombre = input("Nombre de la película a agregar: ")
            agregar_pelicula(nombre)
            input("Presiona cualquier tecla para continuar...")
        elif opcion == "2":
            nombre = input("Nombre de la película a borrar: ")
            borrar_pelicula(nombre)
            input("Presiona cualquier tecla para continuar...")
        elif opcion == "3":
            nombre = input("Nombre de la película a modificar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            modificar_pelicula(nombre, nuevo_nombre)
            input("Presiona cualquier tecla para continuar...")
        elif opcion == "4":
            consultar_peliculas()
            input("Presiona cualquier tecla para continuar...")
        elif opcion == "5":
            nombre = input("Nombre de la película a buscar: ")
            buscar_pelicula(nombre)
            input("Presiona cualquier tecla para continuar...")
        elif opcion == "6":
            vaciar_peliculas()
            input("Presiona cualquier tecla para continuar...")
        elif opcion == "7":
            print("¡Hasta luego!")
            salir = True
        else:
            print("Opción no válida. Intenta de nuevo.")
            input("Presiona cualquier tecla para continuar...")
    os.system('cls')
menu()


