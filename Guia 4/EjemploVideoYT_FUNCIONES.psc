Algoritmo EjemploVideoYT_FUNCIONES
	
	
	Definir valores, i Como Entero
	Dimension valores[5]
	
	Escribir "Ingresa 5 valores enteros"
	
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		Leer valores[i]
	Fin Para
	
	Escribir "Los valores ingresados en forma invertida son:"
	
	Para i<-4 Hasta 0 Con Paso -1 Hacer
		Si i = 0 Entonces
			Escribir valores[i]
		SiNo
			Escribir valores[i] ", " Sin Saltar
		Fin Si
	Fin Para
	
FinAlgoritmo
