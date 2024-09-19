# Función para calcular el descuento en función del monto total y el porcentaje de descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado al monto total de la compra.

    Parámetros:
    monto_total (float): Monto total de la compra.
    porcentaje_descuento (float, opcional): Porcentaje de descuento (por defecto es 10%).

    Retorna:
    float: El monto del descuento calculado.
    """
    # Calcular el descuento
    descuento = monto_total * (porcentaje_descuento / 100)

    # Retornar el descuento calculado
    return descuento


# Monto total de las compras
monto_total1 = 150.0
monto_total2 = 200.0

# Llamada a la función con el valor predeterminado del descuento (10%)
descuento1 = calcular_descuento(monto_total1)
# Monto final a pagar
monto_final1 = monto_total1 - descuento1

# Llamada a la función con un porcentaje de descuento personalizado (15%)
descuento2 = calcular_descuento(monto_total2, 15)
# Monto final a pagar
monto_final2 = monto_total2 - descuento2

# Mostrar los resultados
print(f"Monto total: ${monto_total1}, Descuento: ${descuento1}, Monto final: ${monto_final1}")
print(f"Monto total: ${monto_total2}, Descuento: ${descuento2}, Monto final: ${monto_final2}")
