
def dividir(dividendo: float, divisor: float) -> float | None:
    """
    Función que devuelve la división entre dos números
    Devuelve None si hay un error
    """
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError as error:
        print(f"No se puede dividir por cero")
        return None
    else:
        return resultado