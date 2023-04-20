// Crear una matriz que contenga 3 columnas y la cantidad filas que decida el usuario. Las dos
// primeras columnas contendrán valores enteros ingresados por el usuario y en la 3 columna se
// deberá almacenar el resultado de sumar el número de la primera y segunda columna. Mostrar
// la matriz de la siguiente forma:

//	3 + 5 = 8
//	4 + 3 = 7
//	1 + 4 = 5


Algoritmo guia_4_extra_13
	
	Definir matriz, filas,i,j Como Entero
	
	
	Escribir "Ingrese el número de filas de la matriz"
	leer filas
	
	Dimension matriz[filas,3]
	
	
	
	Para i=0 hasta filas-1
		Para j=0 hasta 1
			
			Escribir "ingrese el valor de la fila ", i, " y columna ",j
			leer matriz[i,j]
			
			
			
		FinPara
		
		matriz[i,2] = matriz[i,0] + matriz[i,1]
		
	FinPara
	
	
	Para i= 0 Hasta filas-1
		
		Escribir matriz[i, 0], " + ", matriz[i, 1], " = ", matriz[i, 2] 
		
		
		
	FinPara



	
	
FinAlgoritmo
