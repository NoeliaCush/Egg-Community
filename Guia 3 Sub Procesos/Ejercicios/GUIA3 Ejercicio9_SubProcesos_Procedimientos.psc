Algoritmo Ejercicio9_SubProcesos_Procedimientos
	
	definir p, punto Como Caracter
	
	punto = "."
	
	escribir "Ingrese una frase, al finalizar coloque un punto"
	
	
	hacer
		
		leer p
		
		si subcadena(p,longitud(p) - 1, longitud(p)) = punto Entonces
			
			escribir "La frase codificada quedaría como: ", t(p)
			
		SiNo
			
			escribir "Coloque un punto al finalizar."
			
		FinSi
		
	mientras que subcadena(p,longitud(p) - 1, longitud(p)) <> punto
	
	
	
	
FinAlgoritmo

SubProceso codificar <- t(p)
	
	definir i como entero
	definir x como caracter
	
	para i <- 0 hasta longitud(p) Hacer
		
		x = subcadena(p,i,i)
		
		
		segun subcadena(p,i,i) Hacer
			
			"a" o "A":
				
				x = "@"
				
			"e" o "E":
				
				x = "#"
				
			"i" o "I":
				
				x = "$"
				
			"o" o "O":
				
				x = "%"
				
			"u" O "U":
				
				x = "°"
				
				
		FinSegun
		
		escribir sin saltar x
		
	FinPara
	
FinSubProceso
