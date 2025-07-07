agenda = {}

def menu_principal():
    print("\t📅 .:: Sistema de Gestión de Agenda de Contactos ::. 📅\n"
          "\t\t1️⃣ Agregar Contacto\n"
          "\t\t2️⃣ Mostrar todos los contactos\n"
          "\t\t3️⃣ Buscar contacto por nombre\n"
          "\t\t4️⃣ Modificar contacto\n"
          "\t\t5️⃣ Eliminar contacto\n"
          "\t\t6️⃣ SALIR")
    opcion = input("Elige una opción (1-6): ")
    return opcion

def borrar_pantalla():
    import os
    os.system("cls")

def esperar_tecla():
    input(".:: Oprima cualquier tecla para continuar ::.")

def agregar_contacto(agenda):
    borrar_pantalla()
    print("\t\t📇 .:: Agregar Contacto ::. 📇")
    nombre = input("Nombre: ").upper().strip()
    if nombre in agenda:
        print("Contacto existente.")
    else:
        tel = input("Teléfono: ").strip()
        email = input("Email: ").strip().upper()
        agenda[nombre] = (tel, email)
        print(f"Contacto {nombre} agregado exitosamente.")

def mostrar_contactos(agenda):
    borrar_pantalla()
    print("\t\t📋 .:: Mostrar Contactos ::. 📋")
    if not agenda:
        print("No hay contactos en la agenda.")
    else:
        print(f"{'Nombre':<15} {'Teléfono':<15} {'Email':<15}")
        print("_" * 60)
        for nombre, datos in agenda.items():
            print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<15}")
        print("_" * 60)

def buscar_contacto(agenda):
    borrar_pantalla()
    print("\t\t🔍 .:: Buscar Contacto ::. 🔍")
    if not agenda:
        print("No hay contactos en la agenda.")
    else:
        nombre = input("Nombre: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15} {'Teléfono':<15} {'Email':<15}")
            print("_" * 60)
            print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<15}")
            print("_" * 60)
        else:
            print("No existe el contacto")

def modificar_contacto(agenda):
    borrar_pantalla()
    print("\t\t✏️ .:: Modificar Contacto ::. ✏️")
    if not agenda:
        print("No hay contactos en la agenda.")
    else:
        nombre = input("Nombre: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15} {'Teléfono':<15} {'Email':<15}")
            print("_" * 60)
            print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<15}")
            print("_" * 60)
            resp = input("¿Desea modificar el contacto? (Si/No): ").upper().strip()
            if resp == "SI":
                tel = input("Teléfono: ").strip()
                email = input("Email: ").strip().upper()
                agenda[nombre] = {tel, email}
                print("Acción realizada con éxito.")
        else:
            print("No existe el contacto")

def eliminar_contacto(agenda):
    borrar_pantalla()
    print("\t\t🗑️ .:: Eliminar Contacto ::. 🗑️")
    if not agenda:
        print("No hay contactos en la agenda.")
    else:
        nombre = input("Nombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15} {'Teléfono':<15} {'Email':<15}")
            print("_" * 60)
            print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<15}")
            print("_" * 60)
            resp = input("¿Desea eliminar el contacto? (Si/No): ").upper().strip()
            if resp == "SI":
                agenda.pop(nombre)
                print("Acción realizada con éxito.")
        else:
            print("No existe el contacto")