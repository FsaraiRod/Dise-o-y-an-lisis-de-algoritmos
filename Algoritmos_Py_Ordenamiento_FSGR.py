"""
Burbuja: Es un algoritmo simple pero menos eficiente para ordenar una lista o arreglo en Python.
Funciona revisando cada elemento con su adyacente y, si están desordenados, los intercambia.
"""
def burbuja(arr):
    n =  len(arr)
    for i in range (n):
        for j in range (0, n-i-1):
         if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
"""
Inserción: Es un algoritmo eficiente para listas pequeñas o casi ordenadas.
En este caso, se toma un elemento de la lista y se inserta en la posición correcta dentro de la parte ordenada de la lista.
Se repite este proceso para cada elemento de la lista hasta que esté completamente ordenada.
"""
def insercion(arr):
    n = len(arr)
    for i in range(1, n):
        valor = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > valor:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = valor
        
"""
Selección: Mejora el ordenamiento burbuja haciendo un sólo intercambio por cada pasada a través de la lista.
Busca el valor mayor a medida que hace una pasada y lo pone en la ubicación correcta. 
"""
def seleccion(arr):
    n = len(arr)
    for i in range(n):
        indice = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice]:
                indice = j
        arr[i], arr[indice] = arr[indice], arr[i]
        
"""
QuickSort: Es un algoritmo de ordenamiento eficiente que utiliza un enfoque de “divide y vencerás” para ordenar una lista de elementos.
Funciona mediante la selección de un “pivote” de la lista, la partición de la lista en dos sublistas de elementos menores y mayores
que el pivote, y luego la recursión de estos pasos en cada sublista hasta que todos los elementos estén ordenados.
"""
def particion(arr, izquierda, derecha):
    pivote = arr[derecha]
    i = izquierda - 1
    for j in range(izquierda, derecha):
        if arr[j] < pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[derecha] = arr[derecha], arr[i + 1]
    return i + 1

def quickSort(arr, izquierda, derecha):
    if izquierda < derecha:
        indice_pivote = particion(arr, izquierda, derecha)
        quickSort(arr, izquierda, indice_pivote - 1)
        quickSort(arr, indice_pivote + 1, derecha)

    
"""
MergeSort: es un método eficiente para ordenar listas. Funciona dividiendo la lista en mitades más pequeñas,
ordenándolas por separado y luego fusionándolas en una lista ordenada. 
"""
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mitad = len(arr) // 2
    izquierda = mergeSort(arr[:mitad])
    derecha = mergeSort(arr[mitad:])
    
    resultado = []
    i, j = 0, 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

"""
HeapSort:Se puede dividir en dos partes; una función que crea un montón mínimo o un montón máximo,
y una función que implementa el algoritmo de ordenación del montón real.
"""
def heapMon(arr, n, i):
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    if izquierda < n and arr[i] < arr[izquierda]:
        mayor = izquierda
    if derecha < n and arr[mayor] < arr[derecha]:
        mayor = derecha
    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heapMon(arr, n, mayor)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapMon(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapMon(arr, i, 0)

"""
Salidas
"""
lista_burbuja = [12, 49, 23, 5, 6, 2, 7]
print("Lista de ingreso:", lista_burbuja)
burbuja(lista_burbuja)
print("burbuja:", lista_burbuja)
print("\n") 

lista_insercion = [100, 52, 43, 22, 4, 1, 20]
print("Lista de ingreso:", lista_insercion)
insercion(lista_insercion)
print("insercion:", lista_insercion)
print("\n") 

lista_seleccion = [12, 11, 13, 5, 6, 7, 73, 13, 49, 234]
print("Lista de ingreso:", lista_seleccion)
seleccion(lista_seleccion)
print("seleccion:", lista_seleccion)
print("\n") 

lista_quickSort = [2, 54, 34, 1, 24, 43, 76, 29, 12, 25, 32]
print("Lista de ingreso:", lista_quickSort)
quickSort(lista_quickSort, 0, len(lista_quickSort) - 1)
print("quickSort:", lista_quickSort)
print("\n") 
      
lista_mergeSort = [3, 23, 21, 76, 56, 29, 63, 211, 54, 98, 84]
print("Lista de ingreso:", lista_mergeSort)
mergeSort(lista_mergeSort)
print("mergeSort:", lista_mergeSort)
print("\n") 

lista_heapSort = [63, 18, 35, 23, 111, 73, 432, 172, 2, 113, 863, 23, 43, 12, 1]
print("Lista de ingreso:", lista_heapSort)
heapSort(lista_heapSort)
print("heapSort:", lista_heapSort)