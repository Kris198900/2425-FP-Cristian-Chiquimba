# Trabajo con Archivos de Texto en Python
# Nombre: Cristian David Chiquimba Mena
# Fecha: 31 de marzo de 2025

# PASO 1: ESCRITURA DE ARCHIVO DE TEXTO
print("PASO 1: ESCRITURA DE ARCHIVO DE TEXTO")
print("-------------------------------------")

try:
    # Creamos un nuevo archivo llamado 'my_notes.txt' en modo escritura
    archivo = open('my_notes.txt', 'w')

    # Escribimos tres líneas de notas personales diferentes
    archivo.write(
        "Reflexión personal: El aprendizaje de Python me ha abierto nuevas perspectivas sobre cómo resolver problemas cotidianos con tecnología.\n")
    archivo.write(
        "Proyecto futuro: Quiero desarrollar una aplicación que ayude a los estudiantes de mi comunidad a organizar mejor sus tareas y horarios de estudio.\n")
    archivo.write(
        "Nota importante: La gestión de archivos en Python es una habilidad fundamental que me permitirá trabajar con datos persistentes en mis aplicaciones.\n")

    # Cerramos el archivo después de escribir
    archivo.close()
    print("✓ Archivo creado y escrito exitosamente.")

except Exception as e:
    print(f"Error al escribir: {e}")

# PASO 2: LECTURA DE ARCHIVO DE TEXTO
print("\nPASO 2: LECTURA DE ARCHIVO DE TEXTO")
print("----------------------------------")

try:
    # Abrimos el archivo en modo lectura
    archivo = open('my_notes.txt', 'r')

    print("Contenido del archivo línea por línea:")

    # Leemos la primera línea
    linea = archivo.readline()
    contador = 1

    # Mientras haya líneas por leer
    while linea:
        # Mostramos la línea leída
        print(f"Línea {contador}: {linea}", end='')

        # Leemos la siguiente línea
        linea = archivo.readline()
        contador += 1

    # PASO 3: CIERRE DE ARCHIVOS
    archivo.close()
    print("\n✓ Archivo cerrado correctamente.")

except Exception as e:
    print(f"Error al leer: {e}")

print("\nOperaciones completadas exitosamente.")