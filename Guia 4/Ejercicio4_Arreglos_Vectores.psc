Algoritmo Ejercicio4_Vectores
	
	Definir num, i Como Entero
	Definir menu, mostrarmenu Como Caracter
	
	Escribir "Ingrese un valor para el vector"
	Leer num
	
	Dimension A[num], B[num], C[num]
	Definir A, B, C Como Entero
	
	Definir true Como Logico
	true = Verdadero
	Mientras true Hacer
		Escribir "Ingresar al menu"
		Escribir "A. LLenar vector A de forma ALEATORIA"
		Escribir "B. LLenar vector B de forma ALEATORIA"
		Escribir "C. Llenar vector C con la SUMA de los vectores A y B"
		Escribir "D. LLenar vector C con la RESTA de los vectores A y B"
		Escribir "E. Mostrar los vectores A,B o C"
		Escribir "F. Salir"
		Leer menu
		Segun menu Hacer
			"A" o "a":
				Para i<-0 Hasta num-1 Hacer
					A[i] = Aleatorio(-100,100)
				Fin Para
			"B" o "b":
				Para i<-0 Hasta num-1 Hacer
					B[i] = Aleatorio(-100,100)
				Fin Para
			"C" o "c":
				Para i<-0 Hasta num-1 Hacer
					C[i] = A[i] - B[i]
				Fin Para
			"D" o "d":
				Para i<-0 Hasta num-1 Hacer
					C[i] = B[i] - A[i]
				Fin Para
			"E" o "e":
				Escribir "Mostrar vector A, B o C"
				Leer mostrarmenu
				Segun mostrarmenu Hacer
					"A" o "a":
						Escribir "Mostrar vector A"
						Para i<-0 Hasta num-1 Hacer
							Escribir Sin Saltar "espacio", i+1, ":", A[i]
						Fin Para
					"B" o "b":
						Escribir "Mostrar vector B"
						Para i<-0 Hasta num-1 Hacer
							Escribir Sin Saltar "espacio", i+1, ":", B[i]
						Fin Para
					"C" o "c":
						Escribir "Mostrar vector C"
						Para i<-0 Hasta num-1 Hacer
							Escribir Sin Saltar "espacio", i+1, ":", C[i]
						Fin Para
				Fin Segun
				Escribir ""
			"F" o "f":
				Escribir "Salir del menu"
				true = Falso
		Fin Segun
	Fin Mientras
	
FinAlgoritmo
