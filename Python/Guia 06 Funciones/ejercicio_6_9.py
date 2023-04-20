"""
9) Crea una función que reciba 3 parámetros de enteros: horas, minutos y
segundos, los convierta en "tiempo" y devuelva una tupla de enteros:
días, horas, minutos, segundos. El usuario debe introducir los datos
desde la consola y debe ver el resultado de forma legible. Una buena
práctica de programación es crear varias funciones que solamente
hagan una cosa. Trata de documentar brevemente cada función, y
separar la lógica, la interacción con el usuario y lo que se muestra por
pantalla:
"""
def tiempo_convertir(horas, minutos, segundos):
    """Convierte cualquier número al formato de tiempo estándar"""
    while segundos >= 60:
        minutos += segundos // 60
        segundos %= 60
    while minutos >= 60:
        horas += minutos // 60
        minutos %= 60
    dias = 0
    while horas >= 24:
        dias += horas // 24
        horas %= 24
    return(dias, horas, minutos, segundos)

def tiempo_formatear(dias, horas, minutos, segundos):
    """Representa en cadena: das, horas, minutos y segundos"""
    if dias == 1:
        tiempo = f"{dias} dia, {horas:02}h, {minutos:02}m, {segundos:02}s"
    elif dias >= 1:
        tiempo = f"{dias} dias, {horas:02}h, {minutos:02}m, {segundos:02}s"
    else:
        tiempo = f"{horas:02}h, {minutos:02}m, {segundos:02}s"
    return tiempo

def numeros_validar(*args):
    """Valida si todos los caracteres de una cadena son números"""
    for arg in args:
        if not arg.isdigit():
            return False
    return True

def main():
    """
    - Pregunta al usuario por horas, minutos y segundos
    - Valida si los datos son numeros: numeros_validar
    - Convierte los datos en tiempo:
    - Muestra el tiempo en una candena legible: tiempo_formatear
    """

    while True:
        print("Conversor de tiempo (sale sino introduce números)")
        horas = input("Horas: ")
        minutos = input("Minutos: ")
        segundos = input("Segundos: ")
        validacion = numeros_validar(horas, minutos, segundos)
        if not validacion:
            break
        else:
            horas = int(horas)
            minutos = int(minutos)
            segundos = int(segundos)
            tiempo_convertido = tiempo_convertir(horas, minutos, segundos)
            mensaje = tiempo_formatear(*tiempo_convertido)
            print(mensaje)


main()