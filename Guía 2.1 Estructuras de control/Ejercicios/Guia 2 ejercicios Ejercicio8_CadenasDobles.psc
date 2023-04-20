Algoritmo Ejercicio8_CondicionalDoble
	
	Definir cade, cade1, cade2 Como Caracter
	
	Escribir "Indique su palabra"
	Leer cade
	
	cade1= Subcadena(cade,0,0)
	cade2= Subcadena(cade,Longitud(cade)-1, Longitud(cade))
	
	Si cade1=cade2 Entonces
		Escribir "CORRECTO"
	SiNo
		Escribir "INCORRECTO"
	FinSi
	
FinAlgoritmo