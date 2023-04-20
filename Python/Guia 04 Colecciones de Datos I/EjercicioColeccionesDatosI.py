"""
Ejercicio Manos A La Obra 1)


primos = (2, 3, 5, 7, 11, 13, 17, 19, 23)

elemento_1_y_2 = primos[0:2]
print(elemento_1_y_2)

elemento_7_y_8 = primos[7:9]
print(elemento_7_y_8)

"""
"""
dias_habiles = ("lunes", "martes", "miercoles", "jueves", "viernes") 
dias_inhabiles = ("sabado", "domingo")
semana = (*dias_habiles, *dias_inhabiles)
print(semana)
"""

"""
Ejercicio Manos A La Obra 2

conocimientos = ("Python", "Javascript", "HTML", "CSS", "SQL")

lenguaje_1, lenguaje_2, lenguaje_3, lenguaje_4, lenguaje_5 = conocimientos

*_ , lenguaje_5 = conocimientos
"""

"""
Ejercicio Manos A La Obra 3

validaciones = ((False, False), (False, True), (False, False))

print(validaciones[1][1])
"""

"""
Ejercicio Manos A La Obra 4

vocales_1 = ("a", "e", "i") -> Crea para la variable vocales_1, las TUPLAS
vocales_2 = ("o", "u") -> Crea para la variable vocales_2, las TUPLAS
print(vocales_1 + vocales_2) -> SUMA las tuplas y las imprime en pantalla
print(vocales_1 * 3) -> MULTIPLICA los elementos de las TUPLAS por la cantidad (3) y los imprime en pantalla
numeros_1 = (1, 2, 2, 4, 5) -> Crea para la variable numeros_1, las TUPLAS
numeros_2 = (1, 2, 3, 4, 5) -> Crea para la variable numeros_", las TUPLAS
print(numeros_1 >= numeros_2) -> Imprime la COMPARACION entre las variables devolviendo True o False

"""

"""
Ejercicio Manos A La Obra 5

tupla_texto = ("agua", "hidrógeno", "oxígeno", "agua")-> Crea para la variable pupla_texto, las TUPLAS
print(tupla_texto.count("agua")) -> Imprime CUANTAS veces se encuentra el elemento en la tupla
print(tupla_texto.index("agua")) -> Imprime la POSICION en la que se encuentra el elemento
print(tupla_texto.index("agua", 1))
"""
"""
lista = [1, 2, 3, 4, 5, 6]

elemento_1 = lista[0]
elemento_2 = lista[1]
elemento_3_y_4 = lista[2:4]
elemento_ulimo = lista [-1]

print(elemento_1, elemento_2, elemento_3_y_4, elemento_ulimo)

lista[0] = 8
lista[2:4] = [9, 10]
lista[-1] = 12

print(lista)
"""
"""
nombres_1 = ["Agustina", "Isabel", "Lucia", "Teresa"]
nombres_2 = ["Tomas", "Santiago", "Julian"]

prueba = [nombres_1, nombres_2]
print(prueba)

nombres = [*nombres_1, *nombres_2]
print(nombres)
"""
"""
matriz = [[1, 2, 4], [2, 1, 4], [4, 2, 9]]

numero_nueve = matriz[2][2]
print(numero_nueve)

matriz = [(1, 2, 4), (2, 1, 4), (4, 2, 9)]

print(matriz)
"""
"""
mis_numeros = [1, 2, 3]
nuevo_numero = 4

print(mis_numeros + [nuevo_numero])
"""

