Algoritmo Ejercicio9_CondicionalMultiple
	
	Definir num1, num2 Como Real
	Escribir "Indique el primer n�mero"
	Leer num1
	Escribir "Indique el segundo n�mero"
	Leer num2
	
	Definir operacion Como Caracter
	Escribir "Indique la operaci�n que desee realizar"
	Escribir "S - SUMA"
	Escribir "R - RESTA"
	Escribir "M - MULTIPLICACI�N"
	Escribir "D - DIVISION"
	Leer operacion
	
	Segun operacion Hacer
		"S":
			Escribir "Elegiste SUMA, el resultado de la operaci�n es: " (num1+num2)
		"R":
			Escribir "Elegiste RESTA, el resultado de la operaci�n es: " (num1-num2)
		"M":
			Escribir "Elegiste MULTIPLICACI�N, el resultado de la operaci�n es: " (num1*num2)
		"D":
			Escribir "Elegiste DIVISION, el resultado de la operaci�n es: " (num1/num2)
			
		De Otro Modo:
			Escribir "ERROR: la opci�n que elegiste no es una de las disponibles"
	Fin Segun
	
FinAlgoritmo
