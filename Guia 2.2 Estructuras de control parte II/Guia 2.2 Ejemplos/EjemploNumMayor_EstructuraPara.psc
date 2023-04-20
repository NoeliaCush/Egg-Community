Algoritmo EjemploNumMayor_EstructuraPara
	
	Definir a, b, num Como Entero
	b=0
	
	Para a<-0 Hasta 10 Con Paso 2 Hacer
		Escribir "Ingrese un numero"
		Leer num
		
		Si num>b Entonces
			b=num
		FinSi
	Fin Para
	
	Escribir "El numero mayor ingresado es: ", num
	
FinAlgoritmo
