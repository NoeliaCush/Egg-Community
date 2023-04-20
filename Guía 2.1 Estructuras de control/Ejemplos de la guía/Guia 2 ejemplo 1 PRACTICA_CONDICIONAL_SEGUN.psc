Algoritmo PRACTICA_CONDICIONAL_SEGUN
	
	definir eleccion como caracter 
	
	escribir "Ingrese una opción para cocinar su huevo"
	escribir "A - Frito"
	escribir "B - Hervido"
	Escribir "C - Revuelto"
	Escribir "D - Omelette"
	
	Leer eleccion
	
	Segun eleccion Hacer
		"A":
			Escribir "Su huevo se servirá FRITO"
		"B":
			Escribir "Su huevo se servirá HERVIDO"
		"C":
			Escribir "Su huevo se servirá REVUELTO"
		"D":
			Escribir "Su huevo se servirá OMELETE"
			
		De Otro Modo:
			Escribir "La opción ingresada no está entre las ofrecidas"
			
	Fin Segun
FinAlgoritmo
