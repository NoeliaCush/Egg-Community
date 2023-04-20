
"""
edad = int(input("Por favor, indique su edad"))
sexo = input("Por favor, indique si usted es hombre (H) o mujer (M)")

if sexo == "H" and edad > 65 or sexo == "M" and edad > 60 :
    print("A usted le corresponde el beneficio de jubilación")
else: 
    print("A usted no le corresponde el beneficio de jubilación")
"""

""" 
a = int(input("Ingrese un número"))

while a > 10:
    print("Hola")

"""
"""
password = input("ingrese password")
password_2 = "a"
while True :
    password = input("vuelve a ingresar password")
    if password == password_2 :
        break
    else:
        continue

"""

"""
cadena = '5'

while True:
    numero = input("Adivina el numero")
    if numero == '5':
        break
    else: 
        continue

"""
"""
for numero in range(-50, -9, 5):
    print(numero)

"""

"""
1) Imprimir por pantalla los números impares del 1 al 10 al revés

for numero in range (1,10):
    if numero%2 == 1:
        print(numero)

"""

"""
2) Crear un bucle que sume los pares del 0 al 100.

numero = 1
suma = 0

while numero<=100:
    suma += numero
    if numero%2 == 0:
        print("El número " , numero, " es par")
    numero += 1

print("La suma de los números es ", suma)

"""

"""
3) Escribir un programa que requiera del usuario números, hasta que
ingrese 0. Cuando lo haga, mostrar por pantalla la suma de todos los
números ingresados.

numero = int(input("Por favor, ingrese un número"))
suma = 0

while numero != 0:
    suma += numero
    numero = int(input("Por favor, vuelva a ingresar un número"))
  
print("La suma de los números ingresados es ", suma)

"""

"""
4) Pedirle a un usuario que ingrese un número, y devolver los dígitos totales
del número. Por ejemplo, si el número es 75869, la salida debería ser 5

n = (input("Por favor, ingrese un número: "))
contador = 1

for indice, digitos in enumerate(n):
    
    contador += indice

print(contador)

"""

"""
5) Escribir un programa que lea un número impar por teclado. Si el usuario
no introduce un número impar, debe repetirse el proceso hasta que lo
introduzca correctamente.

numero = int(input("Por favor, ingrese un número"))

while True:
    numero = int(input("Por favor, ingrese un número"))
    if (numero%2 == 1):
        break
    else:
        continue

"""

"""
6) Escribir un programa que sume todos los números enteros impares
desde el 0 hasta el 100.

suma = 0

for numero in range (0 , 101):
    suma += numero
    if(numero%2 ==1):
        print("El numero ", numero, " es impar")
    numero += 1

print("La suma es ", suma)
        
"""

"""
7) Escribir un programa que permita al usuario ingresar dos años y luego
imprima todos los años en ese rango. Tienen que ser los años bisiestos.
Nota: para que un año sea bisiesto debe ser divisible por 4 y no debe ser
divisible por 100, excepto si también es divisible por 400.

anio_1 = int(input("Ingrese un año"))
anio_2 = int(input("Ingrese un año"))

for anios in range(anio_1, anio_2):
    if not anios%4 and (anios%100 or not anios%400):
        print(anios)

"""

"""
8) Se decide organizar un juego de estrategia. Se forman dos equipos de
seis integrantes cada uno. Un integrante del grupo es "el jefe". Se
comunicarán mediante un canal común: deben buscar la forma de
ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar
un método antiguo de encriptación llamado “la cifra del césar”, que
consiste en correr cada letra del mensaje –considerando la posición de
cada una en el alfabeto– una determinada cantidad de lugares. Ejemplo:
si el valor de "corrimiento" es 2, la palabra “ATAQUE” se transforma en
“CVCSWG”. Cada día, el “jefe” del equipo debe enviar un mensaje a su
grupo. Escribir un programa que permita encriptar los 5 mensajes. El
"corrimiento" (cantidad de letras que se correrán hacia la derecha) será
dado por el usuario antes de comenzar a encriptar. Los 5 mensajes
usarán el mismo "corrimiento". Nota: si el alfabeto termina antes de
poder correr la cantidad de lugares necesarios, se vuelve a comenzar
desde la letra “a”. Ejemplo: la palabra “EXTRA” corrida 3 lugares se
convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, el
siguiente cálculo matemático permite volver a comenzar por el principio
una vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27.
Solo se encriptarán las letras de los mensajes, dejando al resto de
caracteres sin modificación.

alfabeto = "abcdefghijklmnopqrstuvwxyz"
indice = 0
corrimiento = int(input("Ingrese el -corrimiento-"))
print("Por favor, ingrese 5 mensajes")
mensaje_modificado = ""
arr = []
for i in range (0,5):
    mensaje = input("Ingrese un mensaje")
    for i in range (0, len(mensaje)):
        indice = alfabeto.find(mensaje[i])
        mensaje_modificado = alfabeto[((indice + corrimiento )) % 26]
    
    arr.append(mensaje_modificado)
    mensaje_modificado =""

for i in arr:
    print(i)

"""
"""
9)Realizar el siguiente ejercicio, y después ver el video:
Escribir un programa que lea dos números por teclado y permite elegir
entre 4 opciones en un menú:
    1) Mostrar una suma de los dos números.
    2) Mostrar una resta de los dos números (el primero menos el segundo).
    3) Mostrar una multiplicación de los dos números. 4) Si elige esta opción
se interrumpirá la impresión del menú y el programa finalizará. 5) En caso
de no introducir una opción válida, el programa informará de que no es
correcta


numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

while True:
    print("1. Sumar los numeros")
    print("2. Restar los numeros")
    print("3. Multiplicar los numeros")
    print("4. Salir")
    opcion = input(" ")
    if opcion == "1":
        print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
    elif opcion == "2":
        print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
    elif opcion == "3":
        print(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")
    elif opcion == "4":
        break
    else:
        print("Opción inválida")

"""
"""
10) Realizar el siguiente ejercicio, y después ver el video:
Escribir un programa que reciba tres entradas:
- usuario: str
- password: str
- repetir_password: str
Luego debe validar que:
- La longitud de usuario sea mayor que 5
- El primer carácter de usuario no debe ser un número
- El password debe ser menor a 4 caracteres
- repetir_password debe ser igual a password



usuario = input("Ingrese el usuario: ")
password = input("Ingrese una contraseña: ")
repetir_password = input("Vuelva a ingresar la contraseña")

validacion_1 = len(usuario) > 5
validacion_2 =not usuario[0].isdigit()
validacion_3 =len(password) < 4
validacion_4 =password == repetir_password

es_formulario_valido = True

if not validacion_1:
    print("La longitud de usuairo debe ser mayor a 5")
    es_formulario_valido = False

if not validacion_2:
    print("El primer caracter de usuario NO debe ser un digito")
    es_formulario_valido = False

if not validacion_3:
    print("La longitud de la cotnraseña debe ser menor a 4")
    es_formulario_valido = False

if not validacion_4:
    print("La contraseña no es igual")
    es_formulario_valido = False

if es_formulario_valido:
    print("Formulario enviado")
else:
    print("Formulario inválido")

"""