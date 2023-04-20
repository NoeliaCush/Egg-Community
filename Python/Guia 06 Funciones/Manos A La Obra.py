
"""
FUNCIÓN SIN PARÁMETRO:

def saludar():
    print("¡Hola!")

saludar()
"""
"""
RETORNO DE LAS FUNCIONES

    #Sin devolución:

def saludar():
print("¡Hola!")
    #return None
    return

resultado = saludar()
print(resultado)


    #Con devolución de datos primitivos

def saludar():
    print("¡Hola!")
    return("¡Adiós!")

resultado = saludar()
print(resultado)

    #Con devolución de expresión o cálculo numérico

def calcular():
    return 3 + 4 * 3

calculo = calcular()
print(calculo)

    #Con devolución de varios valores

def ver_saludos():
    return "hola", "adiós"

saludos = ver_saludos()
print(saludos)

    #Con devolución de datos

def ver_saludos():
    palabras = ("hola", "adiós")
    return palabras

saludos = ver_saludos()
print(saludos)

ÁMBITO DE LAS VARIABLES

variable_global = 10

def prueba():
    variable_local = 10_000
    print(variable_local)

print(variable_global)

prueba()

print(variable_local) #Variable no definida

variable_global = 999

def funcion_1():
    print("Valor en la función 1: ", variable_global)

def funcion_2():
    print("Valor en la función 2: ", variable_global)

funcion_1()
funcion_2()

variable_global = 999

def funcion_1():
    global variable_global
    variable_global = 12
    print("Valor en la función 1: ", variable_global)

funcion_1()
print(variable_global)
"""

"""
MANOS A LA OBRA 1

numero_1 = 10
numero_2 = 2

def media():
    print("La media es: ", ((numero_1+numero_2)/2))

media()
"""

"""
FUNCIONES CON PARÁMETROS

def saludar(nombre):
    print(f"¡Hola {nombre}!")

mi_nombre = input("¿Cuál es tu nombre?: ")
saludar(mi_nombre)

    # Argumentos de tipo inmutable

def cambiar(parametro):
    parametro += 1
    return parametro

variable = 1
variable = cambiar(variable)

print(variable)

    # Argumentos de tipo mutable

def cambiar(parametro):
    parametro.append(2)

variable = [1]
#cambiar(variable)
cambiar(variable.copy())
print(variable)

    #Argumentos por posición

def saludar(nombre, veces):
    for v in range(veces):
        print(f"¡Hola {nombre}!")

mi_nombre = input("¿Cuál es tu nombre?: ")
saludar(mi_nombre, 3)


    #Argumentos por nombre

def saludar(nombre, veces):
    for v in range(veces):
        print(f"¡Hola {nombre}!")

mi_nombre = input("¿Cuál es tu nombre?")
saludar(veces= 3, nombre=mi_nombre)


    #Parámetroos predeterminados

#Un parámetro requerido y un parámetro opcional:

def cuenta(nombre, apellido, saldo = 0):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    nombre_completo = f"{apellido}, {nombre}"
    return nombre_completo, saldo

persona_1 = cuenta("louis", "pasteur", 1000)
persona_2 = cuenta("nikola", "tesla")

print(persona_1)
print(persona_2)

#Dos parámetros opcionales

def cuenta(nombre="", saldo=0):
    if not nombre and not saldo:
        print("Faltan parámetros")
    else:
        print(f"El titular {nombre} tiene un saldo de ${saldo:.2f}")
    
cuenta()
cuenta("Tech", 100_000)
"""

