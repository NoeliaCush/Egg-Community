"""
8) Un usuario debe ingresar un número entero, y puede ingresar los dígitos
precedidos (sin espacios) del signo '+' o el signo '-'. Ejemplo: 2000,
-2000 o +2000. Luego de que haya ingresado el número, la función
'validar_número' debe recibir como parámetro esa cadena de texto,
analizarla, y devolver True si cumple las condiciones, si no, False. Si la
función devuelve True, debes convertir la cadena a un entero.
Documentar la función. Imprimir el resultado.
"""

def validar_numero(entrada):
    """Valida si el parámetro recibido es un entero positivo o negativo"""
    validar_1 = entrada.isdecimal()
    validar_2 = entrada[0] in ("-")
    validar_3 = entrada[1:].isdecimal()
    if validar_1 or (validar_2 and validar_3):
        entrada = int
        return True
    else:
        return False


def main():
    while True:
        entrada = input("Ingrese un número")
        valido = validar_numero(entrada)
        print(valido)

main()
