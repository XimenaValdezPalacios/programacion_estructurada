import os
import mysql.connector
from mysql.connector import Error

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

def conectar():
    try:
        conexion= mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"El error se presento en {e}")
        return None

def crearpelicula():
    borrarpantalla()
    conectar()
    conexionBD=conectar()
    if conexionBD !=None:
        print("\t\t..::Crear Película::.. \n")
        pelicula["nombre"]=input("Ingresa el nombre: ").lower().strip()
        #pelicula.update({"nombre": input("Ingresa el nombre: ").lower().strip()})
        pelicula.update({"categoria": input("Ingresa la categoría: ").lower().strip()})
        pelicula.update({"clasificacion": input("Ingresa la clasificación: ").lower().strip()})
        pelicula.update({"genero": input("Ingresa el género: ").lower().strip()})
        pelicula.update({"idioma": input("Ingresa el idioma: ").lower().strip()})
        
        ###BD
        cursor=conexionBD.cursor()
        sql = "INSERT INTO peliculas (nombre, categoria, clasificacion, genero, idioma) VALUES (%s, %s, %s, %s, %s)"
        val = (pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"])
        cursor.execute(sql, val)
        conexionBD.commit()
        print("\t\t..::La operacion se realizo con exito::..")
    

def borrarPeliculas():
  borrarpantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Borrar Películas ::. \n")
    nombre=input("Ingresa el nombre de la pelicula a borrar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelis in registros:
        print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
      print(f"-"*80) 
      resp=input(f"¿Deseas borrar la pelicula {nombre}? (Si/No): ").lower().strip()
      if resp=="si":
        sql="delete from peliculas where nombre = %s"
        val=(nombre,)
        cursor.execute(sql,val)
        conexionBD.commit()
        print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")
    else:
      print("\t .:: peliculas no encontradas en el sistema ::..")

def mostrarpelicula(): 
    borrarpantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\t\t..::Mostrar Películas::.. \n")
        cursor = conexionBD.cursor()
        sql = "select * from peliculas"
        cursor.execute(sql)
        registros = cursor.fetchall()
        if registros:
            print("Mosrara las Peliculas")
            print (f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(F"-"*80)
            for pelis in registros:
                print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
                print(F"-"*80)
        else:
            print("\t\t..::No hay películas para mostrar::..")


        #if len(pelicula)>0:
         #   for i in pelicula:
          #      print(f"\t{i} : {pelicula[i]}")
        #else:
         #   print("\t\t..::No hay películas para mostrar::..")

def buscarpeliculas():
    borrarpantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\t\t..::Buscar Películas::.. \n")
        nombre = input("Ingresa el nombre de la película que deseas buscar: ").lower().strip()

        cursor = conexionBD.cursor()
        sql = "select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros = cursor.fetchall()
        if registros:
            print("Mosrara las Peliculas")
            print (f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(F"-"*80)
            for pelis in registros:
                print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
                print(F"-"*80)
        else:
            print("\t\t..::No hay películas para mostrar::..")
        
def modificarPeliculas():
    borrarpantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\t\t..::Modificar Películas::.. \n")
        nombre = input("Ingresa el nombre de la película que deseas modificar: ").lower().strip()

        cursor = conexionBD.cursor()
        sql = "select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros = cursor.fetchall()
        if registros:
            print("Mosrara las Peliculas")
            print (f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(F"-"*80)
            for pelis in registros:
                print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
                print(F"-"*80)
        else:
            print("\t\t..::No hay películas para mostrar::..")


        #if len(pelicula)>0:
         #   for i in pelicula:
          #      print(f"\t{i} : {pelicula[i]}")
        #else:
         #   print("\t\t..::No hay películas para mostrar::..")
        
#valor enseñar. que se repita en modificar