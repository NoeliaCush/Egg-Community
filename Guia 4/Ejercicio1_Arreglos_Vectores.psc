
//Realizar un programa que rellene un vector con 5 valores ingresados por el usuario y los 
//muestre por pantalla

Algoritmo Ejercicio1_Arreglos_Vectores
	
	Definir vector,num, i Como Entero
	Dimension vector[5]
	
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		Escribir "Ingrese un número para el vector", i
		Leer num
		vector[i] = num 
	Fin Para
	
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		Escribir Sin Saltar "[", vector[i], "]"
	Fin Para
	
FinAlgoritmo


