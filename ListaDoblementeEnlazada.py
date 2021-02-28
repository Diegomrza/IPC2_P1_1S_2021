from NodoMatrices import Matrices
class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None

    def insertar_final(self, nombre, n, m, matriz):
        nodo_nuevo = Matrices(nombre, n, m)
        nodo_nuevo.matriz = matriz
        #self.matriz = matriz
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
            print(temporal.nombre, " n=", temporal.n, " m=", temporal.m)
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