from NodoMatrices import Matrices
from ListaSimple import ListaSimple
from graphviz import Digraph
import xml.etree.ElementTree as ET 
class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
    #Método que inserta al final
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
    #Método que muestra los nodos en una lista doble
    def mostrar(self):
        temporal = self.primero
        while temporal is not None:
            print(temporal.nombre, " n =", temporal.n, " m =", temporal.m)
            temporal.matriz.mostrar()
            temporal = temporal.siguiente
    #Método que comprueba si el nombre de una matriz ya existe
    def comprobar_nombre(self, nombre_a_comparar):
        aux = self.primero
        
        while aux != None and aux.siguiente != self.primero:
            if aux.nombre == nombre_a_comparar:
                return True
            aux = aux.siguiente

        return False
    #Método que comprueba si una lista está vacía
    def vacia(self):
        return self.primero == None
    #Método que obtiene la matriz binaria
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
        self.prueba(obj_l_p, n, m)
        
    def prueba(self,obj_l_p, n, m):

        for x in range(0,n):
            lista_temporal = ListaSimple()
            for y in range(0,m):
                valor = obj_l_p.pos(x+1, y+1)
                lista_temporal.insertar(x+1,y+1,valor)
            codigo = self.comparar_filas(lista_temporal, obj_l_p, n, m, x+1)
            if codigo == True:
                print("Son iguales")

    def comparar_filas(self, fila, fila2, n, m, indice):
        for x in range(1,n+1):
            contador = 0
            for y in range(1, m+1):
                if indice == x:
                    break
                elif fila2.obtener_nodo(x,y) == fila.obtener_nodo(indice,y):
                    contador+=1
            if contador == m:
                print("Son iguales")
                return True
            else:
                return False

    def grafos(self, nombre):
        
        aux = self.primero
        name = ''
        n = ''
        m = ''
        while aux != None and aux.siguiente != self.primero:
            if nombre == aux.nombre:
                name = aux.nombre 
                n = str(aux.n)
                m = str(aux.m)
                matr = aux.matriz
                break
            aux = aux.siguiente

        g = Digraph('G', filename='grafo.gv', format='png')
        g.node('M',label='Matrices')
        g.node('E',label=name)
        g.node('n', label='n='+n)
        g.node('m', label='m='+m)
        
        g.edges(['ME','En','Em'])
        
        for x in range(0, aux.n):
            g.edges(['E'+str(x)])
            for y in range(0, aux.m):
                g.edges([str(y)+str(matr.obtener_nodo(y+1,x+1))])  
        
        g.render(r"grafo.png",view=True)
        
    def obtener_longitud(self):
        aux = self.primero
        datos = '<matrices>'

        while aux is not None:
            datos += '<matriz '+'nombre="'+aux.nombre+'" n="'+str(aux.n)+'" m="'+str(aux.m)+'">'
            for x in range(0, aux.n):
                for y in range(0, aux.m):
                    datos += '<dato '+'x="'+str(x)+'" y="'+str(y)+'">'+aux.matriz.obtener_nodo2(x+1,y+1)+'</dato>'
            datos += '</matriz>'
            aux = aux.siguiente
        datos += '</matrices>'
        myfile = open('final.xml', 'w')
        myfile.write(datos)
        myfile.close()

        print("Archivo creado satisfactoriamente")    
        