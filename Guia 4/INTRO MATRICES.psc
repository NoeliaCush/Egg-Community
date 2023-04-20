Algoritmo Matrices
	//DEFINIMOS EL TIPO DE DATOS DE NUESTRAS VARIABLES
	Definir matriz, i, j Como Entero
	
	//DIMENSIONAMOS A NUESTRA MATRIZ
	Dimension matriz[3, 3]
	
	//Filas
	Para i<- 0 Hasta 2
		//Columnas
		Para j<-0 Hasta 2
			Escribir "INGRESE VALOR PARA FILA ", i " Y COLUMNA ", j 
			Leer matriz[i, j]
		FinPara
	FinPara
	
	Para i<- 0 Hasta 2
		Para j<-0 Hasta 2
			Escribir Sin Saltar "[",matriz[i, j],"] " 
		FinPara
		Escribir ""
	FinPara
	
FinAlgoritmo
