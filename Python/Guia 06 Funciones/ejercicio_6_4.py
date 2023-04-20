"""
4) Crea una función llamada intermedio. Recibirá dos argumentos de tipo
float. Devolverá el número intermedio. El número intermedio de dos
números corresponde a la suma de los dos números dividida entre 2.
Documenta la función.
"""

def intermedio(numero_1, numero_2):
    """Intermedio de dos numeros
    - Parametros:
        - numero_1 : float
        - numero_2 : float
    -return: suma de los parámetros dividido 2, float"""
    return ((numero_1 + numero_2) / 2)

numero_1 = float(input("Ingrese un numero: "))
numero_2 = float(input("Ingrese un numero: "))

print(f"El intermedio de {numero_1} y {numero_2} es {intermedio(numero_1, numero_2)}")