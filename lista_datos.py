class lista_numeros:
    def __init__(self):
        self.lista_numero = []
        
    def guardar_numero(self, dato_numero):
        self.lista_numero.append(dato_numero)
        print(f"[guardar_numero] Lista actual: {self.lista_numero}")
    
    def incluir_lista(self, dato_numero):
        self.lista_numero.extend(dato_numero)
        print(f"[incluir_lista] Lista actual: {self.lista_numero}")
    
    def insertar_dato(self, posicion, dato):
        self.lista_numero.insert(posicion, dato)
        print(f"[insertar_dato] Lista actual: {self.lista_numero}")
        
    def eliminar_dato(self, dato):
        if dato in self.lista_numero:
            self.lista_numero.remove(dato)
            print(f"[eliminar_dato] '{dato}' eliminado. Lista actual: {self.lista_numero}")
        else:
            print(f"[eliminar_dato] '{dato}' no encontrado en la lista.")
    
    def ver_numero(self):
        print(f"[ver_numero] Lista completa: {self.lista_numero}")
        return self.lista_numero
