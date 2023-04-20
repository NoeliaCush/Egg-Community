Algoritmo EjercicioEXTRA7_CondicionalMultiple
	
	//Hacer un algoritmo que lea un número por el teclado y determine si tiene tres dígitos.
	
	Definir num Como Cadena;
	
	Escribir "Digite un número";
	Leer num
	
	//Escribir "La longitud del número es: ", longitud(num);
	
	Segun longitud(num) Hacer
		3:
			Escribir "El número ingresado tiene 3 digitos";
		De Otro Modo:
			Escribir "El número ingresado no contine 3 digitos";
	Fin Segun
	
FinAlgoritmo
