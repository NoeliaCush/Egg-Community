Algoritmo Ejercicio3_BucleMientras
	
	Definir suma, contador, num como entero
	Definir promedio Como Real
	
	suma=0
	contador=0
	num=0
	
	Mientras num<>-1 Hacer
		Escribir "Ingrese un número, al finalizar precione -1"
		Leer num
		Si num <>-1 Entonces
			suma= suma + num
			contador= contador +1
		FinSi
		
	Fin Mientras
	
	Escribir "La suma de los numeros ingresados es: ", suma
	Escribir "El contador de numeros ingresados es: ", contador
	
	promedio= (suma+1)/(contador-1)
	
	Escribir "promedio" promedio
	
FinAlgoritmo
