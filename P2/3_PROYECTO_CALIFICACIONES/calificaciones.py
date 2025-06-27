def borrarPantalla():
   import os  
   os.system("cls")

def esperarTecla():
      input("Oprima cualquier tecla para continuar")  

def menu_principal():
    print("🎓 .:: Sistema de Gestión de Calificaciones ::. 🎓\n"
             "1️⃣  Agregar  \n"
             "2️⃣  Mostrar \n"
             "3️⃣  Cálcular Promedios \n"
             "4️⃣  Buscar\n"
             "5️⃣  SALIR 🚪")
    opcion = input("Elige una opción (1-5): ") 
    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    print("➕ Agregar Calificaciones")
    nombre = input("👤 Nombre del Alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
         continua = True
         while continua:
             try:
                  cal = float(input(f"✏️ Calificación {i}: "))
                  if cal >= 0 and cal < 11:
                      calificaciones.append(cal)
                      continua = False
                  else:
                      print("⚠️ Ingresa un número valido") 
             except ValueError:
                  print("⚠️ Ingresa un valor númerico")
    lista.append([nombre] + calificaciones)
    print("✅ Acción realizada con éxito")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("📋 Mostrar Calificaciones") 
    if len(lista) > 0:
         print(f"{'👤 Nombre':<15}{'📝 Calf. 1':<10}{'📝 Calf. 2':<10}{'📝 Calf. 3':<10}")
         print(f"{'-'*40}")
         for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
         print(f"{'-'*40}")  
         cuantos = len(lista)
         print(f"👥 Son {cuantos} alumnos")
    else:
         print("❌ No hay calificaciones registradas en el sistema")    

def calcular_promedios(lista):
      borrarPantalla()
      print("📊 .:: PROMEDIOS ::. ")
      if len(lista) > 0:
         print(f"{'👤 Alumno':<15}{'📈 Promedio':<10}")
         print(f"{'-'*30}")
         promedio_grupal = 0
         for fila in lista:
             nombre = fila[0]
             promedio = sum(fila[1:]) / 3
             print(f"{nombre:<15}{promedio:.2f}")  
             promedio_grupal += promedio 
         print(f"{'-'*30}")
         promedio_grupal = promedio_grupal / len(lista)
         print(f"🏅 El promedio grupal es: {promedio_grupal:.2f} ")
      else:
         print("❌ No hay calificaciones registradas en el sistema")  

def buscar_calificacion(lista):
    borrarPantalla()
    print("🔍 Buscar Calificación")
    if len(lista) > 0:
        nombre = input("👤 Nombre del Alumno a buscar: ").upper().strip()
        encontrado = False
        for fila in lista:
            if fila[0] == nombre:
                print(f"{'👤 Nombre':<15}{'📝 Calf. 1':<10}{'📝 Calf. 2':<10}{'📝 Calf. 3':<10}")
                print(f"{'-'*40}")
                print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
                encontrado = True
        if not encontrado:
            print("❌ Alumno no encontrado")
    else:
        print("❌ No hay calificaciones registradas en el sistema")
