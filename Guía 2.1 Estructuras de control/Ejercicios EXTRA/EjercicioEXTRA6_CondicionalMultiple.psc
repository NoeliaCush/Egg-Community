Algoritmo EjercicioEXTRA6_CondicionalMultiple
	
	
	//Leer tres n�meros que denoten una fecha (d�a, mes, a�o) y comprobar que sea una fecha 
	//v�lida. Si la fecha no es v�lida escribir un mensaje de error por pantalla. Si la fecha es 
	//v�lida se debe imprimir la fecha cambiando el n�mero que representa el mes por su 
	//nombre. Por ejemplo: si se introduce 1 2 2006, se deber� imprimir "1 de febrero de 2006". 
	
	
	Definir dia, mes, anio Como Entero;
	
	Escribir "Digite el d�a, mes y a�o:";
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
