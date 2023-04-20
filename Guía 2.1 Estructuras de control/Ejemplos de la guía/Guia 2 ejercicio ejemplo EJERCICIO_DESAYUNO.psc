Algoritmo EJERCICIO_DESAYUNO
	
	Definir desayuno Como Caracter
	Escribir "A - TÉ"
	Escribir "B - CAFÉ"
	Escribir "B1 - CAFE SOLO"
	ESCRIBIR "B2 - CAFE CORTADO"
	ESCRIBIR "B21 - CAFE CORTADO CON LECHE VEGETAL"
	
	leer desayuno
	
	Si desayuno=="A" Entonces
		Escribir "El usuario ha elegido tomar TE"
	SiNo
		Si desayuno== "B" Entonces
			Escribir "El usuario ha elegido tomar CAFÉ"
		SiNo
			Si desayuno== "B1" Entonces
				Escribir "El usuario ha elegido tomar CAFE SOLO"
			SiNo
				Si desayuno== "B2" Entonces
					Escribir "El usuario ha elegido tomar CAFE CORTADO"
				SINO 
					Si desayuno== "B21" Entonces
						Escribir "El usuario ha elegido tomar CAFE CON LECHE VEGETAL"
					FinSi
				FinSi
			FinSi
		FinSi
		
	FinSi
	
	
FinAlgoritmo
