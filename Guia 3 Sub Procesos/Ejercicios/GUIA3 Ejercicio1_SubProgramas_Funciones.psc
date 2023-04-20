
//Realizar una función que calcule la suma de dos números. En el algoritmo principal le 
//pediremos al usuario los dos números para pasárselos a la función. Después la función 
//calculará la suma y lo devolverá para imprimirlo en el algoritmo.

Funcion suma <- operacion( num1 Por Referencia, num2 Por Referencia )
	
	Definir suma Como Real;
	
	suma = num1+num2;
	
Fin Funcion

Algoritmo Ejercicio1_SubProgramas_Funciones
	
	Definir num1, num2 Como Real;
	
	Escribir "Ingrese el primer número: ";
	Leer num1;
	Escribir "Ingrese el segundo número: ";
	Leer num2;
	
	Escribir "La suma entre los números ingresados es igual a: " operacion(num1,num2)
	
FinAlgoritmo
