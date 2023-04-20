
//Realizar un programa que lea 10 números reales por teclado, los almacene en un arreglo y 
//muestre por pantalla la suma, resta y multiplicación de todos los números ingresados al 
//arreglo.

Algoritmo Ejercicio2_Vectores
	
	Definir vector, i, num, suma, resta, multiplicacion Como Real
	Dimension vector[10]
	
	suma <- 0;
	resta <- 0;
	multiplicacion <- 1;
	
	//Para pasar por los elementos de dimensión del vector 
	Para i<-0 Hasta 9 Con Paso 1 Hacer
		Escribir "Digite un número para el vector" i
		Leer num
		vector[i] = num
		suma <- suma + vector[i]
		resta <- resta - vector[i]
		multiplicacion<- multiplicacion * vector[i]
	Fin Para
	
	//Para mostrar los elementos del vector
	Para i<-0 Hasta 9 Con Paso 1 Hacer
		Escribir Sin Saltar "[" vector[i] "]"
	Fin Para
	
	Escribir "La suma de todos los números es:", suma
	Escribir "La resta de todos los números es:", resta
	Escribir "La multiplicación de todos los números es:", multiplicacion
	
	
FinAlgoritmo
