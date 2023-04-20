Algoritmo EjercicioEXTRA6_CondicionalMultiple
	
	
	//Leer tres números que denoten una fecha (día, mes, año) y comprobar que sea una fecha 
	//válida. Si la fecha no es válida escribir un mensaje de error por pantalla. Si la fecha es 
	//válida se debe imprimir la fecha cambiando el número que representa el mes por su 
	//nombre. Por ejemplo: si se introduce 1 2 2006, se deberá imprimir "1 de febrero de 2006". 
	
	
	Definir dia, mes, anio Como Entero;
	
	Escribir "Digite el día, mes y año:";
	Leer dia;
	Leer mes;
	Leer anio;
	
	Segun mes Hacer
		1:
			Escribir dia, " de ENERO de ", anio;
		2:
			Escribir dia, " de FEBRERO de ", anio;
		3:
			Escribir dia, " de MARZO de ", anio;
		4:
			Escribir dia, " de ABRIL de ", anio;
		5:
			Escribir dia, " de MAYO  de ", anio;
		6:
			Escribir dia, " de JUNIO de ", anio;
		7:
			Escribir dia, " de JULIO de ", anio;
		8:
			Escribir dia, " de AGOSTO de ", anio;
		9:
			Escribir dia, " de SEPTIEMBRE de ", anio;
		10:
			Escribir dia, " de OCTUBRE de ", anio;
		11:
			Escribir dia " de NOVIEMBRE de ", anio;
		12:
			Escribir dia, " de DICIEMBRE de ", anio;
		De Otro Modo:
			Escribir "ERROR";
	Fin Segun
	
	
FinAlgoritmo
