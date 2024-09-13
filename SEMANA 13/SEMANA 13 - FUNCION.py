def temperatura_promedio(ciudades_temperaturas):
    """
    Esta función se encarga de obtener el promedio de temperatura para un grupo de ciudades.

    Argumentos:
    ciudades_temperaturas (dict): Un diccionario que contiene como claves los nombres de las ciudades
                                  y como valores una lista de temperaturas diarias.

    Retorna:
    dict: Un diccionario que relaciona cada ciudad con su temperatura promedio.
    """
    # Diccionario para almacenar las temperaturas promedio de cada ciudad
    temperaturas_promedio = {}

    # Iteramos a través del diccionario de ciudades y sus respectivas temperaturas
    for ciudad, temperaturas in ciudades_temperaturas.items():
        # Calculamos el promedio sumando las temperaturas y dividiendo por la cantidad de valores
        promedio = sum(temperaturas) / len(temperaturas)
        # Asignamos el promedio calculado al diccionario de resultados
        temperaturas_promedio[ciudad] = promedio

    # Devolvemos el diccionario con las temperaturas promedio por ciudad
    return temperaturas_promedio


# Creamos un conjunto de datos para varias ciudades con sus respectivas temperaturas
ciudades_temperaturas = {
    "Ciudad 1": [19, 21, 23, 20, 22],
    "Ciudad 2": [26, 28, 27, 29, 25],
    "Ciudad 3": [16, 18, 17, 15, 19],
    "Ciudad 4": [31, 33, 34, 32, 30],
    "Ciudad 5": [23, 24, 22, 25, 21]
}

# Llamamos a la función y calculamos el promedio de temperaturas para cada ciudad
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los promedios calculados para cada ciudad
print("Promedio de Temperaturas por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    # Imprimimos el resultado formateado con dos decimales
    print(f"{ciudad}: {promedio:.2f}°C")