"""
Ejercicio Mano A La Obra 6

lista_vieja = [1, 2, 3, 4] #Crea la lista
print(lista_vieja) #Imprime en pantalla la lista

lista_vieja.append(5) #La función APEEND agrega un elemento más a la lista
print(lista_vieja) #Imprime en pantalla la lista con el nuevo elemento incorporado

print("...")

lista_nueva = lista_vieja.copy() #La función COPY copia los elementos de una lista a otra
print(lista_nueva) #Imprime en pantalla la lista nueva
lista_vieja.clear() #La función CLEAR elimina los elementos de una lista
print(lista_vieja) #Imprime en pantalla la lista vieja

print("...")

mas_numeros = [4, 4, "HOLA", 6, 7] #Crea una lista nueva
# lista_nueva.append(mas_numeros) #La función APPENDS también puede anidar listas dentro de otras
lista_nueva.extend(mas_numeros) #La función EXTENDS no solo las anida sino que las agrega a la lista
print(lista_nueva) #Imprime en pantalla la nueva lista con sus nuevos valores agregados

print("...")

print(lista_nueva.count(4)) #La función COUNT cuenta la cantidad de elementos especificos que se encuentran en la lista

print("...")

print(lista_nueva.index("HOLA")) #La función INDEX retorna la POSICION en la que se encuentre un determinado elemento

print("...")

lista_nueva.insert(8, "ADIOS") #La función INSERT coloca en la posición que se indice el elemento
print(lista_nueva) #Imprime en pantalla la lista nueva

print("...")

lista_nueva.pop(0) #La función POP remueve el elemento de la posición en la que se indice
print(lista_nueva) #Imprime en pantalla la lista actualizada

print("...")

lista_nueva.remove("ADIOS") #La función REMOVE quita de la lista el VALOR del elemento
print(lista_nueva) #Imprime en pantalla la lista actualizada

print("...")

lista_nueva.reverse() #La función REVERSE muestra los elementos de la lista de atrás hacia delante
print(lista_nueva) #Imprime la lista con el nuevo orden

print("...")

lista_nueva.remove("HOLA") #Se remueve el elemento HOLA porque sino no se puede usar la función en una lista que tiene elementos STR e INT
lista_nueva.sort() #La función SORT ordena de menor a mayor los elementos de la lista
print(lista_nueva) #Imprime en pantalla la lista con el nuevo orden

vocales = ["u", "e", "i", "a"] #Se crea una lista nueva
vocales.sort() #Se utiliza la función SORT para ordenar los elementos
print(vocales) #Imprime en pantalla la lista con los elementos ordenados

"""

"""
mi_conjunto = {10, 1.2, "hola", True, False}
print(mi_conjunto)
print(type(mi_conjunto))
"""

"""
Manos A La Obra Ejercicio 7

conjunto = {0, "hola", 1, 2, True, False, "hola"} #Crea la colección
print(conjunto) #Imprime en pantalla la colección mostrando que NO se pueden repetir valores
"""

"""
Manos A La Obra Ejercicio 8

conjunto = {10, 20, 30, 40}
print(conjunto[0]) #NO se puede usar SLICING con conjunto porque el objeto SET no es suscriptible
"""

"""
Manos A La Obra Ejercicio 9

conjunto = {10, 20, 30, 40}
a, b, c, d = conjunto #Si se puede desempacar conjuntos (¿?)
print(a, b, c, d)

print(...)

tupla = (10, 20, 30, 40)
mi_tupla = (*tupla,)
print(mi_tupla)

lista = [10, 20, 30, 40]
mi_lista = [*lista]
print(mi_lista)

conjunto = {10, 20, 30, 40}
mi_conjunto = {*conjunto}
print(mi_conjunto)
"""

"""
Manos A La Obra Ejercicio 10

conjunto_1 ={(1, 2), (2, 3), (1,2)} #Crea un conjunto compuesto de TUPLAS
print(conjunto_1) #Imprime el conjunto ordenado sin repetir valores SIN errores porque el conjunto SI puede contener TUPLAS

print("...")

conjunto_2 = {[1, 2], [2, 3], [1, 2]} #Crea un conjunto compuesto de LISTAS
print(conjunto_2) #Ocurre un ERROR porque los conjuntos NO PUEDEN CONTENER LISTAS

conjunto_3 = {{1, 2}, {2, 3}, {1, 2}} #Crea un conjunto compuesto de CONJUNTOS
print(conjunto_3) #Ocurre un ERROR porque los conjuntos NO PUEDEN CONTENER CONJUNTOS
"""

