
//Realizar una funci�n que valide si un n�mero es impar o no. Si es impar la funci�n debe 
//devolver un verdadero, si no es impar debe devolver falso. Nota: la funci�n no debe tener 
//mensajes que digan si es par o no, eso debe pasar en el Algoritmo.

Funcion respuesta <- operacion(num)
	Definir respuesta Como Logico
	
	respuesta <- num MOD 2 <>0
	
Fin Funcion


Algoritmo Ejercicio2SubProgramas_Funciones
	
	Definir num Como Entero;
	
	Escribir "Digite un n�mero: ";
	Leer num;	
	
	Si num MOD 2 <>0 Entonces
		Escribir "�El n�mero ", num, " es impar?" operacion(num);
	SiNo
		Escribir "�El n�mero ", num, " es impar?" operacion(num);
	Fin Si
	
	
	
FinAlgoritmo
