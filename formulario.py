from lista_datos import lista_numeros

objlista = lista_numeros()


class calculadora:
    def pedir_numero(self):
        numero1= input("numero 1: ")
        numero2= input("numero 2: ")
        return numero1, numero2
        
        
    
    def almacenar_numero(self, numero1, numero2):
        dato_numero = [numero1, numero2]
        print(dato_numero)
        objlista.guardar_numero(dato_numero)
        objlista.guardar_numero(dato_numero)
        objlista.guardar_numero([1,5])
        print(objlista.lista_numero)
        
        
    
        
#codigo principal

objcalculadora = calculadora()
auxnum1, auxnum2= objcalculadora.pedir_numero()
objcalculadora.almacenar_numero(auxnum1, auxnum2)