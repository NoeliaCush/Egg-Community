Algoritmo EJERCICIO_05
	
	definir vector, val, i, n, n2 como entero
	
	escribir "Ingrese el tamaño deseado para el Vector."
	leer n
	
	dimension vector(n)
	
	para i <- 0 hasta n-1 Hacer
		
		escribir "Ingrese el valor para el vector ", i
		leer vector(i)
		
	FinPara
	
	escribir vectorMayor(vector, i, n)
	
FinAlgoritmo

funcion buscar <- vectorMayor(vector, i, n)
	
	definir mayor, vectorM Como Entero
	mayor = 0
	
	para i <- 0 hasta n-1
		
		si vector(i) > mayor Entonces
			
			mayor = vector(i)
			vectorM = i
			
		FinSi
		
	FinPara
	
	escribir "El mayor es el Vector(", vectorM, "). Su valor es ", mayor
	
FinFuncion
