SubProceso calcularMedia (minima por valor ,maxima por valor, dia por valor)
	
	Escribir " La media del dia ",dia," es: ", (maxima + minima) / 2
	
FinSubProceso

Algoritmo Ejercicio7_SubProcesos_Procedimiento
	definir min,max Como Real
	definir cantidad_dias,i como entero
	
	Escribir "Introducir la cantidad de dias a medir: "
	leer cantidad_dias
	
	Para i=1 Hasta cantidad_dias Hacer
		Escribir "introducir temperatura maxima del dia ",i 
		leer max
		escribir "introducir temperatura minima del dia ",i
		leer min
		calcularMedia(min,max,i)
	FinPara
	
FinAlgoritmo
