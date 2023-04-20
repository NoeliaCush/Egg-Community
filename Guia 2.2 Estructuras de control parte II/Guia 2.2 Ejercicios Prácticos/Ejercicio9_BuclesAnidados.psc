Algoritmo Ejercicio9_BuclesAnidados
	
	Definir filas, columnas,i ,j Como Entero
	
	Escribir "Ingrese la cantidad de filas:"
	Leer filas
	Escribir "Ingrese la cantidad de columnas:"
	Leer columnas
	
	Para i<-1 Hasta filas Con Paso 1 Hacer
		Escribir sin saltar " "
		Para j<-1 Hasta columnas Con Paso 1 Hacer
			Si i=1 o j=1 o i=filas o j=columnas Entonces
				Escribir "*" Sin Saltar
			Sino 
				Escribir " " Sin Saltar
			FinSi
		Fin Para
		Escribir ""
	Fin Para
	
	
FinAlgoritmo
	