from NodoMatrices import Matrices
from ListaSimple import ListaSimple
class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None

    def insertar_final(self, nombre, n, m, matriz):
        nodo_nuevo = Matrices(nombre, n, m)
        nodo_nuevo.matriz = matriz
        self.matroz(matriz, n, m)

        if self.primero is None:
            self.primero = nodo_nuevo
        else:
            temporal = self.primero
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nodo_nuevo
            nodo_nuevo.anterior = temporal
       
    def mostrar(self):
        temporal = self.primero
        while temporal is not None:
            print(temporal.nombre, " n =", temporal.n, " m =", temporal.m)
            temporal.matriz.mostrar()
            temporal = temporal.siguiente
        
    def comprobar_nombre(self, nombre_a_comparar):
        aux = self.primero
        
        while aux != None and aux.siguiente != self.primero:
            if aux.nombre == nombre_a_comparar:
                return True
            aux = aux.siguiente

        return False

    def vacia(self):
        return self.primero == None

    def matroz(self, matriz, n, m):

        obj_l_p = ListaSimple()
        
        for i in range(0, n):
            for j in range(0, m):
                val = 0
                if matriz.pos(i+1, j+1) > 0:
                    val = 1
                obj_l_p.insertar(i+1, j+1, val)
                
        print("\nMatriz binaria")
        obj_l_p.mostrar()