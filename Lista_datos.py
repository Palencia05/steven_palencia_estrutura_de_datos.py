class ListaNumeros:
    def __init__(self):
        self.lista_numero = []

    def guardar_numero(self, dato_numero):
        self.lista_numero.append(dato_numero)
        print(f"Lista actual: {self.lista_numero}")

    def incluir_lista(self, datos):
        self.lista_numero.extend(datos)
        print(f"Lista actual: {self.lista_numero}")

    def insertar_dato(self, posicion, dato):
        if 0 <= posicion <= len(self.lista_numero):
            self.lista_numero.insert(posicion, dato)
            print(f"Lista actual: {self.lista_numero}")
        else:
            print("Posición inválida.")

    def eliminar_dato(self, dato):
        if dato in self.lista_numero:
            self.lista_numero.remove(dato)
            print(f"'{dato}' eliminado. Lista actual: {self.lista_numero}")
        else:
            print(f"'{dato}' no encontrado en la lista.")

    def ver_numero(self):
        print(f"Lista completa: {self.lista_numero}")
        return self.lista_numero

    def eliminar_ultimo(self):
        if self.lista_numero:
            eliminado = self.lista_numero.pop()
            print(f"Eliminado: {eliminado}. Lista actual: {self.lista_numero}")
        else:
            print("La lista está vacía.")

    def buscar_indice(self, dato):
        if dato in self.lista_numero:
            print(f"{dato} está en la posición {self.lista_numero.index(dato)}")
        else:
            print(f"{dato} no está en la lista.")

    def contar_repetidos(self, dato):
        print(f"{dato} aparece {self.lista_numero.count(dato)} veces")

    def ordenar_lista(self):
        self.lista_numero.sort()
        print(f"Lista ordenada: {self.lista_numero}")

    def invertir_lista(self):
        self.lista_numero.reverse()
        print(f"Lista invertida: {self.lista_numero}")
