# CalculoDescuentoPython.py
# Programa para calcular el descuento en compras
# Autor: Cristian David Chiquimba Mena
# Fecha: 19/03/2025

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando un porcentaje al monto total de la compra.

    Args:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float, opcional): El porcentaje de descuento a aplicar. Por defecto es 10%.

    Returns:
        float: El monto del descuento calculado.
    """
    # Calculamos el descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


def main():
    """
    Función principal del programa que realiza llamadas a la función calcular_descuento
    y muestra los resultados.
    """
    print("Programa para calcular descuentos en compras")
    print("Autor: Cristian David Chiquimba Mena")
    print("-" * 40)

    # Primera llamada a la función con solo el monto total (usando descuento por defecto)
    compra1 = 1500.0
    descuento1 = calcular_descuento(compra1)
    monto_final1 = compra1 - descuento1

    print("\nPrimera compra:")
    print(f"Monto total: ${compra1:.2f}")
    print(f"Porcentaje de descuento: 10% (valor por defecto)")
    print(f"Monto de descuento: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}")

    # Segunda llamada a la función con monto total y porcentaje de descuento personalizado
    compra2 = 2500.0
    porcentaje2 = 15
    descuento2 = calcular_descuento(compra2, porcentaje2)
    monto_final2 = compra2 - descuento2

    print("\nSegunda compra:")
    print(f"Monto total: ${compra2:.2f}")
    print(f"Porcentaje de descuento: {porcentaje2}%")
    print(f"Monto de descuento: ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")


if __name__ == "__main__":
    main()