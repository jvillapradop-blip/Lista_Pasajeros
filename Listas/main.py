from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un numero entero.")


def leer_pasajero():
    numero = leer_entero("  No. de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cedula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def cargar_datos_prueba(lista):
    lista.añadir(Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"))
    lista.añadir(Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"))
    lista.añadir(Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"))
    lista.añadir(Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"))
    lista.añadir(Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"))
    print("  Datos de prueba cargados")


def mostrar_opciones(titulo, extras=False):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir           2. Listar            3. Insertar en posicion")
    print(" 4. Buscar (lineal)  5. Buscar (binaria)  6. Modificar")
    print(" 7. Eliminar por posicion                 8. Eliminar por numero")
    print(" 9. Ordenar asc     10. Ordenar desc     11. Reversar")
    print("12. Copiar          13. Longitud")
    if extras:
        print("14. Filtrar por destino                  15. Mayores de edad")
    print(" C. Cargar datos de prueba                0. Volver")


def menu_lista1():
    while True:
        mostrar_opciones("MENU 1 - MiLista")
        op = input("Opcion: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista1.añadir(pasajero):
                print("  Pasajero añadido")
        elif op == "2":
            lista1.listar()
        elif op == "3":
            pos = leer_entero("  Posicion a insertar: ")
            pasajero = leer_pasajero()
            if lista1.insertar(pos, pasajero):
                print(f"  Pasajero insertado en la posicion [{pos}]")
        elif op == "4":
            num = leer_entero("  No. de pasajero a buscar: ")
            pos = lista1.buscar(num)
            if pos != -1:
                print(f"  Encontrado en [{pos}]: {lista1.datos[pos]}")
            else:
                print("  No existe un pasajero con ese numero")
        elif op == "5":
            num = leer_entero("  No. de pasajero a buscar (binaria): ")
            pos = lista1.buscar_binaria(num)
            if pos != -1:
                print(f"  Encontrado en [{pos}]: {lista1.datos[pos]}")
            else:
                print("  No encontrado (recuerda ordenar ascendentemente primero)")
        elif op == "6":
            num = leer_entero("  No. de pasajero a modificar: ")
            nuevo_destino = input("  Nuevo destino: ").strip()
            nuevo_asiento = input("  Nuevo asiento: ").strip().upper()
            if lista1.modificar(num, nuevo_destino, nuevo_asiento):
                print("  Datos del pasajero actualizados")
            else:
                print("  No existe un pasajero con ese numero")
        elif op == "7":
            pos = leer_entero("  Posicion a eliminar: ")
            eliminado = lista1.eliminar_por_posicion(pos)
            if eliminado is not None:
                print(f"  Eliminado: {eliminado}")
            else:
                print("  Posicion fuera de rango")
        elif op == "8":
            num = leer_entero("  No. de pasajero a eliminar: ")
            if lista1.eliminar_por_valor(num):
                print(f"  Pasajero #{num} eliminado")
            else:
                print("  No existe un pasajero con ese numero")
        elif op == "9":
            lista1.ordenar_asc()
            print("  Lista ordenada de menor a mayor:")
            lista1.listar()
        elif op == "10":
            lista1.ordenar_desc()
            print("  Lista ordenada de mayor a menor:")
            lista1.listar()
        elif op == "11":
            lista1.reversar()
            print("  Lista invertida:")
            lista1.listar()
        elif op == "12":
            copia = lista1.copiar()
            copia.reversar()
            print("  Copia creada y reversada:")
            copia.listar()
            print("  Lista original (sin cambios):")
            lista1.listar()
        elif op == "13":
            total = lista1.longitud()
            print(f"  Total de pasajeros: {total}")
        elif op == "C":
            cargar_datos_prueba(lista1)
        elif op == "0":
            break
        else:
            print("  Opcion no valida")


def menu_lista2():
    while True:
        mostrar_opciones("MENU 2 - list de Python", extras=True)
        op = input("Opcion: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista2.añadir(pasajero):
                print("  Pasajero añadido")
        elif op == "2":
            lista2.listar()
        elif op == "3":
            pos = leer_entero("  Posicion a insertar: ")
            pasajero = leer_pasajero()
            if lista2.insertar(pos, pasajero):
                print(f"  Pasajero insertado en la posicion [{pos}]")
        elif op == "4":
            num = leer_entero("  No. de pasajero a buscar: ")
            pos = lista2.buscar(num)
            if pos != -1:
                print(f"  Encontrado en [{pos}]: {lista2.pasajeros[pos]}")
            else:
                print("  No existe un pasajero con ese numero")
        elif op == "5":
            num = leer_entero("  No. de pasajero a buscar (binaria): ")
            pos = lista2.buscar_binaria(num)
            if pos != -1:
                print(f"  Encontrado en [{pos}]: {lista2.pasajeros[pos]}")
            else:
                print("  No encontrado (recuerda ordenar ascendentemente primero)")
        elif op == "6":
            num = leer_entero("  No. de pasajero a modificar: ")
            nuevo_destino = input("  Nuevo destino: ").strip()
            nuevo_asiento = input("  Nuevo asiento: ").strip().upper()
            if lista2.modificar(num, nuevo_destino, nuevo_asiento):
                print("  Datos del pasajero actualizados")
            else:
                print("  No existe un pasajero con ese numero")
        elif op == "7":
            pos = leer_entero("  Posicion a eliminar: ")
            eliminado = lista2.eliminar_por_posicion(pos)
            if eliminado is not None:
                print(f"  Eliminado: {eliminado}")
            else:
                print("  Posicion fuera de rango")
        elif op == "8":
            num = leer_entero("  No. de pasajero a eliminar: ")
            if lista2.eliminar_por_valor(num):
                print(f"  Pasajero #{num} eliminado")
            else:
                print("  No existe un pasajero con ese numero")
        elif op == "9":
            lista2.ordenar_asc()
            print("  Lista ordenada de menor a mayor:")
            lista2.listar()
        elif op == "10":
            lista2.ordenar_desc()
            print("  Lista ordenada de mayor a menor:")
            lista2.listar()
        elif op == "11":
            lista2.reversar()
            print("  Lista invertida:")
            lista2.listar()
        elif op == "12":
            copia = lista2.copiar()
            copia.reversar()
            print("  Copia creada y reversada:")
            copia.listar()
            print("  Lista original (sin cambios):")
            lista2.listar()
        elif op == "13":
            total = lista2.longitud()
            print(f"  Total de pasajeros: {total}")
        elif op == "14":
            destino = input("  Destino a filtrar: ").strip()
            filtrados = lista2.filtrar_por_destino(destino)
            if filtrados:
                for p in filtrados:
                    print(f"  {p}")
            else:
                print("  (sin pasajeros para ese destino)")
        elif op == "15":
            mayores = lista2.mayores_de_edad()
            if mayores:
                for p in mayores:
                    print(f"  {p}")
            else:
                print("  (no hay pasajeros mayores de edad)")
        elif op == "C":
            cargar_datos_prueba(lista2)
        elif op == "0":
            break
        else:
            print("  Opcion no valida")


def main():
    while True:
        print("\n===== TAREA LISTAS - PASAJEROS =====")
        print("1. Menu 1 - MiLista")
        print("2. Menu 2 - list de Python")
        print("3. Salir")
        op = input("Opcion: ").strip()
        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            print("Hasta pronto!")
            break
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()