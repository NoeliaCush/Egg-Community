"""
1) Crea las funciones necesarias para que el usuario ingrese dos números
y el programa devuelva el resultado de una división. Prevé los posibles
errores del usuario. Luego, crea un paquete llamado 'mi_division'. En
él crea un archivo para cada función respectivamente. Fuera del
paquete, en un nivel superior, crea un archivo 'main.py' para que sea el
script que importe el paquete y ejecute el programa. Pon en práctica las
mejores prácticas que has aprendido.
"""

from mi_division import calculo
from mi_division import ingresar

def main() -> None:
    """
    Un usuario ingresa dos números y el programa lo divide
    """
    print("Voy a dividir")
    numeros = ingresar.ingresar_datos()
    if numeros:
        a, b = numeros
        division = calculo.dividir(a, b)
        if division:
            print(f"El resultado es {calculo.dividir}")
        else:
            print("No se obtuvo resultado")

main()