"""
Manos A La Obra Ejercicio 11

conjunto_viejo = {1, 2} #Crea un conjunto
conjunto_viejo.add(3) #Utiliza la función ADD para agregar un elemento nuevo al conjunto
print(conjunto_viejo) #Imprime en pantalla el conjunto

print("...")

conjunto = conjunto_viejo.copy() #La función COPY copia los elementos de un conjunto a otro
print(conjunto) #Imprime en pantalla el conjunto
conjunto_viejo.clear() #La función CLEAR setea el conjunto eliminando todos los elementos del conjunto
print(conjunto_viejo) #Se imprime SET()

print("...")

#nuevos_elementos = (3, 4, 5) #Crea una TUPLA nueva
#nuevos_elementos = [5, 6, 7] #Crea una LISTA nueva
nuevos_elementos = {7, 8, 9} #Crea un CONJUNTO nuevo
conjunto.update(nuevos_elementos) #La función UPDATE se usa para agregar al conjunto valores de TUPLA, LISTA, CONJUNTO
print(conjunto) #Imprime en pantalla el conjunto

print("...")

conjunto.pop() #La función POP remueve el elemento de la posición en la que se indique
print(conjunto) #Imprime en pantalla el conjunto

print("...")

conjunto.remove(9) #La función REMOVE quita del CONJUNTO el VALOR del elemento
print(conjunto) #Imprime en pantalla el conjunto

print("...")

conjunto.discard(8) #La función DISCARD remueve del conjunto un elemento  SOLO si este está presente en el conjunto, a diferencia de REMOVE esta función NO produce error
print(conjunto) #Imprime en pantalla el conjunto
"""
"""
a = {1, 2} #Crea Conjunto
b = {2, 3} #Crea Conjunto

x = a.intersection(b) #La función INTERSECCIÓN muestra los elementos que se encuentran en AMBOS conjuntos
print(x) #Imprime en pantalla el resultado 
x = a & b
print(x)

print("...")

x = a.union(b) #La función UNION junta las colecciones, de valores únicos, por lo que no toma los elementos que sea iguales en ambos conjuntos
print(x) #Imprime el resultado en pantalla
x = a | b 
print(x)

print("...")

x = a.difference(b) #La función DIFFERENCE muestra los elementos que se encuentran en un conjunto que NO están en el otro
print(x) #Imprime el resultado en pantalla
x = a - b
print(x)

print("...")

x = a.symmetric_difference(b) #La función SYMMECTRIC DIFFERENCE muestra los elementos que estan en UNO U OTRO conjunto PERO NO EN AMBOS
print(x) #Imprime el resultado en pantalla
x = a ^ b
print(x)
"""

"""
1) Tuplas. A partir de la siguiente tupla:
    tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)
Imprimir por pantalla, de forma ordenada, lo siguiente:
    a) El último elemento de tupla
    b) El número de elementos de tupla (usa la función 'len')
    c) La posición donde se encuentra el elemento 87 de tupla
    d) Un elemento que esté en la posición 8 de tupla
    e) Una lista con los últimos tres ítems de tupla
    f) El número de veces que el ítem 7 aparece en tupla

tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)

print(tupla[-1]) #El ULTIMO ELEMENTO
print(len(tupla)) #El NUMERO DE ELEMENTOS
print(tupla.index(87)) #La POSICION DEL ELEMENTO
print(tupla[8]) #El elemento que ESTÁ EN LA POSICION 8
print(tupla[13:17]) #Una lista con los ULTIMOS 3 ELEMENTOS
print(tupla.count(7)) #VECES que aparece el numero 7

"""

"""
2) Listas. A partir de las siguientes listas:
    lista_1 = [1, 12, 123]
    lista_2 = ["Bye", "Ciao", "Agur", "Adieu"]
        a) Añade a la lista_1 el entero 1234 y luego la cadena "Hola"
        b) Añade a la lista_2 el string “Adios” y luego el entero 1234
        c) Genera una lista_3 con todos los elementos de la lista_1 menos el último
        d) Genera una lista_4 con todos los elementos de la lista_2 menos el primero y el último
        e) Genera una lista_5 con los elementos de la lista_4 y de la lista_3

lista_1 = [1, 12, 123]
lista_2 = ["Bye", "Ciao", "Agur", "Adieu"]

lista_1.append(1234) #Se añade el entero
lista_1.append("Hola") #Se añade la cadena
print("Lista 1: ")
print(lista_1) #Imprime la lista con el entero y la cadena incluidas

lista_2.append("Adios") #Se añade la cadena
lista_2.append(1234) #Se añade el entero
print("Lista 2: ")
print(lista_2) #Impre la lista con la cadena y el entero incluidas

lista_3 = lista_1.copy() #Copia TODOS los elementos de la lista 1
lista_3.remove("Hola") #Elimina el ULTIMO elemento de la lista 1
print("Lista 3: ") 
print(lista_3) #Imprime la lista con TODOS los elementos de la lista 1 MENOS el ULTIMO elemento

lista_4 = lista_2.copy() #Copia TODOS los elementos de la lista 2
lista_4.remove("Bye") #Elimina el PRIMER elemento de la lista 2
lista_4.remove(1234) #Elimina el ULTIMO elemento de la lista 2
print("Lista 4: ")
print(lista_4) #Imprime la lista con TODOS los elementos de la lista 2 MENOS el PRIMER y ULTIMO elemento

lista_5 = lista_4.copy() #Genera la lista copiando los elementos de la lista 4
lista_5.extend(lista_3) #La función extends agrega a la lista 5 los elementos de la lista 3
print("Lista 5: ")
print(lista_5) #Imprime la lista con los elementos de las listas 4 y 3

"""
"""
3) Conjuntos. Crear un conjunto 'usuarios' con los usuarios 'Brahms', 'Schubert', 'Vivaldi', 'Verdi' y 'Tchaikovsky'.
    Crear otro conjunto 'administradores', y poner como administrador a 'Brahms' y 'Verdi'.
    Eliminar al administrador 'Brahms' del conjunto de administradores.
    Agregar a 'Tchaikovsky' como nuevo administrador, pero no eliminarlo del conjunto de usuarios. Mostrar todos los usuarios por consola.
    Además, mostrar si cada usuario es administrador o no.

usuarios = {'Brahms', 'Schubert', 'Vivaldi', 'Verdi', 'Tchaikovsky'}
administradores = {'Brahms', 'Verdi'}
 
administradores.discard('Brahms') #Elimina del conjunto uno de los elementos
administradores.add('Tchaikovsky') #Añade al conjunto uno de los elementos
print("Usuarios: ")
print(usuarios)
mostrar = usuarios.intersection(administradores) # Muestra los elementos de un conjunto que se encuentra en otro                             
print("Usuarios que son administradores: ")
print(mostrar)
"""

