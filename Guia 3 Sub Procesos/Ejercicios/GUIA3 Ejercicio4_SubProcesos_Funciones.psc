
//Realizar un programa que pida al usuario una frase y una letra a buscar en esa frase. La 
//función debe devolver la cantidad de veces que encontró la letra. Nota: recordar el uso de la 
//función Subcadena()

Funcion contadorletra <- cuentaletras ( frase Por Referencia,letra Por Referencia )
	definir contadorletra ,i como entero
	contadorletra=0
	para i <- 0 Hasta Longitud(frase) Con Paso 1 Hacer
		si letra= SubCadena(frase,i,i) Entonces
			contadorletra= contadorletra +1
		FinSi
	FinPara
	
Fin Funcion

algoritmo Ejercicio4SubProcesos_Funciones
	
	definir frase,letra Como Caracter
	Escribir "ingresa una frase y una letra "
	leer frase,letra
	escribir"la cantidad de veces que la letra se repitio fue: " cuentaletras(frase,letra)
	
FinAlgoritmo

