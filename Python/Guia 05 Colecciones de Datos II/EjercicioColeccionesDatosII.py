"""
#CREAR UN DICCIONARIO:
mi_diccionario = {"sal": 10.50, "pan": 20.00, "leche": 25.25}
print(mi_diccionario)
print(type(mi_diccionario))

mi_diccionario_2 = dict(sal=20, pan=40, leche=35.25)
print(mi_diccionario_2)
print(type(mi_diccionario_2))

#INVOCAR VALORES DE UN DICCIONARIO:
mi_diccionario = {"sal": 10.50, "pan": 20.00, "leche": 25.25}
print(mi_diccionario["sal"])

#MODIFICAR UN ELEMENTO DE UN DICCIONARIO:
diccionario = {"sal": 10.50, "pan": 20.00, "leche": 25.25}
diccionario["sal"] = 110.00
print(diccionario)

#AGREGAR UN ELEMENTO A UN DICCIONARIO:
diccionario = {"sal": 10.50, "pan": 20.00, "leche": 25.25}
diccionario["vino"] = 100.00
print(diccionario)

#ELIMINAR UN ELEMENTO DE UN DICCIONARIO:
meses = {1: "enero", 2:"febrero"}

print(meses)
del meses[1]
print(meses)
"""

"""
Manos A La Obra Ejercicio 1
#DESEMPACAR DICCIONARIOS

diccionario = {"sal": 10.50, "pan": 20.00, "leche": 25.25} #Crea el diccionario
a, b, c = diccionario #Asigna valores a los elementos de la variable
print("Primer caso: ")
print(a, b, c) #Imprime en pantalla las claves hashables 

diccionario_1 = {"sal": 10.50, "pan": 20.00} #Crea el diccionario
diccionario_2 = {"leche": 25.25, "vino": 100.00} #Crea el diccionario

mi_diccionario = (*diccionario_1, *diccionario_2) # un solo * para desempacar las claves
print("Segundo caso: ")
print(mi_diccionario) #Imprime en pantalla las claves hashables de los dos diccionarios

mi_diccionario = {**diccionario_1, **diccionario_2} # dos ** para desempacar las claves y los elementos
print("Tercer caso: ")
print(mi_diccionario)# Imprime en pantalla las claves hashables junto con los elementos de cada diccionario
"""

"""
#ANIDAR EN DICCIONARIOS

#Una de las formas:
diccionario = {
    "articulos":{
        "sal": 10.50,
        "pan": 20.00,
        "leche": 25.25,
        "vino": 100.00
    },
    "proveedores":{
        1: "Sociedad La Estación",
        2: "Sociedad Buen Vino"
    },
}

#Otra de las formas
diccionario = {
    "articulos": {"sal": 10.50, "pan": 20.00, "leche": 25.25, "vino": 100.00},
    "proveedores": {1: "Sociedad La Estación", 2: "Sociedad Buen Vino"},
}

dato = diccionario["articulos"]["sal"]
print(dato)
dato = diccionario["proveedores"][1]
print(dato)
"""

