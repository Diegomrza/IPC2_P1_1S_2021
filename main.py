from ListaCircularEnlazada import ListaCircularEnlazada

lista_nueva = ListaCircularEnlazada()

lista_nueva.insertar_final('matriz1', 5, 5)
lista_nueva.insertar_final('matriz2', 4, 4)
lista_nueva.insertar_final('matriz3', 3, 3)
lista_nueva.insertar_final('matriz4', 2, 2)
lista_nueva.insertar_final('matriz5', 1, 1)

print(lista_nueva.mostrar())


def cargar_archivo(ruta):
    try:
        with open(ruta) as file:
            contenido = file.read()
            print(contenido) 
    except:
        print('El archivo no pudo ser abierto porque el archivo: ' + ruta + ' no existe')
        
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
        ruta = input()
        cargar_archivo(ruta)
    elif entrada == '2':
        print('opcion 2')
    elif entrada == '3':
        print('opcion 3')
    elif entrada == '4':
        print('opcion 4')
    elif entrada == '5':
        print('opcion 5')
    elif entrada == '6':
        print('opcion 6')
        exit()