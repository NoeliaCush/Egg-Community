
//Realizar una funci�n que calcule la suma de dos n�meros. En el algoritmo principal le 
//pediremos al usuario los dos n�meros para pas�rselos a la funci�n. Despu�s la funci�n 
//calcular� la suma y lo devolver� para imprimirlo en el algoritmo.

Funcion suma <- operacion( num1 Por Referencia, num2 Por Referencia )
	
	Definir suma Como Real;
	
	suma = num1+num2;
	
Fin Funcion

Algoritmo Ejercicio1_SubProgramas_Funciones
	
	Definir num1, num2 Como Real;
	
	Escribir "Ingrese el primer n�mero: ";
	Leer num1;
	Escribir "Ingrese el segundo n�mero: ";
	Leer num2;
	
	Escribir "La suma entre los n�meros ingresados es igual a: " operacion(num1,num2)
	
FinAlgoritmo
