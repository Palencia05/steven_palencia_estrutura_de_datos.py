class BaseDatos:
    def __init__(self):
        self.lista_pares = []
        self.lista_impares = []

    def crear_tupla_pares(self, numeros):
        self.lista_pares = [n for n in numeros if n % 2 == 0]
        print(f"Tupla de pares: {tuple(self.lista_pares)}")

    def crear_tupla_impares(self, numeros):
        self.lista_impares = [n for n in numeros if n % 2 != 0]
        print(f"Tupla de impares: {tuple(self.lista_impares)}")

    def ver_tuplas(self):
        print(f"Pares: {tuple(self.lista_pares)}")
        print(f"Impares: {tuple(self.lista_impares)}")

    def modificar_valor(self, tipo, indice, nuevo_valor):
        if tipo == "par":
            if 0 <= indice < len(self.lista_pares):
                self.lista_pares[indice] = nuevo_valor
                print(f"Nueva tupla de pares: {tuple(self.lista_pares)}")
            else:
                print("Índice fuera de rango.")
        elif tipo == "impar":
            if 0 <= indice < len(self.lista_impares):
                self.lista_impares[indice] = nuevo_valor
                print(f"Nueva tupla de impares: {tuple(self.lista_impares)}")
            else:
                print("Índice fuera de rango.")

    def eliminar_valor(self, tipo, valor):
        if tipo == "par":
            if valor in self.lista_pares:
                self.lista_pares.remove(valor)
                print(f"Actual tupla de pares: {tuple(self.lista_pares)}")
            else:
                print("Valor no encontrado.")
        elif tipo == "impar":
            if valor in self.lista_impares:
                self.lista_impares.remove(valor)
                print(f"Actual tupla de impares: {tuple(self.lista_impares)}")
            else:
                print("Valor no encontrado.")
