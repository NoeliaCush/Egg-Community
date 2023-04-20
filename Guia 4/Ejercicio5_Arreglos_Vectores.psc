Funcion respuesta <- vectorMayor(vector Por referencia,num Por Referencia)
	Definir respuesta Como Entero
	
	Para i<-1 Hasta tamanio-1 Hacer
		Escribir "Ingrese el valor del vector", i
		Leer num
		vector[i] = num
	Fin Para
	
Fin Funcion

Algoritmo Ejercicio5_Arreglos_Vectores
	
	Definir tamanio, num,vector, i Como Entero
	
	Escribir "Ingrese el tamaño del vector"
	Leer tamanio
	Dimension vector[tamanio]
	
	Para i<-0 Hasta tamanio-1 Hacer
		Escribir "Ingrese el valor del vector", i
		Leer vector[i]
	Fin Para
	
	Escribir vectorMayor(vector,i,n)
	
	Para i<-1 Hasta tamanio-1 Hacer
		Escribir Sin Saltar "[", vector[i], "]"
	Fin Para
	
	Escribir "El valor más grande del vector es" mayor(vector, num)
	
FinAlgoritmo
