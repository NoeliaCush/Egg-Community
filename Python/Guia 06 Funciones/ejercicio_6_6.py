"""
6) Crea una función llamada separar. Recibirá una lista de números enteros.
Devolverá dos listas ordenadas. La primera, con los números pares, y la
segunda, con los números impares. Documenta la función.
"""

def separar(numeros):
    numeros.sort()
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
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

