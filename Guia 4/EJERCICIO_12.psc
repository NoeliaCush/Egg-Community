Algoritmo EJERCICIO_12
	
	definir palabra, matriz Como Caracter
	definir i, j, k como entero
	
	Dimension matriz(3,3)
	
	Escribir "Ingrese una palabra de hasta 9 caracteres: "
	leer palabra
	
	Si Longitud(palabra)<>9 
		Escribir "La palabra ingresa no contiene 9 caracteres, ingrese nuevamente"
		Leer palabra
	Fin Si
	
	palabra = Mayusculas(palabra)
	k=0
	
	para i <- 0 hasta 2 
		
		para j <- 0 hasta 2 
			
			
			matriz[i,j]= Subcadena(palabra,k,k)
			k=k+1
		FinPara
		
		
		
	FinPara
	
	
	Para i<-0 Hasta 2
		Para j<-0 Hasta 2
			Escribir   "[" matriz[i, j],"] " " " Sin Saltar
		FinPara
		escribir " "
	FinPara
	
	

FinAlgoritmo
