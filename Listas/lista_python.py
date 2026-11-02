from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):
        if self.buscar(pasajero.numero) != -1:
            print("  Ya existe un pasajero con ese numero")
            return False
        self.pasajeros.append(pasajero)
        return True

    def listar(self):
        if not self.pasajeros:
            print("  (lista vacia)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"  [{i}] {p}")

    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            print("  Posicion fuera de rango")
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  Ya existe un pasajero con ese numero")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    def buscar(self, numero):
        indices = [i for i, p in enumerate(self.pasajeros) if p.numero == numero]
        if len(indices) > 0:
            return indices[0]
        return -1

    def buscar_binaria(self, numero):
        claves = [p.numero for p in self.pasajeros]
        pos = bisect_left(claves, numero)
        if pos < len(self.pasajeros) and self.pasajeros[pos].numero == numero:
            return pos
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.pasajeros[pos].destino = nuevo_destino
        self.pasajeros[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            return None
        return self.pasajeros.pop(posicion)

    def eliminar_por_valor(self, numero):
        encontrados = [p for p in self.pasajeros if p.numero == numero]
        if len(encontrados) == 0:
            return False
        self.pasajeros.remove(encontrados[0])
        self.pasajeros = [p for p in self.pasajeros if p.numero != numero]
        return True

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=False)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva_lista = ListaPython()
        nueva_lista.pasajeros = self.pasajeros.copy()
        return nueva_lista

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):
        return [p for p in self.pasajeros if p.destino == destino]

    def mayores_de_edad(self):
        return [p for p in self.pasajeros if p.es_mayor_de_edad()]