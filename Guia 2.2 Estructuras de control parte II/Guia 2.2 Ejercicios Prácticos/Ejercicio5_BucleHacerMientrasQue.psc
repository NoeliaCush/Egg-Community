Algoritmo Ejercicio5_BucleHacerMientrasQue
	
	Definir num Como Entero;
	Definir suma, max, min, promedio Como Real;
	
	suma <- 0
	
	Repetir
		Escribir "Digite un número:"
		Leer num
		suma <- suma + num
		Si num ==1 Entonces
			max = num
			min = num
		SiNo
			Si num > max Entonces
				max = num
			SiNo
				Si num < min Entonces
					min = num
				FinSi
			FinSi
		FinSi
		
	Mientras Que num <>0
	
	Escribir "El mayor número ingresado es: ", max;
	Escribir "El menor número ingresado es:", min;
	Escribir "El promedio de todos los números es:" (suma/2)
	
	
	
	
FinAlgoritmo
