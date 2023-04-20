Algoritmo Ejercicio9_CondicionalMultiple
	
	Definir num1, num2 Como Real
	Escribir "Indique el primer número"
	Leer num1
	Escribir "Indique el segundo número"
	Leer num2
	
	Definir operacion Como Caracter
	Escribir "Indique la operación que desee realizar"
	Escribir "S - SUMA"
	Escribir "R - RESTA"
	Escribir "M - MULTIPLICACIÓN"
	Escribir "D - DIVISION"
	Leer operacion
	
	Segun operacion Hacer
		"S":
			Escribir "Elegiste SUMA, el resultado de la operación es: " (num1+num2)
		"R":
			Escribir "Elegiste RESTA, el resultado de la operación es: " (num1-num2)
		"M":
			Escribir "Elegiste MULTIPLICACIÓN, el resultado de la operación es: " (num1*num2)
		"D":
			Escribir "Elegiste DIVISION, el resultado de la operación es: " (num1/num2)
			
		De Otro Modo:
			Escribir "ERROR: la opción que elegiste no es una de las disponibles"
	Fin Segun
	
FinAlgoritmo
