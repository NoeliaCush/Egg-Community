
//Crea una funci�n EsMultiplo que reciba los dos n�meros pasados por el usuario, validando 
//que el primer n�mero m�ltiplo del segundo y devuelva verdadero si el primer n�mero es 
//m�ltiplo del segundo, sino es m�ltiplo que devuelva falso.

Funcion EsMultiplo <- operacion(num1 Por Referencia, num2 Por Referencia)
	
	Definir EsMultiplo Como Logico;
	
	EsMultiplo <- num1 Mod num2 == 0
	
Fin Funcion

Algoritmo Ejercicio3SubProcesos_Funciones
	
	Definir num1, num2 Como Entero;
	
	Escribir "Ingrese el primer n�mero:";
	Leer num1;
	Escribir "Ingrese el segundo n�mero:";
	Leer num2;
	
	Escribir "�El n�mero ", num1, " es m�ltiplo de el n�mero ", num2 , " ?"  operacion(num1, num2)
	
FinAlgoritmo
