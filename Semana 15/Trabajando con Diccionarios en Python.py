# Hecho por Cristian Chiquimba

# 1. Crear un Diccionario con información personal ficticia
# Se crea el diccionario 'informacion_personal' con claves y valores representando información básica de una persona.
informacion_personal = {
    "nombre": "Juan Perez",  # Nombre de la persona
    "edad": 28,              # Edad de la persona
    "ciudad": "Quito",       # Ciudad donde vive
    "profesion": "Ingeniero de Software"  # Profesión de la persona
}

# 2. Acceder y modificar el valor de la clave 'ciudad'
# Se accede al valor asociado a la clave "ciudad" y luego se cambia el valor a "Guayaquil".
print("Ciudad antes de modificar:", informacion_personal["ciudad"])  # Muestra la ciudad antes de modificar
informacion_personal["ciudad"] = "Guayaquil"  # Modificando la ciudad de Quito a Guayaquil
print("Ciudad después de modificar:", informacion_personal["ciudad"])  # Muestra la ciudad después de modificar

# 3. Agregar una nueva clave-valor para el teléfono
# Se agrega una nueva clave llamada "telefono" con un número ficticio de teléfono.
informacion_personal["telefono"] = "0998765432"  # Agregando un número de teléfono ficticio

# 4. Verificar existencia de la clave 'telefono' (ya se agregó en el paso anterior)
# Se verifica si la clave "telefono" está presente en el diccionario. Si no existe, se agregaría, pero en este caso ya fue agregado.
if "telefono" in informacion_personal:
    print("El teléfono está presente en el diccionario.")  # Si existe, se imprime un mensaje confirmando su existencia
else:
    print("El teléfono no está presente en el diccionario.")  # Si no existiera, se imprimiría este mensaje

# 5. Eliminar la clave 'edad' del diccionario
# La clave 'edad' se elimina del diccionario, ya que no es necesaria para este ejercicio.
del informacion_personal["edad"]  # Eliminando la clave 'edad' del diccionario

# 6. Imprimir el diccionario final
# Finalmente, se imprime el diccionario actualizado para mostrar cómo queda después de realizar todas las operaciones.
print("Diccionario final:", informacion_personal)  # Imprime el diccionario final con las modificaciones realizadas
