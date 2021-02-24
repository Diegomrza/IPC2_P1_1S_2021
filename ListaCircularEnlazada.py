from NodoMatrices import Matrices
class ListaCircularEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def insertar_inicio(self, nombre, n, m):
        nuevo = Matrices(nombre, n, m)
        if self.vacia():
            self.primero = self.ultimo = nuevo
            self.ultimo.siguiente = self.primero
        else:
            print("Hola")

    def insertar_final(self, nombre, n, m):
        #nuevo = Matrices(nombre, n, m)
        if self.vacia():
            self.primero = self.ultimo = Matrices(nombre, n, m)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Matrices(nombre, n, m)
            self.ultimo.siguiente = self.primero 
       
    def mostrar(self):
        aux = self.primero
        while aux.siguiente != self.primero:
            print(aux.nombre, " ", aux.n, " ", aux.m)
            aux = aux.siguiente
        print(aux.nombre, " ", aux.n, " ", aux.m)

    