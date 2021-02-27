from NodoSimple import NodoSimple

class ListaSimple:
    def __init__(self):
        self.primero = None

    def insertar(self, x, y, contenido):
        nuevo = NodoSimple(x, y, contenido)
        if self.primero is None:
            self.primero = nuevo
        else:
            temporal = self.primero
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo

    def mostrar(self):
        tmp = self.primero
        while tmp is not None:
            print('ccx: ' + tmp.x + '\tccy: ' + tmp.y + '\tContenido: ' + tmp.contenido)
            tmp = tmp.siguiente
    
    def patrones(self):
        print("hello")
        self.mostrar()
        return None