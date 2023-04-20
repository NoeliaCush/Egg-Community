//Realizar un procedimiento que permita realizar la divisi�n entre dos n�meros y muestre el 
//cociente y el resto utilizando el m�todo de restas sucesivas.
//El m�todo de divisi�n por restas sucesivas consiste en restar el dividendo con el divisor hasta 
//obtener un resultado menor que el divisor, este resultado es el residuo, y el n�mero de restas 
//realizadas es el cociente. Por ejemplo: 50 / 13:
//50 - 13 = 37 una resta realizada
//37 - 13 = 24 dos restas realizadas
//24 - 13 = 11 tres restas realizadas
//dado que 11 es menor que 13, entonces: el residuo es 11 y el cociente es 3.

SubProceso CalcularDivision(dividendo Por Referencia, divisor Por Referencia, cont Por Referencia)
	Escribir "La divisi�n entre: ", dividendo, " / ", divisor, " = ", cont
FinSubProceso

Algoritmo Ejercicio8_Subprogramas_PROCEDIMIENTOS
	
	Definir dividendo, divisor, resta Como Real;
	Definir cont Como Entero;
	Escribir "Ingrese un n�mero que sea el dividendo:"
	Leer dividendo
	Escribir "Ingrese un n�mero que sea el divisor:"
	Leer divisor
	
	cont <- 0
	resta <- dividendo
	
	Mientras resta - divisor >=0 Hacer
		resta <- resta - divisor
		Escribir (resta + divisor), " - ", divisor, " = ", resta
		cont <- cont + 1
	Fin Mientras
	
	CalcularDivision(dividendo, divisor, cont)
	
	
	
FinAlgoritmo
