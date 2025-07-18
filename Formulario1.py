from Lista_datos import ListaNumeros
from base_datos import BaseDatos

class Calculadora:
    def __init__(self):
        self.objlista = ListaNumeros()
        self.basedatos = BaseDatos()

    def pedir_lista_numeros(self):
        entrada = input("Ingrese números separados por coma (ej: 1,2,3): ")
        try:
            return [int(x.strip()) for x in entrada.split(",")]
        except ValueError:
            print("Entrada inválida.")
            return []

    def submenu_tuplas(self):
        while True:
            print("\n--- SUBMENÚ DE TUPLAS ---")
            print("1. Modificar valor en tupla")
            print("2. Eliminar valor de tupla")
            print("3. Ver tuplas")
            print("4. Volver al menú principal")
            opcion = input("Seleccione una opción (1-4): ")

            if opcion == "1":
                tipo = input("¿Modificar tupla 'par' o 'impar'?: ").lower()
                try:
                    indice = int(input("Índice a modificar: "))
                    nuevo = int(input("Nuevo valor: "))
                    self.basedatos.modificar_valor(tipo, indice, nuevo)
                except ValueError:
                    print("Entrada inválida.")
            elif opcion == "2":
                tipo = input("¿Eliminar de tupla 'par' o 'impar'?: ").lower()
                try:
                    valor = int(input("Valor a eliminar: "))
                    self.basedatos.eliminar_valor(tipo, valor)
                except ValueError:
                    print("Entrada inválida.")
            elif opcion == "3":
                self.basedatos.ver_tuplas()
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu(self):
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Agregar dos números a la lista")
            print("2. Insertar número en posición específica")
            print("3. Eliminar número de la lista")
            print("4. Mostrar lista")
            print("5. Eliminar último número")
            print("6. Buscar índice")
            print("7. Contar repeticiones")
            print("8. Ordenar lista")
            print("9. Invertir lista")
            print("10. Crear tupla con pares")
            print("11. Crear tupla con impares")
            print("12. Submenú de tuplas")
            print("13. Salir")

            opcion = input("Seleccione una opción (1-13): ")

            if opcion == "1":
                try:
                    n1 = float(input("Número 1: "))
                    n2 = float(input("Número 2: "))
                    self.objlista.incluir_lista([n1, n2])
                except ValueError:
                    print("Entrada inválida.")

            elif opcion == "2":
                try:
                    pos = int(input("Posición: "))
                    n1 = float(input("Número 1: "))
                    n2 = float(input("Número 2: "))
                    self.objlista.insertar_dato(pos, n2)
                    self.objlista.insertar_dato(pos, n1)
                except ValueError:
                    print("Entrada inválida.")

            elif opcion == "3":
                try:
                    n1 = float(input("Número 1: "))
                    n2 = float(input("Número 2: "))
                    self.objlista.eliminar_dato(n1)
                    self.objlista.eliminar_dato(n2)
                except ValueError:
                    print("Entrada inválida.")

            elif opcion == "4":
                self.objlista.ver_numero()

            elif opcion == "5":
                self.objlista.eliminar_ultimo()

            elif opcion == "6":
                try:
                    num = float(input("Buscar número: "))
                    self.objlista.buscar_indice(num)
                except ValueError:
                    print("Entrada inválida.")

            elif opcion == "7":
                try:
                    num = float(input("Número a contar: "))
                    self.objlista.contar_repetidos(num)
                except ValueError:
                    print("Entrada inválida.")

            elif opcion == "8":
                self.objlista.ordenar_lista()

            elif opcion == "9":
                self.objlista.invertir_lista()

            elif opcion == "10":
                nums = self.pedir_lista_numeros()
                self.basedatos.crear_tupla_pares(nums)

            elif opcion == "11":
                nums = self.pedir_lista_numeros()
                self.basedatos.crear_tupla_impares(nums)

            elif opcion == "12":
                self.submenu_tuplas()

            elif opcion == "13":
                print("¡Hasta luego!")
                break

            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    calc = Calculadora()
    calc.menu()
