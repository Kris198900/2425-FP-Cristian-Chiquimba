# Definimos las temperaturas para las 7 ciudades, en 7 días de la semana, para 3 semanas consecutivas.
# Cada ciudad tiene 7 días de la semana, con temperaturas representadas para 3 semanas.

temperaturas = [
    [  # Quito
        [18, 19, 18],  # Lunes
        [19, 21, 20],  # Martes
        [18, 18, 17],  # Miércoles
        [20, 21, 19],  # Jueves
        [19, 20, 18],  # Viernes
        [22, 23, 21],  # Sábado
        [17, 18, 16]  # Domingo
    ],
    [  # Guayaquil
        [28, 30, 29],  # Lunes
        [30, 32, 31],  # Martes
        [29, 31, 30],  # Miércoles
        [31, 33, 32],  # Jueves
        [30, 32, 31],  # Viernes
        [33, 34, 32],  # Sábado
        [29, 30, 28]  # Domingo
    ],
    [  # Cuenca
        [15, 16, 15],  # Lunes
        [16, 17, 16],  # Martes
        [15, 16, 14],  # Miércoles
        [17, 18, 16],  # Jueves
        [16, 17, 15],  # Viernes
        [19, 20, 18],  # Sábado
        [14, 15, 13]  # Domingo
    ],
    [  # Ambato
        [18, 19, 18],  # Lunes
        [19, 20, 19],  # Martes
        [18, 19, 17],  # Miércoles
        [20, 21, 19],  # Jueves
        [19, 20, 18],  # Viernes
        [21, 22, 20],  # Sábado
        [17, 18, 16]  # Domingo
    ],
    [  # Riobamba
        [16, 17, 16],  # Lunes
        [17, 18, 17],  # Martes
        [16, 17, 15],  # Miércoles
        [18, 19, 17],  # Jueves
        [17, 18, 16],  # Viernes
        [19, 20, 18],  # Sábado
        [15, 16, 14]  # Domingo
    ],
    [  # Quevedo
        [26, 27, 28],  # Lunes
        [27, 28, 29],  # Martes
        [26, 27, 28],  # Miércoles
        [28, 29, 30],  # Jueves
        [27, 28, 29],  # Viernes
        [30, 31, 30],  # Sábado
        [26, 27, 28]  # Domingo
    ],
    [  # Tulcán
        [12, 13, 14],  # Lunes
        [13, 14, 13],  # Martes
        [12, 13, 12],  # Miércoles
        [14, 15, 14],  # Jueves
        [13, 14, 13],  # Viernes
        [15, 16, 15],  # Sábado
        [12, 13, 12]  # Domingo
    ]
]

# Nombres de las ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Riobamba", "Quevedo", "Tulcán"]

# Iteramos sobre las ciudades para calcular el promedio por semana
for i, ciudad in enumerate(temperaturas):
    print(f"Ciudad: {ciudades[i]}")

    # Iteramos sobre las semanas (3 semanas)
    for semana in range(3):  # Semanas 0, 1 y 2
        suma_temperaturas = 0

        # Iteramos sobre los días de la semana (7 días)
        for dia in ciudad:  # Lunes, Martes, etc.
            suma_temperaturas += dia[semana]

        # Calculamos el promedio para la semana
        promedio = suma_temperaturas / 7  # Promedio de 7 días
        print(f"Semana {semana + 1}: Promedio de temperatura = {promedio:.2f}°C")

    print()  # Imprimir una línea en blanco entre las ciudades
