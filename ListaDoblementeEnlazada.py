from NodoMatrices import Matrices
class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None

    def insertar_final(self, nombre, n, m, matriz):

        nuevo = Matrices(nombre, n, m)
        nuevo.matriz = matriz

        if self.primero is None:
            self.primero = nuevo
        else:
            temporal = self.primero
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo
            nuevo.anterior = temporal
       
    def mostrar(self):
        temporal = self.primero
        while temporal is not None:
            print(temporal.nombre, " ", temporal.n, " ", temporal.m)
            temporal.matriz.mostrar()
            print()
            temporal = temporal.siguiente

    def vacia(self):
        return self.primero == None