"""
4) Escribir un programa que pregunte al usuario cuántas tareas quiere anotar.
    Ir agregando cada tarea que el usuario vaya ingresando a una colección.
    Mostrar por pantalla la lista de tareas en orden alfabético.

to_do = int(input("¿Cuántas tareas desea realizar hoy?"))
tareas = []

for i in range(to_do):
    tareas.append(input("¿Qué tarea querés realizar hoy?"))
    tareas.sort()

print("La lista de tareas es: " + str(tareas))
"""

"""
5) Escribir un programa que pregunte al usuario que ingrese palabras, y cada vez que ingrese una, la guarde en una lista.
La palabra será guardada en mayúsculas y en orden inverso.
Salir del programa cuando el usuario no ingrese nada.
Mostrar por pantalla la lista completa de palabras invertidas.

"""

"""
6) Crear la lista 'mis_numeros'. El usuario debe introducir enteros.
Cada vez que ingresa un número, guardarlo en una tupla anidada dentro de la lista 'mis_numeros'.
Sale de la entrada de números cuando presiona 'enter' si no hay nada ingresado.
Al terminar, mostrar por pantalla 'mis_numeros', por un lado, y por otro, los elementos desempacados de 'mis_numeros' (no aparecerán los corchetes).
Finalmente, mostrar por pantalla cada elemento desempacado de cada tupla (no aparecerán los paréntesis ni la coma).
Usar la función len().

mis_numeros = []

while True:
    numero = input("Numero: ")
    if numero:
        numero = int(numero)
        mis_numeros.append((numero,))
    else:
        break

for indice in range(len(mis_numeros)):
    print(*mis_numeros[indice])

"""

"""
7) Listas. Realizar el siguiente ejercicio, y después ver el video:
A partir de la siguiente variable:
matriz = [[1, 5, 1],
[2, 1, 2],
[3, 0, 1],
[1, 4, 4]]
Debes crear un cuarto elemento en las listas anidadas, cuyo valor deber
ser el resultado de la suma de los tres elementos actuales. El resultado
final debe ser el siguiente:
matriz = [[1, 5, 1, 7],
[2, 1, 2, 5],
[3, 0, 1, 4],
[1, 4, 4, 9]]
3
Lo debes hacer creando tres fragmentos de códigos para llegar al mismo
resultado de 3 formas:
a) Usando append() y slicing.
b) Usando append() y sum()
c) Usando el operador + y sum() pero sin usar append()

matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

#ALTERNATIVA 1
matriz[0].append(matriz[0][0] + matriz[0][1] + matriz[0][2])
matriz[1].append(matriz[1][0] + matriz[1][1] + matriz[1][2])
matriz[2].append(matriz[2][0] + matriz[2][1] + matriz[2][2])
matriz[3].append(matriz[3][0] + matriz[3][1] + matriz[3][2])

print(matriz)

#ALTERNATIVA 2
matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))

print(matriz)

#ALTERNATIVA 3

matriz[0] += [sum(matriz[0])]
matriz[1] += [sum(matriz[1])]
matriz[2] += [sum(matriz[2])]
matriz[3] += [sum(matriz[3])]

print(matriz)
"""