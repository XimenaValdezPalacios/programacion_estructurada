import os

'''pelicula={
    "nombre":"",
    "categoria":"",
    "clasificacion":"",
    "genero":"",
    "ideoma":""
}
'''
peliculas = []
pelicula={}

def esperatecla():
    input("\n\t...Oprime cualquier tecla para continuar...")

def borrarpantalla():
    os.system("cls")

def crearpelicula():
    borrarpantalla()
    print("\t\t..::Crear Película::.. \n")
    pelicula["nombre"]=input("Ingresa el nombre: ").lower().strip()
    #pelicula.update({"nombre": input("Ingresa el nombre: ").lower().strip()})
    pelicula.update({"categoria": input("Ingresa la categoría: ").lower().strip()})
    pelicula.update({"clasificacion": input("Ingresa la clasificación: ").lower().strip()})
    pelicula.update({"genero": input("Ingresa el género: ").lower().strip()})
    pelicula.update({"ideoma": input("Ingresa el idioma: ").lower().strip()})
    print("\t\t..::La operacion se realizo con exito::..")
    peliculas.append(pelicula)

def borarpelicula():
    borrarpantalla()
    print("\t\t..::Borrar todas las películas del sistema::.. \n")
    resp = input("Deseas quitar TODAS las películas del sistema? (si/no): ").lower().strip()
    if resp == "si":
        pelicula.clear()
        print("\n\t\t..::Operación realizada con éxito::..")

def mostrarpelicula(): 
    borrarpantalla()
    print("\t..::Películas::.. ")
    if len(pelicula)>0:
        for i in pelicula :
            print(f"\t{i} : {pelicula[i]}")
    else:
        print("\n\t\tEl catálogo de películas se encuentra vacío")

    #print(f"{peliculas}")

def agregarcaracteristicapelicula():
    borrarpantalla()
    print("\n\t:::Agregar Característica a Película:::\n")
    atributo=input("Ingresa la nueva caracteristica de la pelicula: ").lower().strip()
    valor=input("Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
    pelicula[atributo] = valor
    print("\n\t\t:::·LA OPERACIÓN SE REALIZÓ CON ÉXITO!:::\n")

def modificarcaracteristicapelicula():
    borrarpantalla()
    print("\n\t:::Modificar Característica de Película:::\n")
    atributo = input("Ingresa la característica que deseas modificar: ").lower().strip()
    if atributo in pelicula:
        valor = input("Ingresa el nuevo valor de la característica: ").upper().strip()
        pelicula[atributo] = valor
        print("\n\t\t:::·LA OPERACIÓN SE REALIZÓ CON ÉXITO!:::\n")

def borrarcaracteristicapeliculas():
    borrarpantalla()
    print("\n\t:::Borrar Caracteristicas a Películas:::\n")
    if len(pelicula) == 0:
        print("\tNo hay características para mostrar.")
        esperatecla()
    else:
        for i in pelicula:
            print(f"\t{i} : {pelicula[i]}")
        resp = input("\n¿Deseas borrar alguna característica? (si/no): ").lower().strip()
        if resp == "si":
            atributo = input("\nLa característica que deseas borrar o quitar: ").lower().strip()
            if atributo in pelicula:
                del pelicula[atributo]
                print("\n\t\t:::·LA OPERACIÓN SE REALIZÓ CON ÉXITO!:::\n")
            else:
                print("\n\t\t:::·La característica no existe en la película!:::\n")
            esperatecla()
        else:
            print("\n\tNo se realizó ninguna operación.")


        
#valor enseñar. que se repita en modificar