class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(nodo.derecha, valor)

    def in_orden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        resultado = []
        if nodo.izquierda:
            resultado += self.in_orden(nodo.izquierda)
        resultado.append(nodo.valor)
        if nodo.derecha:
            resultado += self.in_orden(nodo.derecha)
        return resultado

    def pre_orden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        resultado = [nodo.valor]
        if nodo.izquierda:
            resultado += self.pre_orden(nodo.izquierda)
        if nodo.derecha:
            resultado += self.pre_orden(nodo.derecha)
        return resultado

    def post_orden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        resultado = []
        if nodo.izquierda:
            resultado += self.post_orden(nodo.izquierda)
        if nodo.derecha:
            resultado += self.post_orden(nodo.derecha)
        resultado.append(nodo.valor)
        return resultado

def mezclar_in_orden(arbol1, arbol2):
    in_orden1 = arbol1.in_orden()
    in_orden2 = arbol2.in_orden()

    mezcla = in_orden1 + in_orden2
    mezcla.sort()  

    nuevo_arbol = ArbolBinario()
    for valor in mezcla:
        nuevo_arbol.insertar(valor)

    return nuevo_arbol, nuevo_arbol.in_orden()

arbol1 = ArbolBinario()
arbol1.insertar(5)
arbol1.insertar(3)
arbol1.insertar(7)

arbol2 = ArbolBinario()
arbol2.insertar(8)
arbol2.insertar(4)
arbol2.insertar(6)

print("Recorrido InOrden de Árbol 1:", arbol1.in_orden())
print("Recorrido PreOrden de Árbol 1:", arbol1.pre_orden())
print("Recorrido PostOrden de Árbol 1:", arbol1.post_orden())

print("Recorrido InOrden de Árbol 2:", arbol2.in_orden())
print("Recorrido PreOrden de Árbol 2:", arbol2.pre_orden())
print("Recorrido PostOrden de Árbol 2:", arbol2.post_orden())

nuevo_arbol, recorrido = mezclar_in_orden(arbol1, arbol2)

print("\nRecorrido InOrden del árbol mezclado:", recorrido)