"""
Manos A La Obra 2
#FUNCIONES DE DICCIONARIOS

    FUNCIÓN GET:

diccionario = {"sal": 10.50, "pan": 20.00, "leche": 25.25, "vino": 100.00} #Crea el diccionario

precio_sal = diccionario.get("sal") #La función GET permite encontrar a partir de la CLAVE el elemento del diccionario
print(precio_sal) #Imprime el resultado por pantalla
precio_sal = diccionario.get("Sal") #Si la clave está mal escrita a como aparece en el diccionario sale "NONE"
print(precio_sal) #Imprime el resultado por pantalla
precio_sal = diccionario.get("Sal", "Artículo no encontrado") #Si la clave está mal escrita y se agrega un texto, aparece el texto
print(precio_sal) #Imprime el resultado por pantalla

    #FUNCIÓN COPY:

diccionario = {"sal": 10.50, "pan": 20.00, "leche": 25.25, "vino": 100.00} #Crea el diccionario

diccionario_igual = diccionario #Otra forma de hacer lo mismo sin usar la función
diccionario_copia = diccionario.copy() #Se utiliza la función COPY para copiar un diccionario a otro

#print(diccionario) #Imprime el resultado por pantalla
#print(diccionario_igual) #Imprime el resultado por pantalla
#print(diccionario_copia) #Imprime el resultado por pantalla

    #CREAR UN DICCIONARIO DESDE LA CLASE (?):

articulos = {"fideos", "arroz"} #Crea colección
diccionario_nuevo = dict.fromkeys(articulos, 0.0) #Se inicializa con la clase DICT un diccionario con el método FROMKEYS para crear las llaves

#print(diccionario_nuevo)#Imprime el resultado por pantalla

    #FUNCIÓN KEYS Y VALUES
claves = diccionario_copia.keys() #La función KEYS permite ver las claves del diccionario
print(claves)
print(*claves) #Se imprime los elementos de las claves
valores = diccionario_copia.values() #La función VALUES permite ver los elementos del diccionario
print(valores)
print(*valores)

print("...")

    #FUNCIÓN ITEMS
clave_valores = diccionario_copia.items() #La función ITEMS muestra las claves Y los elementos del diccionario
print(clave_valores)
a, b, c, d = diccionario_copia.items()
print(*a, *b, *c, *d)

print("...")

    #FUNCIÓN UPDATE
diccionario_nuevo.update({"fideos": 3.2, "arroz": 3.4})
print(diccionario_nuevo)

elementos = {"fideos": 30.2, "arroz": 30.4, "carne": 200.4}
diccionario_nuevo.update(**elementos)
print(diccionario_nuevo)

print("...")

    #FUNCIÓN POP

diccionario_nuevo.pop("fideos")
print(diccionario_nuevo)

diccionario_nuevo.popitem()
print(diccionario_nuevo)

print("...")

    #FUNCIÓN SETDEFAULT

print(diccionario_nuevo.setdefault("arroz", 0.0))
print(diccionario_nuevo.setdefault("arrozz", 0.0))


#FUNCION JOIN 

sistemas_operativos = ("Windows", "Linux", "Mac")
cadena = ", ".join(sistemas_operativos)
print(cadena)

sistemas_operativos = ["Windows", "Linux", "Mac"]
cadena = ", ".join(sistemas_operativos)
print(cadena)

sistemas_operativos = {"Windows", "Linux", "Mac"}
cadena = ", ".join(sistemas_operativos)
print(cadena)

sistemas_operativos = {"Windows": True, "Linux": True, "Mac": True}
cadena = ", ".join(sistemas_operativos)
print(cadena)


#Función SPLIT

sistemas_operativos = "Window Linux Mac"

lista = sistemas_operativos.split()
print(lista)

sistemas_operativos = "Windows - Linux - Mac"
lista = sistemas_operativos.split(" - ")
print(lista)


#ITERACIOM SOBRE COLECCIONES DE DATOS

    #IN: DEVUELVE TRUE OR FALSE

mi_tupla = (10, 20, 30)
print(10 in mi_tupla)

mi_lista = ["rojo", "azul", "verde"]
print("blanco" in mi_lista)

mi_conjunto = {(1, 2), (2,3)}
print((1, 2) in mi_conjunto)

mi_diccionario = {"id": 1234, "nombre": "Luciano"}
print("id" in mi_diccionario)

mi_diccionario = {"id": 1234, "nombre": "Luciano"}
print("Luciano" in mi_diccionario["nombre"])


    #FOR: 

tupla = (10, 20, 30)

for elemento in tupla:
    print(elemento)

print("...")

for indice, valor in enumerate(tupla):
    print(indice, valor)

print("...")

lista = ["rojo", "azul", "verde"]

for color in lista:
    print(f"Color: {color}")

print("...")

conjunto = {(1, 2), (2, 3)}

for x in conjunto:
    multiplicacion = x[0] * 2
    cuadrado = x[1] ** 2
    print(multiplicacion, cuadrado)

diccionario = {"id": 1234, "nombre": "Luciano"}

for clave in diccionario:
    print(clave)

for clave in diccionario.keys():
    print(clave)

for valor in diccionario.values():
    print(valor)

for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")


# Conversión de tipos en colecciones

vehiculos = ["auto", "camioneta", "camion", "moto"]
capacidad = [500, 1000, 20000, 20]

diccionario = dict(zip(vehiculos, capacidad))

print(diccionario)


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = []
multiplicador = 2

for x in lista:
    resultado.append(x * multiplicador)

print(resultado)

resultado = [x * multiplicador for x in lista]

print(resultado)


personas = [("Roxana", 36), ("Horacio", 5), ("Gabriel", 41)]
personas_mayores = [p for p in personas if p[1] >=18]
print(personas_mayores)
"""

"""
1) Escribir un programa que almacene en una lista los números del 1 al 10 y
los muestre por pantalla en orden inverso.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1,11):
    print(numeros[-i])
"""

"""
2) Escribir un programa que enumere los países de la siguiente lista:
["Canada", "USA", "Mexico", "Australia", "Argentina", "China", "India"]

paises = ["Canada", "USA", "Mexico", "Australia", "Argentina", "China", "India"]

for i, pais in enumerate(paises, start = 1):
    print(f"{i}: {pais}")
"""

"""
3) Pedirle a un usuario que ingrese un número, y devolver los dígitos totales
del número. Por ejemplo, si el número es 75869, la salida debería ser 5

numero = (input("Por favor, ingrese un número: "))

contador = len(numero)

print(f"El número {numero} tiene un total de {contador} digitos")
"""

