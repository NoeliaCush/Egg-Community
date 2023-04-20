
Algoritmo EjemploVideoYT_MATRICES
	
	Definir M,N,i,j Como Entero
	
	Escribir "Ingrese la cardinal de M y N de la matriz original"
	Leer M, N
	
	Definir original, transpuesta Como Real
	Dimension original[M,N], transpuesta[N,M]
	
	Para i<-0 Hasta M-1 Hacer
		Para j<-0 Hasta N-1 Hacer
			Escribir "Ingrese el valor del elemento [", i, ",", j, "]" Sin Saltar
			Leer original(i,j)
		Fin Para
	Fin Para
	
	imprimeMatriz(original,M,N)
	
	Para I<-0 Hasta M-1 Hacer
		Para j<-0 Hasta N-1 Hacer
			transpuesta(j,i) = original(i,j)
			
		Fin Para
	Fin Para
	
	Escribir "Tamaño: ", (M*N), ". Matriz transpuesta:"
	imprimeMatriz(transpuesta, N,M)
	
FinAlgoritmo

SubProceso imprimeMatriz(matriz, M,N)
	Definir i,j Como Entero
	Para i<-0 Hasta M-1  Hacer
		Para j<-0 Hasta N-1  Hacer
			Escribir matriz(i,j), " " Sin Saltar
		Fin Para
		Escribir " "
	Fin Para
FinSubProceso

