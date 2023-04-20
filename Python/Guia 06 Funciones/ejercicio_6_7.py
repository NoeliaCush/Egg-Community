"""
7) Realiza el ejercicio anterior con el método de comprensión de listas.
"""
def separar(numeros):
    numeros.sort()
    pares = [numero for numero in numeros if numero%2 == 0]
    impares = [numero for numero in numeros if numero%2 != 0]
    return pares, impares

def main():
    bienvenida = "Ingresa numeros positivos y negativos"
    print(bienvenida)
    print("=" * len(bienvenida))
    lista = []
    cantidad = int(input("¿Cuántos numeros quieres ingresar?"))
    for n in range(cantidad):
        numero = int(input(f"{n + 1} número: "))
        lista.append(numero)
    pares, impares = separar(lista)
    print()
    print(f"Numeros pares: {pares}")
    print(f"Números impares: {impares}")

main()