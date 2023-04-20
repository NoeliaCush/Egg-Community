from typing import Any

from . import convertir


def entero_natural(entrada: Any) -> bool | int:
    """Valida si un entero es mayor a 0"""
    entero_natural = convertir.a_int(entrada)
    if not entero_natural > 0:
        return False
    return entero_natural
    

def cadena_no_vacia(entrada: Any) -> bool | str:
    """Valida si una cadena no es vacía"""
    cadena = convertir.a_str(entrada)
    cadena = str(cadena).strip()
    if not len(cadena) > 0:
        return False
    return cadena


def real_positivo(entrada: Any) -> bool | float:
    """Valida si un numero real es positivo"""
    real_positivo = convertir.a_float(entrada)
    if not real_positivo > 0:
        return False
    return real_positivo