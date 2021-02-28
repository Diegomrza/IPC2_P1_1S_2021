from ListaDoblementeEnlazada import ListaDoblementeEnlazada
from ListaSimple import ListaSimple
import xml.etree.ElementTree as ET
from xml import etree
#  C:\Users\Squery\Desktop\Proyecto 1 IPC2\Matriz.xml
#  C:\Users\Squery\Desktop\Proyecto 1 IPC2\Matriz2.xml
ruta = ""
lista_enlazada = ListaDoblementeEnlazada()

def cargar_archivo():
    global ruta 
    ruta = input()
    
def procesar_archivo(ruta):
    global lista_enlazada
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        
        for elemento in root:
            contador = 0
            lista_simple = ListaSimple()
            for subelemento in elemento:
                lista_simple.insertar(subelemento.attrib['x'], subelemento.attrib['y'], subelemento.text)
                contador += 1
            if int(elemento.attrib['n'])*int(elemento.attrib['m']) == contador and lista_enlazada.comprobar_nombre(elemento.attrib["nombre"]) != True:
                #matriz_patrones(lista_simple)
                lista_enlazada.insertar_final(elemento.attrib['nombre'], elemento.attrib['n'], elemento.attrib['m'], lista_simple)
            elif lista_enlazada.comprobar_nombre(elemento.attrib["nombre"]) == True:
                print("Matrices con nombres repetidos!")
                exit()
            else:
                print("Los tamaños de n, m, no coinciden con los datos leídos del archivo")
                exit()
        print('archivo procesado con exito\n')
    except IOError:
        print("El archivo no se pudo leer")

   
x = True
while x:
    print('\n\nMenú principal')
    print('      1. Cargar archivo')
    print('      2. Procesar archivo')
    print('      3. Escribir archivo de salida')
    print('      4. Mostrar datos del estudiante')
    print('      5. Generar gráfica')
    print('      6. Salida')

    entrada = input('Ingrese una opción\n')

    if entrada == '1':
        print('Ingrese la ruta del archivo: ')
        cargar_archivo()
    elif entrada == '2':
        print("Procesando archivo")
        procesar_archivo(ruta)
        lista_enlazada.mostrar()
    elif entrada == '3':
        print('opcion 3')
    elif entrada == '4':
        print('opcion 4')
    elif entrada == '5':
        print('opcion 5')
    elif entrada == '6':
        print('opcion 6')
        exit()
    elif int(entrada) > 6 or int(entrada) < 0:
        print('Opción inválida')