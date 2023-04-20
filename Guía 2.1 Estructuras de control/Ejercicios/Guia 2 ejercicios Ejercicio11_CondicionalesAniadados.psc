Algoritmo Ejercicio11_CondicionalesAniadados
	
	Escribir " El grado de eficiecia depende de dos condiciones: Que el operario produzca MENOS de 200 tornillos defectuosos y más de 1000 sin defecto. En base a ello se le otorgará un grado"
	
	Definir cant_Defectuosos, cant_SinDefectos Como Entero
	
	Escribir "Indique la cantidad de tornillos que produjo que fueron defectuosos"
	Leer cant_Defectuosos
	Escribir "Indique la cantidad de tornillos que produjo sin defectos"
	Leer cant_SinDefectos

	Si (cant_Defectuosos>200 y cant_SinDefectos<1000) Entonces
		Escribir "No cumpliste con ninguna de las condiciones, tu grado es un 5"
	SiNo
		Si (cant_Defectuosos<200 y cant_SinDefectos<1000) Entonces
			Escribir "Cumpliste sólo con la primer condición, tu grado es un 6"
		SiNo
			Si (cant_Defectuosos>200 y cant_SinDefectos>1000) Entonces
				Escribir "Cumpliste sólo con la segunda condición, tu grado es un 7"
			SiNo
				Si (cant_Defectuosos<200 y cant_SinDefectos>1000) Entonces
					Escribir "Cumpliste con las dos condiciones, tu grado es un 8"
				FinSi
			FinSi
		FinSi
		
	FinSi
	
	
FinAlgoritmo
