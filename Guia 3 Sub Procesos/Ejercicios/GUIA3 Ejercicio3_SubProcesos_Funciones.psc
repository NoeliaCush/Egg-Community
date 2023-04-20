
//Crea una función EsMultiplo que reciba los dos números pasados por el usuario, validando 
//que el primer número múltiplo del segundo y devuelva verdadero si el primer número es 
//múltiplo del segundo, sino es múltiplo que devuelva falso.

Funcion EsMultiplo <- operacion(num1 Por Referencia, num2 Por Referencia)
	
	Definir EsMultiplo Como Logico;
	
	EsMultiplo <- num1 Mod num2 == 0
	
Fin Funcion

Algoritmo Ejercicio3SubProcesos_Funciones
	
	Definir num1, num2 Como Entero;
	
	Escribir "Ingrese el primer número:";
	Leer num1;
	Escribir "Ingrese el segundo número:";
	Leer num2;
	
	Escribir "¿El número ", num1, " es múltiplo de el número ", num2 , " ?"  operacion(num1, num2)
	
FinAlgoritmo
