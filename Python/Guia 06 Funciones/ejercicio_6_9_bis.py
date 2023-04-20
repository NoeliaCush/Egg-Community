"""
Copia y pega el ejercicio anterior en un nuevo archivo. Crea otra función,
'año_bisiesto' que reciba como parámetro un entero. La función debe
validar si el número ingresado corresponde a un año bisiesto o no.
Devuelve True o False. Documentar la función. Cuando el usuario ingresa
el input, la función 'validar_numero' devuelve True o False. Si es True,
llamar a 'año_bisiesto' y mostrar al usuario si lo ingresado es o no un
año bisiesto.
"""

def validar_numero(entrada):
    """Valida si el parámetro recibido es un entero positivo o negativo"""
    validar_1 = entrada.isdecimal()
    validar_2 = entrada[0] in ("-")
    validar_3 = entrada[1:].isdecimal()
    if validar_1 or (validar_2 and validar_3):
        return True
    else:
        return False
    
def año_bisiesto(año):
    """Valida si el entero recibido es un año bisiesto o no """
    validar_1 = año % 4 == 0
    validar_2 = not (año % 100 == 0)
    validar_3 = año % 400 == 0
    if validar_1 or (validar_2 and validar_3):
        return True
    else:
        return False
    

def main():
    while True:
        entrada = input("Ingrese un año (s: salir): ")
        if entrada == "s":
            break
        es_numero = validar_numero(entrada.strip())
        if not es_numero:
            continue
        año = int(entrada)
        es_año_bisiesto = año_bisiesto(año)
        if es_año_bisiesto:
            print(f"El año {año} si es bisiesto")
        else:
            print(f"No es bisiesto")

main()