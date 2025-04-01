# Trabajo con Archivos de Texto en Python
# Nombre: Cristian David Chiquimba Mena
# Fecha: 31 de marzo de 2025

"""
Este programa demuestra operaciones de lectura y escritura en archivos de texto en Python.
Sigue los pasos detallados en la tarea:
1. Escritura de Archivo de Texto
2. Lectura de Archivo de Texto
3. Cierre de Archivos
"""

print("---------- TRABAJO CON ARCHIVOS DE TEXTO EN PYTHON ----------")
print("Estudiante: Cristian David Chiquimba Mena")
print("Fecha: 31 de marzo de 2025")
print("-----------------------------------------------------------\n")

# PASO 1: ESCRITURA DE ARCHIVO DE TEXTO
print("PASO 1: ESCRITURA DE ARCHIVO DE TEXTO")
print("-------------------------------------")

# Creamos un nuevo archivo llamado 'my_notes.txt' en modo escritura ('w')
print("Creando y abriendo el archivo 'my_notes.txt' en modo escritura...")
archivo = open('my_notes.txt', 'w')
print("✓ Archivo abierto exitosamente.")

# Escribimos tres líneas de notas personales
print("\nEscribiendo notas personales en el archivo...")
print("- Escribiendo primera nota...")
archivo.write(
    "La programación es como la poesía del siglo XXI; cada línea de código es un verso que transforma ideas en realidad digital.\n")

print("- Escribiendo segunda nota...")
archivo.write(
    "Mi sueño es crear un algoritmo que pueda reconocer patrones en la música tradicional de mi región y generar nuevas composiciones que preserven nuestra identidad cultural.\n")

print("- Escribiendo tercera nota...")
archivo.write(
    "El mayor desafío que enfrenté en mi último proyecto fue implementar recursividad para resolver un problema que parecía imposible; después de tres noches sin dormir, la solución me llegó mientras tomaba un baño.\n")
print("✓ Notas escritas exitosamente.")

# PASO 3: CIERRE DE ARCHIVOS (Después de escribir)
print("\nCerrando el archivo después de escribir...")
archivo.close()
print("✓ Archivo cerrado correctamente.")

# PASO 2: LECTURA DE ARCHIVO DE TEXTO
print("\n\nPASO 2: LECTURA DE ARCHIVO DE TEXTO")
print("-----------------------------------")

# Abrimos el archivo en modo lectura ('r')
print("Abriendo el archivo 'my_notes.txt' en modo lectura...")
archivo = open('my_notes.txt', 'r')
print("✓ Archivo abierto exitosamente.")

# Leemos el contenido línea por línea
print("\nLeyendo y mostrando el contenido línea por línea:")
print("-------------------------------------------------")

# Inicializamos un contador para las líneas
contador = 1

# Leemos la primera línea
print(f"Leyendo línea {contador}...")
linea = archivo.readline()

# Mientras haya líneas por leer
while linea:
    # Mostramos la línea leída
    print(f"Línea {contador}: {linea}", end='')

    # Incrementamos el contador
    contador += 1

    # Leemos la siguiente línea
    if contador <= 3:  # Solo para mostrar el mensaje en las líneas que sabemos que existen
        print(f"Leyendo línea {contador}...")
    linea = archivo.readline()

print("\n✓ Lectura completada. Se leyeron", contador - 1, "líneas.")

# PASO 3: CIERRE DE ARCHIVOS (Después de leer)
print("\nCerrando el archivo después de leer...")
archivo.close()
print("✓ Archivo cerrado correctamente.")

print("\n-----------------------------------------------------------")
print("Operaciones con archivos de texto completadas exitosamente.")
print("-----------------------------------------------------------")