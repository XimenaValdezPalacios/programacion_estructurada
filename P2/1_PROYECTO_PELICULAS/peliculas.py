peliculas = []

def agregar_pelicula(nombre):
    if nombre:
        peliculas.append(nombre)
        print(f"Película '{nombre}' agregada.")
    else:
        print("No se pudo agregar la película (el nombre está vacío).")

def borrar_pelicula(nombre):
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f"Película '{nombre}' borrada.")
    else:
        print("La película no existe en la lista.")

def modificar_pelicula(nombre, nuevo_nombre):
    if nombre in peliculas:
        idx = peliculas.index(nombre)
        idx = peliculas.index(nombre)
        if nuevo_nombre:
            peliculas[idx] = nuevo_nombre
            print(f"Película '{nombre}' modificada a '{nuevo_nombre}'.")
        else:
            print("El nuevo nombre es inválido.")
    else:
        print("La película no existe en la lista.")

def consultar_peliculas():
    if peliculas:
        print("\nLista de películas:")
        conteo = {}
        for peli in peliculas:
            conteo[peli] = conteo.get(peli, 0) + 1
        mostradas = set()
        idx = 1
        for peli in peliculas:
            if peli not in mostradas:
                cantidad = conteo[peli]
                print(f"{idx}. {peli} (x{cantidad})" if cantidad > 1 else f"{idx}. {peli}")
                mostradas.add(peli)
                idx += 1
    else:
        print("No hay películas en la lista.")

def buscar_pelicula(nombre):
    cantidad = peliculas.count(nombre)
    if cantidad > 0:
        print(f"La película '{nombre}' está en la lista ({cantidad} vez/veces).")
    else:
        print(f"La película '{nombre}' no se encontró.")

def vaciar_peliculas():
    peliculas.clear()
    print("Lista de películas vaciada.")