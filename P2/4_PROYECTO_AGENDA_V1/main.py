import os
os.system("cls")

import agenda

def main():
    datos = {} 

    opcion=True
    while opcion:
     agenda.borrar_pantalla()
     opcion=agenda.menu_principal()

     match opcion:
        case "1":  
            agenda.agregar_contacto(datos)
            agenda.esperar_tecla()
        case "2":
            agenda.mostrar_contactos(datos)
            agenda.esperar_tecla()   
        case "3":
            agenda.buscar_contacto(datos)
            agenda.esperar_tecla()
        case "4":
            agenda.modificar_contacto(datos)
            agenda.esperar_tecla()
        case "5":
            agenda.eliminar_contacto(datos)
            agenda.esperar_tecla()
        case "6":
            opcion=False    
            agenda.borrar_pantalla()
            print(" Terminaste la ejecucion del SW")
        case _:
            opcion=True 
            print("Opción invalida vuelva a intentarlo") 
            agenda.esperar_tecla()

if __name__ == "__main__":
    main()
    