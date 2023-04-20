Algoritmo EjercicioEXTRA5_CondionalMultiple
	
	//Solicitar al usuario que ingrese un valor entre 1 y 7. EL programa debe mostrar por pantalla 
	//un mensaje que indique a qué día de la semana corresponde. Considere que el número 1 
	//corresponde al día "Lunes", y así sucesivamente.
	
	
	Definir dia Como Entero;
	Escribir "Digite un número que corresponda al día de la semana:";
	Leer dia;
	
	Segun dia Hacer
		1:
			Escribir "LUNES";
		2:
			Escribir "MARTES";
		3:
			Escribir "MIERCOLES";
		4: 
			Escribir "JUEVES";
		5: 
			Escribir "VIERNES";
		6:
			Escribir "SABADO";
		7:
			Escribir "DOMINGO";
		De Otro Modo:
			Escribir "ERROR: Valor ingresado incorrecto";
	Fin Segun
	
	
FinAlgoritmo