"""
Manos A La Obra 2

def media(numero_1 = 0, numero_2 = 0):
    numero_1 = int(input("Numero 1: "))
    numero_2 = int(input("Numero 2: "))
    resultado = ((numero_1 + numero_2) / 2)
    return resultado

operacion = media()

print(f"Resultado = {operacion}")
"""
"""
DESEMPAQUE DE ARGUMENTOS

def cuenta(nombre, apellido):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    nombre_completo = f"{apellido}, {nombre}"
    return nombre_completo

persona_1 = ("louis", "pasteur")
persona_2 = {"nombre": "louis", "apellido": "pastaeur"}

prueba_1 = cuenta(*persona_1)
prueba_2 = cuenta(**persona_2)

print(prueba_1)
print(prueba_2)

def cuenta(nombre, apellido, saldo = 0):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    nombre_completo = f"{apellido}, {nombre}"
    return nombre_completo, saldo

personas= [("louis", "pasteur", 1000), ("nikola", "tesla")]

for p in personas:
    persona = cuenta(*p)
    print(persona)
"""
"""
ARGUMENTOS INDETERMINADOS
    #Argumentos de longitud variable


def promedio(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    promedio = suma / len(numeros)
    return promedio

x = promedio(5)
y = promedio(5, 7)
z = promedio(5, 7, 10, 9)

print(f"El promedio es {x:.1f}")
print(f"El promedio es {y:.1f}")
print(f"El promedio es {z:.1f}")

def enumerar_pedido(plato_del_dia, *args):
    print(f"\n1 - PLATO PRINCIPAL: {plato_del_dia}")
    for indice, valor in enumerate(args, start=2):
        print(f"{indice} - {valor}")

enumerar_pedido("muzzarela")
enumerar_pedido("cuatro quesos", "bebida", "postre")
enumerar_pedido(plato_del_dia="muzzarela")

    #Argumentos de longitud variable por nombre

def datos_personales(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, valor)

datos_personales(email = "email@mail.com", telefono = 1234)

datos_personales(**{"email":"email@mail.com", "telefono":1234})

def super_funcion(*args, **kwargs):
    total = 0
    for arg in args:
        total += arg
    print("Sumatoria: ", total)
    for kwarg in kwargs:
        print(f"{kwarg}: {kwargs[kwarg]}")

super_funcion(50, -1, 0.4, nombre="Uilises", edad=27)
"""

"""
FUNCIONES RECURSIVAS

def jugar(intento=1):
    print("Intento", intento)
    respuesta = input("¿De qué color es una naranja?")
    if respuesta != "naranja":
        if intento < 3:
            print("¡Fallaste! Intenta de nuevo...")
            intento += 1
            jugar(intento)
        else:
            print("¡Perdiste!")
    else:
        print("¡Ganaste!")

jugar()
"""
"""
DOCSTRING

def volumen_cubo(lado):
    ""Calcula el volumen de un cubo. Devuelve un flotante""
    volumen = lado**3
    return float(volumen)

print(volumen_cubo.__doc__)

def volumen_cubo(lado):
    ""
    Calcula el volumen de un cubo.
    -Parámetros:
        -lado: int o float
    -Return: float
    ""
    volumen = lado**3
    return float(volumen)

help(volumen_cubo)
"""

"""
Manos A La Obra 3 y 4 

def media(*args):
    ""
     La funcion calcula la media de los numeros recibido por parametros
    :param args: coleccion de numeros.
    :return: Float
    ""
    suma = 0
    for parametro in args:
        #suma = sum(parametro)
        for num in parametro:
            suma+= num
        return float(suma / len(parametro))


numeros = [2, 5, 6, 12, 3, 2, 55, 99.5]
numeros2 = []
veces = int(input("Ingrese la cantidad de nuemeros"))
for i in range(veces):
    numeros2.append(int(input("Ingrese un numero:")))
promedio = media(numeros2)

print(f"El promedio de los numeros{numeros2} es {promedio:.1f}")
print(sum(numeros2))

def promedio(*args):
    suma = 0
    for arg in args:
        suma += arg
    promedio = suma / len(args)
    return promedio

coleccion = (5, 7, 10, 9)
resultado = promedio(5, 7, 10, 9)

print(f"El promediode los números {coleccion} es {resultado}")
"""



