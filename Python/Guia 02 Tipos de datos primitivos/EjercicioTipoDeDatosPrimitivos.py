#Esto es un comentario

""" 1) Escribir un programa que muestre por pantalla ¡Hola Mundo! y un emoji. En los nuevos sistemas de Windows, presiona <ctrl> + <.>

print ("Hola mundo! :D")

"""

""" 2) Guardar la cadena '¡Hola Mundo!' en una variable y luego mostrar por pantalla el contenido de la variable

a = 'Hola mundo!'

print (a)

""" 

""" 3) Preguntar el nombre al usuario y después mostrar la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido

nombre = input('¿Cómo te llamas?')

print ("Hola ",nombre," !")

""" 

""" 4) Mostrar por pantalla el resultado de la siguiente operación aritmética

operacion = ( ( (8 + 2) // (2 - 5) ) ** 2 )

print(operacion)

""" 

""" 5) Preguntar al usuario cuántas horas trabaja y cuánto le pagan por hora. Mostrar el salario que le corresponde por 20 días hábiles de trabajo.
Utiliza el nombre de las variables según el estilo aconsejado

horas_trabajo = float(input('¿Cuántas horas trabaja?'))
pago_horas = float(input('¿Cuánto le pagan por hora?')) 
dias_laborales = 20

salario = horas_trabajo * pago_horas * dias_laborales

print(salario)

""" 

""" 6) Pedir al usuario su peso en kilogramos y su altura en metros. Calcular el índice de masa corporal y guardarla en una variable.
Mostrar: "Tu índice de masa corporal es <imc>" donde <imc> es el índice de masa corporal calculado.
Redondear con dos decimales usando f-string.

peso = float(input('¿Cuánto pesas?'))
altura = float(input('¿Cuánto medis?'))
imc = peso * altura

print(f"Tu índice de masa corporal es {round(imc,2)}")

"""     

""" 7) Realizar el siguiente ejercicio, y después ver el video: Dadas las siguientes expresiones: 
Crea un programa que utilice la misma cantidad de variables según la cantidad de expresiones, las cuales serán evaluadas en una nueva
variable. Mostrar por pantalla. (En la última variable utiliza los paréntesis para encerrar las expresiones, y puedes separarlas con la coma.)

expresion_1 = False == True
expresion_2 = 10 >= 2 * 4
expresion_3 = 33 / 3 == 11
expresion_4 = True > False
expresion_5 = True * 5 == 2.5 * 2

expresiones = (expresion_1, expresion_2, expresion_3, expresion_4, expresion_5)

print(expresiones)

""" 

""" 8) Realizar el siguiente ejercicio, y después ver el video relacionado: Dadas las diferentes operaciones relacionales que contienen únicamente
valores lógicos True y False:

operacion_1 = not False
operacion_2 = not 3 == 5
operacion_3 = 33 / 3 == 11 and 5 > 2
operacion_4 = True or False
operacion_5 = True * 5 == 2.5 * 2 or 123 >= 23
operacion_6 = 12 > 7 and True < False

operaciones = (operacion_1, operacion_2, operacion_3, operacion_4, operacion_5, operacion_6)

print(operaciones)

""" 

"""  9) Realizar el siguiente ejercicio, y después ver el video:
Crear una validación de datos. Un usuario introduce su nombre y edad.
Si cumple las siguientes condiciones:
    ● Nombre: tiene que ser diferente de cuatro asteriscos ****
    ● Edad: debe ser mayor que 12 y menor que 18
    ● Nombre: tiene que tener una longitud mayor o igual que 3, pero, a la vez, menor que 10
Entonces, mostrar True o False según corresponda. Debes encadenar operadores lógicos en una sola línea.

nombre = input("¿Cúal es tu nombre?")
edad = int(input("¿Cuántos años tenés?"))

validacion = nombre != "****" and edad > 12 and edad <18 and len(nombre) > 3 and len(nombre) < 10

print(validacion)

""" 
