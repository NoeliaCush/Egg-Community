"""
3) Crea una función llamada relación. Recibirá 2 parámetros de tipo
entero. Si el primer parámetro es mayor que el segundo, la función debe
devolver 1; pero si el primer número es menor que el segundo, debe
devolver -1. Si ambos números son iguales, debe devolver 0. Documenta
la función.

"""

def relacion(numero_1, numero_2):
    """Relación entre dos parametros
    - Parametros
        - numero_1: int
        - numero_2: int
    -return: int"""
    if numero_1 > numero_2:
        return 1
    elif numero_1 < numero_2:
        return -1
    else:
        return 0

numero_1 = int(input("Ingrese un entero: "))
numero_2 = int(input("Ingrese un entero: "))

print(f"El resultado de la relación entre {numero_1} y {numero_2} es {relacion(numero_1, numero_2)}")
