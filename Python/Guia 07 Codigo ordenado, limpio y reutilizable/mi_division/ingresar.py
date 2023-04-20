
def ingresar_datos() -> tuple[float, float] | None:
    """
    El usuario ingresa 2 entradas. La función devuelve 2 floats
    Devuelve None si no introduce números o si da error.
    """
    try:
        a = float(input("¿Dividendo? "))
        b = float(input("¿Divisor? "))
    except ValueError:
        print("No se puede dividir si no se pone números")
        return None
    except KeyboardInterrupt:
        print("\n Salió sin introducir lo necesario")
        return None
    else:
        return a, b