"""
4)Escribir un programa que pida al usuario un número entero del 0 al 9
dentro de un bucle. Comprobar si el número se encuentra en la lista de
números válidos y notificarlo:
numeros_validos = [1, 3, 6, 9]

numero = int(input("Por favor, introduzca un número del 0 al 9: "))
numeros_validos = [1, 3, 6, 9]

while numero >= 0 & numero <= 9:
    numero = int(input("Por favor, introduzca un número del 0 al 9: "))
    if numero in numeros_validos:
        print(f"El número {numero} se encuentra dentro de los números válidos")
        break
"""

"""
5) Crear una lista de países en letras minúsculas. Luego, por medio de la
comprensión de listas, crear una nueva lista con las mismas cadenas,
cuya primera letra sea en mayúsculas.

paises = ["argentina", "chile", "uruguay", "brasil"]

cap_paises = [pais.capitalize() for pais in paises]

print(cap_paises)
"""

"""
6) Realizar el siguiente ejercicio, y después ver el video:
Dadas dos listas, debes generar una tercera con todos los elementos
que se repitan en ellas, pero no debe repetirse ningún elemento en la
nueva lista.

lista_1 = ["h", "o", "r", "o", " ", "s", "o", "l", "a"]
lista_2 = ["h", "o", "l", "a", " ", "l", "u", "n", "a"]

interseccion = set(lista_1) & set(lista_2)

lista_3 = list(interseccion)

print(lista_3)
"""
"""
7) Programar las siguientes instrucciones de forma ordenada. Inicialmente,
el diccionario es: animales = {"elefante": ""}
    a) Añadir al diccionario las claves: "perro", "tigre" y "mono", con sus
respectivos valores: "Bobby", "Peepe” y "Homero"
    b) Modificar las claves: "elefante" y "delfín" con los valores: "Trompis"
y "Manolo" respectivamente.

animales = {"elefante": ""}

animales.update({"perro": "Bobby", "tigre": "Peepe", "mono": "Homero"})

print(f"Punto A) Diccionario: {animales}")

animales["elefante"] = "Trompis"
animales["delfín"] = "Manolo"
print(f"Punto B) Diccionario: {animales}")
"""

"""
8) A partir del siguiente diccionario:
{"Euro": "€", "Dólar": "$", "Yen": "¥"}
Preguntar al usuario por una moneda, y luego mostrar su símbolo, o un
mensaje si la moda no está en el diccionario

monedas = {"Euro": "€", "Dólar": "$", "Yen": "¥"}

moneda = str(input("Ingrese una divisa (Euro/ Dólar/ Yen):")).title()

monedas_claves = monedas.keys()

if moneda in monedas_claves:
    print(monedas[moneda])
else:
    print("La moneda ingresada no se encuentra")
"""

"""
9) Pregunta al usuario por su nombre, edad, dirección y teléfono. Guardar
los datos en un diccionario. Mostrar por pantalla: <nombre> tiene
<edad> años, vive en <dirección> y su número de teléfono es
<teléfono>

persona = {}

nombre = str(input("¿Cómo te llamás?: "))
edad = str(input("¿Cuántos años tenés?: "))
direccion = str(input("¿Cuál es tu dirección?: "))
telefono = str(input("¿Cuál es tu número de teléfono?: "))

persona.update({
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
})

print(f"{nombre} tiene {edad} años, vive en {direccion} y su numero de teléfono es {telefono}")
"""

"""
10) Crear un diccionario con la siguiente estructura:
{
"artículo": {
int: {"nombre": str, "precio": float, "stock": int},
}
}
El programa permitirá cargar artículos. La clave <int> del diccionario
anidado, corresponde al código de un artículo. Cada vez que se añada
un nuevo dato, debe imprimirse el contenido del diccionario.
Crear varios artículos y simular una venta. Informar si no hay stock y el
precio final de la compra.

from pprint import pprint

articulos = { "artículo": {}}

while True:
    respuesta = input("¿Quiere agregar un artículo? s/n: ").lower()
    if respuesta == "n":
        break
    elif respuesta == "s":
        codigo = int(input("Código: "))
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        datos = {"nombre": nombre, "precio": precio, "stock": stock}
        articulos["artículo"][codigo] = datos
        pprint(articulos)


compra = {"articulo": [], "total": 0}

while True:
    respuesta = input("¿Compra? s/n:").lower()
    if respuesta == "s":
        codigo = int(input("¿Qué desea? Ingresa el código: "))
        if codigo not in articulos["artículo"]:
            input("El código no existe")
            pprint(articulos)
        else:
            nombre = articulos["artículo"][codigo]["nombre"]
            precio = articulos["artículo"][codigo]["precio"]
            stock = articulos["artículo"][codigo]["stock"]
            if stock > 0:
                cantidad = int(input(f"¿Cuánto lleva? (máximo {stock}): "))
                articulos["artículo"][codigo]["stock"] -= cantidad
                compra["artículo"].append({"nombre": nombre, "precio": precio})
                compra["total"] += precio * cantidad
                print("SU COMPRA:")
                pprint(compra)
            else:
                input("No hay suficiente stock.")
                pprint(articulos)
    elif respuesta == "n":
        print("SU COMPRA:")
        pprint(compra)
        break
"""