# Nombre: Cristian David Chiquimba Mena
# Tarea: Trabajo con Archivos de Texto en Python

# Escritura del archivo de texto
try:
    # Abrimos el archivo en modo escritura ('w'), si no existe lo crea.
    with open('my_notes.txt', 'w') as file:
        # Escribimos tres líneas de notas personales
        file.write("Esta es mi primera nota personal.\n")
        file.write("Estoy aprendiendo a trabajar con archivos de texto en Python.\n")
        file.write("Esta es la tercera línea de mis notas.\n")
    print("Notas escritas con éxito en 'my_notes.txt'.")
except Exception as e:
    print(f"Error al escribir en el archivo: {e}")

# Lectura del archivo de texto
try:
    # Abrimos el archivo en modo lectura ('r')
    with open('my_notes.txt', 'r') as file:
        # Leemos cada línea del archivo y la imprimimos
        print("\nLeyendo el archivo 'my_notes.txt':")
        for linea in file:
            print(linea.strip())  # Eliminamos el salto de línea extra al imprimir
except Exception as e:
    print(f"Error al leer el archivo: {e}")

# No es necesario cerrar el archivo porque 'with' se encarga de cerrarlo automáticamente al finalizar.
