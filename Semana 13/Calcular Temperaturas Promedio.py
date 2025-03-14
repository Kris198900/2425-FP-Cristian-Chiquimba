def calcular_temperaturas_promedio(temperaturas):
    """
    Esta función recibe un diccionario con las temperaturas de varias ciudades durante varias semanas
    y devuelve el promedio de temperaturas por ciudad.
    """
    promedios = {}
    for ciudad, temps in temperaturas.items():
        promedio = sum(temps) / len(temps)
        promedios[ciudad] = promedio
    return promedios

# Datos de temperaturas de las ciudades en grados Fahrenheit
temperaturas = {
    "Rusia (Moscú)": [23, 27, 30, 25],
    "Alaska (Anchorage)": [18, 22, 20, 19],
    "Quito (Ecuador)": [66, 68, 70, 69],
}

# Llamar a la función
resultado = calcular_temperaturas_promedio(temperaturas)

# Mostrar los resultados
print("Promedio de temperaturas por ciudad (en grados Fahrenheit):")
for ciudad, promedio in resultado.items():
    print(f"{ciudad}: {promedio:.2f}°F")
