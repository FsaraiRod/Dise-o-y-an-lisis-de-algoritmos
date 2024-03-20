cantidad = int(input("Ingresar la cantidad: "))
matriz = []
for _ in range(cantidad):
    matriz.append([0] * cantidad)

arriba, abajo, izquierda, derecha = 0, cantidad-1, 0, cantidad-1

numero = 1

while numero <= cantidad * cantidad:

    for i in range(izquierda, derecha+1):
        matriz[arriba][i] = numero
        numero += 1
    arriba += 1

    for i in range(arriba, abajo+1):
        matriz[i][derecha] = numero
        numero += 1
    derecha -= 1

    for i in range(derecha, izquierda-1, -1):
        matriz[abajo][i] = numero
        numero += 1
    abajo -= 1

    for i in range(abajo, arriba-1, -1):
        matriz[i][izquierda] = numero
        numero += 1
    izquierda += 1

for fila in matriz:
    print(*fila)