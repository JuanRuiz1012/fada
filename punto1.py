#escribir un programa que comience con una pila de enteros inicialmente vacia 
#y que ejecute una lista de las siguientes operaciones:
#1. agregar un elemento
#2. quitar los dos ultimos elementos de la pila calcular la suma y añadir el resultado a la pila
#3. toma N primeros elementos de la pila los suma y apilo los elemntos al valor obtenido 
#4. imprime el valor de la pila

#poner el tope al principio o al final

def main():
    stack = []
    while True:
        
        print("1. Agregar un elemento")
        print("2. Quitar los dos ultimos elementos de la pila calcular la suma y añadir el resultado a la pila")
        print("3. Toma N primeros elementos de la pila los suma y apilo los elemntos al valor obtenido")
        print("4. Imprime el valor de la pila")
        print("5. Salir")
        print("Escriba una opcion: ")
        opcion = int(input())
        if opcion == 1:
            print("Escriba el elemento a agregar: ")
            elemento = int(input())
            stack.append(elemento)
        elif opcion == 2:
            if len(stack) > 1:
                c = stack.pop()
                d = stack.pop()
                suma = c+ d
                stack.append(suma)
        elif opcion == 3:
            if len(stack) > 0:
                N = int(input("Escriba N: "))
                suma = 0
                for i in range(N):
                    suma += stack.pop()
                stack.insert(0, suma)
        elif opcion == 4:
            if len(stack) > 0:
                print(stack)
        elif opcion == 5:
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()     