"""
1) Crea una función llamada área_rectángulo que devuelva el área del
rectángulo a partir de una base y una altura. El área de un rectángulo se
obtiene al multiplicar la base por la altura. El usuario debe ingresar dos
números, el resultado se guarda en una variable y se imprime el valor de
la variable mostrándola al usuario. Documenta la función.
"""
def area_rectangulo(base, altura):
    """Calcular el área de un rectángulo
    - Parámetros:
        base: float o int ingresados por el usuario
        altura: float o int ingresados por el usuario
    -Return float o int
    """
    return (base * altura)

base = float(input("Ingrese un valor de base: "))
altura = float(input("Ingrese un valor de altura: "))

print(f"El área del rectángulo es {area_rectangulo(base, altura)}")
