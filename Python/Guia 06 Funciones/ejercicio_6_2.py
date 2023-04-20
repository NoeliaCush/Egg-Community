"""
2) Crea una función llamada área_círculo que devuelva el área de un
círculo a partir de un radio. El área de un círculo se obtiene al elevar el
radio a dos y multiplicando el resultado por el número pi. Importa el
módulo math para utilizar la variable/constante math.pi. Documenta la
función.
"""

import math 

def area_circulo(radio):
    """ Calcular el área de un circulo
    - Parametro:
        - radio: int o float
    - Return: int o float"""
    return (radio**2) * math.pi

radio = float(input("Ingrese el valor de radio: "))

print(f"El área del círculo es: {area_circulo(radio)}")
