"""
Manos A La Obra - Ejercicio 1
    Realizado desde el intérprete de Python
"""
"""
Manos A La Obra - Ejercicio 2
"""

"""
ANOTACIONES DE TIPO

En Tipo de datos primitivos 

a: int = 1000
b: float = 10.99
c: complex = 10j
d: str = "Python"
e: bool = True

dni: str
dni = (input("Ingresa tu DNI: ")) #problema: int no se puede asignar a una variable de tipo str
print(dni)

En colecciones

tupla: tuple[int, int, int] #De forma EXPLICITAse indica que tuple guarda INT
tupla = (1, 2, 3)

lista: list = [10.2, 20.34, 30.43]
conjunto: set = {"Argentina", "Brasil", "Chile"}
diccionario: dict = {"nombre": "Pepone"}

#Esto: lista.append("soy una cadena") ERROR los datos de la lista son FLOAT

print(type(...))

#Para que la tupla sea de un tamaño VARIABLE se usa tuple[int, ...]
tupla: tuple[int, ...]
tupla = (1, 2, 3)
tupla = (1, 2, 3, 4)

#Para las LISTAS solo se anota el tipo de dato
lista: list[float]
lista = [10.2, 20.34, 30.43]
lista.append("12") #dará error porque es de tipo str y requiere float

#Para CONJUNTOS solo se anota el tipo de dato
conjunto: set[str]
conjunto = {"Argentina", "Brasil", "Chile"}
conjunto.add(1000) #dará error es de tipo int y requiere str

#Para DICCIONARIOS se debe especificar el tipo de dato de la CLAVE y el VALOR
diccionario: dict[str, str]
diccionario = {"nombre": "Pepone"}
diccionario["apellido"] = 1234 #Dará error prque es int y requiere str

#En EXPRESIONES ANIDADAS
articulos: dict[int, list[str]] = {}
articulos[1] = ["madera", "clavos"]
articulos["2"] = "martillo" #Dará error porque la clave es str y requiere int

#Para listas de VARIOS TIPOS DE DATOS
cosas: list[int | str]
cosas = [1, "algo"]
cosas = [1, "algo", ["Argentina", "Brasil"]] #Dará error porque no se declaró como valor list[str]
"""

"""
Manos A La Obra - Ejercicio 5

cosas: list[int | str | str ]
cosas = [1, "algo","Argentina, Brasil"]
print(cosas)
"""

"""
Paraa funciones las ANOTACIONES tienen esta estructura

def nombre_funcion(parametro: <tipo>, ...) -> <tipo>: return <objeto>
"""

"""
Manos A La Obra - Ejercicio 6

Paso 1. Escribir el código
Paso 2. Borrar el fragmento "upper()", no ocurre nada no hay sugerencias
Paso 3. Agregar las anotaciones de tipo
Paso 4. Borrar el fragmento "upper()", se abre el menú porque reconoce el tipo de dato de nombre (Str)

def usuario(nombre:str, actividad:bool) -> str:
    mensaje: str = f"{nombre.upper()}: {actividad}"
    return mensaje

situacion = usuario("administrador", True)
print(situacion)
"""

"""
Manos A La Obra - Ejercicio 07
Paso 1. Agregar la anotación de tipo de dato para la devolución
Paso 2. Corrige el siguiente código para que solamente imprima una línea, y no dos,
como hace (sin tocar el cuerpo de la función)
Paso 3. Una forma de indicar que un tipo de datos es opcional
Paso 4. Invoca la función con un único y solo argumento

from typing import Optional

def usuario(nombre: str, actividad: Optional[bool] = None) -> str:
    return f"{nombre.upper()}: {actividad}"

print(usuario("administrador"))
"""

"""MANEJO DE EXCEPCIONES

try:
    print(10 / "numero")
except:
    pass 
    print("Ocurrió un error")

try:
    #print(10 / "0")
    print(10 / 0)
    #print(variable_no_definida)
except TypeError:
    print("Error, un operando no permite la división")
except ZeroDivisionError:
    raise ZeroDivisionError("Error, división por cero")
except NameError:
    print("Error, variable no definida")
except Exception as error:
    print(f"Error, {error}")


try:
    a = int(input("a: "))
    b = int(input("b: "))
    division = a / b
except TypeError:
    print("Error, un operando no permite la división")
except ZeroDivisionError:
    print("Error, división por cero")
except NameError:
    print("Error, variable no definida")
except Exception as error:
    print(f"{type(error).__name__}: {error}")
else:
    print(f"El resultado de la división es {division}")
finally:
    print("Salida")
"""
"""
Manos A La Obra - Ejercicio 8

try:
    lista = [2, 4, 6, 8, 10]
    lista[10]
except Exception as error:
    print(f"{type(error).__name__}: {error}")
"""

"""Manos A La Obra - Ejercicio 9

try:
    colores = {"blanco": "white", "verde": "green", "negro": "black"}
    colores["amarillo"]
except Exception as error:
    print(f"{type(error).__name__}: {error}")
"""

"""Manos A La Obra - Ejercicio 10
Crea una función que reciba como parámetro una lista y un elemento
cualquiera (Any). La función debe agregar el "elemento" al final de la "lista". Si
el elemento existe en la lista, debes lanzar un error de tipo ValueError y mostrar
este mensaje en su lugar:
Error: No puedes agregar el elemento [elemento] porque ya existe en la lista.
"""

"""ASERSION

assert 1 == 1
assert 1 == 2
assert int == type(3)
assert int == type(3.0)
"""

"""Manos A La Obra - Ejercicio 11"""


    
