#Se utlizara la estructura de datos de la lista simple y doblemente enlazada
#Operaciones :
#1. avanza el elemento A, k nodos, el valor de k puede ser negativo lo que implica
# que puede retrocder tener en cuenta el caso de Head y Tail
#2. Inserta un nodo con el valor V a la izquierda de la posicion actual del nodo K
#3. Iserta un nodo con valor V a la derecha de la posicion actual del nodo K
#4. Elimina el nodo a la izquierda del nodo K
#5. Elimina el nodo a la derecha del nodo K
#6. quitara el nodo V de su posicion actual y lo insertara antes del nodo X
#7. quitara el nodo V de su posicion actual y lo insertara despues del nodo X
#8. imprime el resultado 

#####################################################################################
#### PENDIENTE AGREGAR UNA FUNCION QUE INSERTE Y ALMACENE LOS DATOS EN LA LISTA   ###
#####################################################################################



class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class Lista:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def avanza(self, k):
        if k == 0:
            return self.cabeza
        elif k > 0:
            nodo = self.cabeza
            for i in range(k):
                nodo = nodo.derecho
            return nodo
        else:
            nodo = self.cola
            for i in range(k*-1):
                nodo = nodo.izquierdo
            return nodo
    
    def insertaIzquierda(self, valor, k):
        nodo = Nodo(valor)
        if k == 0:
            nodo.izquierdo = self.cabeza
            nodo.derecho = self.cabeza.derecho
            self.cabeza.derecho.izquierdo = nodo
            self.cabeza.derecho = nodo
        else:
            nodo.izquierdo = self.avanza(k-1).izquierdo
            nodo.derecho = self.avanza(k-1)
            nodo.izquierdo.derecho = nodo
            nodo.derecho.izquierdo = nodo
        
    def insertaDerecha(self, valor, k):
        nodo = Nodo(valor)
        if k == 0:
            nodo.izquierdo = self.cabeza.izquierdo
            nodo.derecho = self.cabeza
            self.cabeza.izquierdo.derecho = nodo
            self.cabeza.izquierdo = nodo
        else:
            nodo.izquierdo = self.avanza(k-1)
            nodo.derecho = self.avanza(k-1).derecho
            nodo.izquierdo.derecho = nodo
            nodo.derecho.izquierdo = nodo
        
    def eliminaIzquierda(self, k):
        if k == 0:
            self.cabeza = self.cabeza.derecho
            self.cabeza.izquierdo = None
        else:
            nodo = self.avanza(k-1)
            nodo.izquierdo.derecho = nodo.derecho
            nodo.derecho.izquierdo = nodo.izquierdo
            
    def eliminaDerecha(self, k):
        if k == 0:
            self.cabeza = self.cabeza.izquierdo
            self.cabeza.derecho = None
        else:
            nodo = self.avanza(k-1)
            nodo.derecho.izquierdo = nodo.izquierdo
            nodo.izquierdo.derecho = nodo.derecho
    
    def quitaValor(self, valor, k):
        if k == 0:
            if self.cabeza.valor == valor:
                self.cabezh = self.cabeza.derecho
                self.cabeza.derecho = None
            else:
                nodo = self.cabeza
                while nodo.derecho.valor != valor:
                    nodo = nodo.derecho
                nodo.derecho = nodo.derecho.derecho
                nodo.derecho.izquierdo = nodo
        else:
            nodo = self.avanza(k-1)
            if nodo.valor == valor:
                nodo.izquierdo.derecho = nodo.derecho
                nodo.derecho.izquierdo = nodo.izquierdo
            else:
                while nodo.derecho.valor != valor:
                    nodo = nodo.derecho
                nodo.derecho = nodo.derecho.derecho
                nodo.derecho.izquierdo = nodo
    
    def quitaValorIzquierda(self, valor, k):
        if k == 0:
            if self.cabeza.valor == valor:
                self.cabezh = self.cabeza.izquierdo
                self.cabeza.izquierdo = None
            else:
                nodo = self.cabeza
                while nodo.izquierdo.valor != valor:
                    nodo = nodo.izquierdo
                nodo.izquierdo = nodo.izquierdo.izquierdo
                nodo.izquierdo.derecho = nodo
        else:
            nodo = self.avanza(k-1)            
            if nodo.derecho.valor == valor:
                nodo.derecho = nodo.derecho.derecho
            else:
                nodo = self.avanza(k-1)
                while nodo.derecho.valor != valor:
                    nodo = nodo.derecho
                nodo.derecho = nodo.derecho.derecho                
                nodo.derecho.izquierdo = nodo
    
    def imprime(self):
        if self.cabeza == None:
            print("La lista esta vacia")
        else:
            nodo = self.cabeza
            while nodo.derecho != None:
                print(nodo.valor)
                nodo = nodo.derecho
            print(nodo.valor)


def main():
    lista = Lista()
    while True:
        print("1. Avanza el elemento A, k nodos, el valor de k puede ser negativo lo que implica que puede retrocder tener en cuenta el caso de Head y Tail")
        print("2. Inserta un nodo con el valor V a la izquierda de la posicion actual del nodo K")
        print("3. Iserta un nodo con valor V a la derecha de la posicion actual del nodo K")
        print("4. Elimina el nodo a la izquierda del nodo K")
        print("5. Elimina el nodo a la derecha del nodo K")
        print("6. quitara el nodo V de su posicion actual y lo insertara antes del nodo X")
        print("7. quitara el nodo V de su posicion actual y lo insertara despues del nodo X")
        print("8. imprime el resultado")
        print("9. Salir")
        print("Escriba una opcion: ")
        opcion = int(input())
        if opcion == 1:
            print("Escriba el elemento a avanzar: ")
            k = int(input())
            nodo = lista.avanza(k)
            print(nodo.valor)
        elif opcion == 2:
            print("Escriba el valor a insertar: ")
            valor = int(input())
            print("Escriba la posicion a insertar: ")
            k = int(input())
            lista.insertaIzquierda(valor, k)
        elif opcion == 3:
            print("Escriba el valor a insertar: ")
            valor = int(input())
            print("Escriba la posicion a insertar: ")
            k = int(input())
            lista.insertaDerecha(valor, k)
        elif opcion == 4:
            print("Escriba la posicion a eliminar: ")
            k = int(input())
            lista.eliminaIzquierda(k)
        elif opcion == 5:
            print("Escriba la posicion a eliminar: ")
            k = int(input())
            lista.eliminaDerecha(k)
        elif opcion == 6:
            print("Escriba el valor a quitar: ")
            valor = int(input())
            print("Escriba la posicion a quitar: ")
            k = int(input())
            lista.quitaValor(valor, k)
        elif opcion == 7:
            print("Escriba el valor a quitar: ")
            valor = int(input())
            print("Escriba la posicion a quitar: ")
            k = int(input())
            lista.quitaValorIzquierda(valor, k)
        elif opcion == 8:
            lista.imprime()
        elif opcion == 9:
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()