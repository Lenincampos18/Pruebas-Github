class DivisoresNumero:   # Clase encargada de obtener y ordenar los divisores del número.
    def __init__(self):   # Constructor, se ejecuta cuando se crea el objeto.
        while True:   # Bucle para validar la entrada correcta.
            try:
                self.n = int(input("Ingrese un número entero mayor o igual a 2): "))  # Se solicita el número al usuario.
                if self.n >= 2:   # Se verifica que sea mayor o igual a 2 como indica el enunciado.
                    break
                print("Por favor ingrese un número entero >= 2.")   # Mensaje si el valor no es válido.
            except ValueError:   # Se captura si el usuario ingresa algo que no es número.
                print("Entrada inválida. Intente nuevamente.")   # Mensaje de advertencia.
        
        self.lista = []   # Lista donde se guardaran los divisores.

    def obtener_divisores(self):   # Método q calcula los divisores del número.
        for i in range(1, self.n + 1):   # Se recorre desde 1 hasta el número ingresado.
            if self.n % i == 0:   # Si la división da residuo 0, entonces es divisor.
                self.lista.append(i)   # Se agrega el divisor a la lista
    
    def ordenar_seleccion_desc(self):   # Método para ordenar de mayor a menor usando Algoritmo Selección.
        for i in range(len(self.lista) - 1):   # Se recorre cada posición de la lista.
            max_idx = i   # Se supone que la posición actual es la mayor.
            for j in range(i + 1, len(self.lista)):   # Se busca si existe un número mayor más adelante.
                if self.lista[j] > self.lista[max_idx]:   # Comparación para encontrar el mayor.
                    max_idx = j   # Se guarda la posición del mayor encontrado.
            # Intercambio de valores (swap)
            self.lista[i], self.lista[max_idx] = self.lista[max_idx], self.lista[i]   # Cambiamos el valor mayor al inicio.
    
    def mostrar(self):   # Método para mostrar la lista de divisores.
        print(f"\nLos divisores de {self.n} son:")   # Mensaje descriptivo.
        print(self.lista)   # Se imprime la lista tal cual.
    
    def mostrar_ordenado(self):   # Método para mostrar después de ordenar.
        print(f"\nEl arreglo de los divisores de {self.n} , ordenados de mayor a menor por el Alg. de Selección es:")   # Encabezado de salida.
        print(self.lista)   # Se imprime la lista ya ordenada


#Bloque Principal
obj = DivisoresNumero()   
obj.obtener_divisores()  
obj.mostrar()  
obj.ordenar_seleccion_desc()   
obj.mostrar_ordenado()   
