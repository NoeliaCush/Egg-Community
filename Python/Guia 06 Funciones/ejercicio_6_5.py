"""
5) Crea una función llamada recortar. Recibirá tres parámetros. El primero
es el número (a recortar), el segundo es el "límite inferior" y el tercero el
"límite superior". La función hará lo siguiente:
Devolver el "límite inferior", si el número (a recortar) es menor que este.
Devolver el "límite superior", si el número es mayor que este.
Devolver el "número" sin cambios, si no se supera ningún límite.
"""

def recortar (num_recorte, limite_inferior, limite_superior):
    """Parámetros:
    - num_recorte_ int
    - limite_inferior: int
    - limite_ superior: int"""
    #Devuelve Limite Inferior si el numero es MENOR que el LI
    if num_recorte < limite_inferior:
        return limite_inferior
    #Devuelve el Limite Superior si el numero es MAYOR que el LS
    elif num_recorte > limite_superior:
        return limite_superior
    #Devuelve el número si NO supera ningún limite
    else:
        return num_recorte

num_recorte = int(input("Ingrese el numero a recortar: "))
limite_inferior = int(input("Ingrese el numero que será el limite inferior: "))
limite_superior = int(input("Ingrese el numero que será el limite superior: "))

print(recortar(num_recorte, limite_inferior, limite_superior))
