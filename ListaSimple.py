from NodoSimple import NodoSimple

class ListaSimple:
    def __init__(self):
        self.primero = None
    #Método que inserta al final
    def insertar(self, x, y, contenido):
        nuevo = NodoSimple(x, y, contenido)
        if self.primero is None:
            self.primero = nuevo
        else:
            temporal = self.primero
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo
    #Método que muestra los elementos de una lista matriz
    def mostrar(self):
        tmp = self.primero
        while tmp is not None:
            print('ccx: ',  tmp.x, '\tccy: ', tmp.y, '\tContenido: ', tmp.contenido)
            tmp = tmp.siguiente
        print("")
    #Método que obtiene un valor por medio de sus coordenadas su posición
    def pos(self, fila, columna):
        aux = self.primero
        while aux != None:
            if  aux.x == fila and aux.y == columna:
                return aux.contenido
            else:
                aux = aux.siguiente
        return None
    def obtener_nodo(self,x,y):
        aux = self.primero
        while aux != None:
            if aux.x == x and aux.y == y:
                return aux.contenido
            aux = aux.siguiente

    def obtener_tamaño(self):
        aux = self.primero
        contador = 0
        while aux != None:
            contador += 1
            aux = aux.siguiente
        return contador 