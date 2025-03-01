# Ordenación de una fila en la matriz con Bubble Sort

# Definimos la matriz
matriz = [
    [9, 2, 5],
    [3, 8, 1],
    [6, 7, 4]
]

# Función que ordena una fila de la matriz usando Bubble Sort
def ordenar_fila(matriz, fila):
    for i in range(len(matriz[fila]) - 1):  # Recorrimos la fila
        for j in range(len(matriz[fila]) - i - 1):  # Comparamos cada par de números
            if matriz[fila][j] > matriz[fila][j + 1]:  # Si están desordenados
                # Intercambiamos los valores
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Imprimimos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenamos la segunda fila (índice 1)
ordenar_fila(matriz, 1)

# Imprimimos la matriz después de ordenar la fila
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
