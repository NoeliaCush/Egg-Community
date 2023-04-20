
//Realizar un programa que rellene un vector de tama�o N, con valores ingresados por el 
//usuario. A continuaci�n, se debe buscar un elemento dentro del arreglo (el n�mero a buscar 
//tambi�n debe ser ingresado por el usuario). El programa debe indicar la posici�n donde se 
//encuentra el valor. En caso que el n�mero se encuentre repetido dentro del arreglo se deben 
//imprimir todas las posiciones donde se encuentra ese valor. 
//Finalmente, en caso que el n�mero a buscar no est� adentro del arreglo se debe mostrar un 
//mensaje.

Algoritmo Ejercicio3_Arreglos_Vectores
	
	Definir vector, tamanio, i, num, incognita, cont, pos Como Entero
	
	
	Escribir "Ingrese el tama�o del vector"
	Leer tamanio
	
	Dimension vector[tamanio]
	
	Para i<-0 Hasta tamanio-1 Con Paso 1 Hacer
		Escribir "Ingrese el valor del vector" i
		Leer num
		vector[i]=num
	Fin Para
	
	Escribir "Ingrese el n�mero que desee buscar"
	Leer incognita
	
	cont <-0
	Para i<-0 Hasta tamanio-1 Con Paso 1 Hacer
		Si vector[i]=incognita Entonces
			pos = i
			cont<- cont +1
		Fin Si
	Fin Para
	
	Si cont =1 Entonces
		Escribir "El elemento que busca se encuentra en la posici�n:", pos
	SiNo
		Si cont >1 Entonces
			Escribir "El elemento que busca se encuentra en la posici�n", pos, "y en la posici�n" pos
		SiNo
			Escribir "El elemento que busca no se encuentra"
		FinSi
	FinSi
	
	
	
	
	
	
FinAlgoritmo
