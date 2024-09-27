# Primero, vamos a crear un diccionario llamado 'informacion_personal', que contiene información ficticia de una persona.
# Incluimos detalles básicos como su nombre, edad, ciudad donde vive y su profesión.
informacion_personal = {
    "nombre": "Jaime Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Ahora, accedemos al valor que está guardado en la clave 'ciudad', simplemente para ver cuál es la ciudad original de esta persona.
# Luego, procedemos a cambiar esa ciudad por otra, para simular que la persona se ha mudado a un nuevo lugar.
print(f"Ciudad original: {informacion_personal['ciudad']}")
informacion_personal["ciudad"] = "Guayaquil"  # Cambiamos la ciudad de 'Quito' a 'Guayaquil'.
print(f"Ciudad modificada: {informacion_personal['ciudad']}")  # Mostramos la nueva ciudad.

# Agregamos una nueva clave 'especializacion_profesional', para especificar el área de trabajo dentro de su profesión.
# Este es un ejemplo de cómo agregar más detalle sobre el trabajo de una persona.
informacion_personal["especializacion_profesional"] = "Ingeniería Civil"  # Especificamos el campo en el que trabaja.

# A continuación, verificamos si existe una clave llamada 'telefono' en nuestro diccionario.
# Si la clave no está presente, agregamos un número de teléfono ficticio, lo que es muy común en la vida real cuando necesitamos actualizar datos.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Como no había un teléfono, lo añadimos.

# Ahora vamos a eliminar la clave 'edad', ya que para este ejemplo no necesitamos mantener ese dato.
# Antes de eliminar, comprobamos que efectivamente la clave 'edad' exista en el diccionario para evitar posibles errores.
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminamos la clave 'edad' del diccionario.

# Finalmente, imprimimos el diccionario actualizado para ver cómo ha quedado después de todas las modificaciones que hemos hecho.
# Ahora podemos ver el resultado de las operaciones: la ciudad ha cambiado, se ha agregado el teléfono, una especialización profesional, y se ha eliminado la edad.
print("Diccionario final:")
print(informacion_personal)
