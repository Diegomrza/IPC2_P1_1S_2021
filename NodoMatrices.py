from ListaSimple import ListaSimple

class Matrices:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.matriz = ListaSimple()
        self.siguiente = None
        self.anterior = None
