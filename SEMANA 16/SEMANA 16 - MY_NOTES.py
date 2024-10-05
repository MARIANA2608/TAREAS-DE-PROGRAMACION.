# Escritura de Archivo de Texto
# Creamos un nuevo archivo llamado 'my_notes.txt' en modo de escritura ('w')
with open('my_notes.txt', 'w') as archivo:
    # Escribimos al menos tres notas personales en el archivo
    archivo.write("MI NOMBRE ES MARIANA CASCO, ME GUSTA LA NATACIÓN.\n")
    archivo.write("ME GUSTAN LOS DEPORTES.\n")
    archivo.write("TRABAJO EN RIOBAMBA.\n")

# Lectura de Archivo de Texto línea por línea utilizando readline()
# Abrimos el archivo en modo de lectura ('r')
with open('my_notes.txt', 'r') as archivo:
    # Leemos el archivo línea por línea usando readline()
    print("Leyendo el contenido línea por línea:")
    while True:
        linea = archivo.readline()  # Leer una línea a la vez
        if not linea:  # Si no quedan más líneas, salimos del bucle
            break
        print(linea.strip())  # Mostramos la línea en la consola, removiendo los saltos de línea extra

# No es necesario cerrar el archivo manualmente porque el uso de 'with' lo hace automáticamente.
