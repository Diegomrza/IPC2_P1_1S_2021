from ListaDoblementeEnlazada import ListaDoblementeEnlazada #Importación del TDA Lista Doble
from ListaSimple import ListaSimple                         #Importación del TDA Lista Simpre
import xml.etree.ElementTree as ET                          #Importacion de el módulo ElementTree
from xml import etree                                       #Importacion del módulo para leer archivos xml

#  C:\Users\Squery\Desktop\Proyecto 1 IPC2\Matriz.xml
#  C:\Users\Squery\Desktop\Proyecto 1 IPC2\Matriz2.xml

ruta = ""
lista_enlazada = ListaDoblementeEnlazada()

#Obtiene la ruta del archivo que se desea leer
def cargar_archivo(): 
    global ruta 
    ruta = input()
    
#Este método lee el archivo y lo ingresa en los tda listas
def procesar_archivo(ruta): 
    global lista_enlazada
    try:
        #Se obtiene todo el archivo leído
        tree = ET.parse(ruta)
        #Se obtiene la raíz del archivo
        root = tree.getroot()   
        #Con este for se recorre toda la raíz para buscar los diferentes elementos obtenidos dentro de ella
        for elemento in root:
            #Contador para comparar si las dimensiones de la matriz leída coinciden con los elementos del archivo
            contador = 0 
            #Lista simple temporal
            lista_simple = ListaSimple()
            #Con este for se ingresan todos los datos de una matriz en la lista simple 
            for subelemento in elemento: 
                lista_simple.insertar(subelemento.attrib['x'], subelemento.attrib['y'], subelemento.text)
                #Por cada elemento ingresado en la matriz temporal se aumenta en 1 el contador
                contador += 1 
                #Si los tamaños de n y m multiplicados coinciden con el numero del contador se ingresan
                #los datos a la lista doble
            if int(elemento.attrib['n'])*int(elemento.attrib['m']) == contador and lista_enlazada.comprobar_nombre(elemento.attrib["nombre"]) != True:
                #matriz_patrones(lista_simple)
                lista_enlazada.insertar_final(elemento.attrib['nombre'], elemento.attrib['n'], elemento.attrib['m'], lista_simple)
                
                #Se verifica que si un nombre de la matriz ya existe, no se deje ingresar otra matriz con 
                #el mismo nombre y se procede a cerrar el programa
            elif lista_enlazada.comprobar_nombre(elemento.attrib["nombre"]) == True:
                print("Matrices con nombres repetidos!")
                exit()
            else:
                #Si los tamaños de la n y m multiplicados no coinciden con el contador, no se deja
                #ingresar la matriz y se procede a cerrar el programa
                print("Los tamaños de n, m, no coinciden con los datos leídos del archivo")
                exit()
        print('archivo procesado con exito\n')
    except IOError:
        #Si el archivo posee algun tipo de error muestra un mensaje de que no se pudo leer
        print("El archivo no se pudo leer")

#Variable de tipo booleano para mantener el bucle while del menú siempre y cuando no se seleccione
#la opción de salir
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
        print('Saliento del programa')
        exit()
    elif int(entrada) > 6 or int(entrada) < 0:
        print('Opción inválida')