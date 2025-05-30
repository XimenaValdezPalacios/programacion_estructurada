#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

import os
os.system("cls")

numeros = [7, 14, 10, 90, 78]

#1er forma
print(numeros)

#2da forma valor
for i in numeros:
    print(i)

#3ra forma indices
for i in range(0,len(numeros)):
    print(numeros[i])




#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
 
os.system("cls")
palabras = ["hola", "adios", "que", "tal"]
palabra_buscar=input("Dame la palabra buscar: ")

#1er forma
if palabra_buscar in palabras:
    print("Se encontro la palabra")
else:
    print("No encontro la palabra")


#2da forma
encontro=False

for i in palabras:
    if i==palabra_buscar:
        encontro=True

if encontro:
    print("Se encontro la palabra")
else:
    print("No se encontro la palabra")

#3ra forma
encontro=False

for i in range(0,len(palabras)):
    if palabras[i]==palabra_buscar:
        encontro=True

if encontro:
    print("Se encontro la palabra")
else:
    print("No se encontro la palabra")


os.system("cls")
#Ejemplo 3 Añadir elementos a la lista
os.system("cls")

numeross = []
opc="si"

while opc=="si":
    numeross.append(float(input("Dame un numero entero o decimal: ")))
    opc=input("Deseas solicitar otro numero? (Si/No): ").lower()

print(numeross)

#Ejemplo 4 Crear una lista multidimencional (matriz) que almacene el nombre y telefono de 4 personas
os.system ("cls")
matriz = [["Juan", "1234567890"], 
          ["Maria", "0987654321"], 
          ["Pedro", "1122334455"], 
          ["Ana", "5566778899"]]
# Imprimir la matriz
for i in range(len(matriz)):
    print(f"Nombre: {matriz[i][0]}, Telefono: {matriz[i][1]}")
