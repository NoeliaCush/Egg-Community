
//Escribir una función recursiva que devuelva la suma de los primeros N enteros.

Funcion suma <- SumaRecursiva( n )
	
	Definir suma Como Entero
	
	Si n==1 Entonces
		suma<-n
	SiNo
		suma=n+SumaRecursiva(n-1)
	Fin Si
	
Fin Funcion

Algoritmo Ejercicio10_SubProcesos_Recursiva
	
	Definir n Como Entero
	Repetir
		Escribir "Ingrese la cantidad de números"
		Leer n
	Mientras Que n<0
	
	Escribir "La suma de ", n, " primeros números consecutivos es:", SumaRecursiva(n)
FinAlgoritmo
