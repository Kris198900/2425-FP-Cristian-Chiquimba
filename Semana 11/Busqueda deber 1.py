# Búsqueda de un número en la matriz

# Aquí creamos una matriz 3x3 con números
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Definimos la función para buscar un número en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):  # Recorremos las filas
        for j in range(len(matriz[i])):  # Recorremos las columnas
            if matriz[i][j] == valor:  # Si el número está en la posición (i, j)
                return (i, j)  # Regresamos la posición de la fila y columna
    return None  # Si no se encuentra el valor, regresamos None

# Vamos a buscar el número 3
valor_buscado = 3

# Llamamos a la función y mostramos el resultado
posicion = buscar_valor(matriz, valor_buscado)

if posicion:
    print(f"¡Sí! El número {valor_buscado} está en la posición {posicion}")
else:
    print(f"El número {valor_buscado} no está en la matriz.")
