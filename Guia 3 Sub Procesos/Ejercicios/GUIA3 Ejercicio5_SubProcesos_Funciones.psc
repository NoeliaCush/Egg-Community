
//Realizar una funci�n que reciba un numero ingresado por el usuario y averig�e si el n�mero es
//primo o no. Un n�mero es primo cuando es divisible s�lo por 1 y por s� mismo, por ejemplo: 2, 
//3, 5, 7, 11, 13, 17, etc. Nota: recordar el uso del MOD.

Funcion Resultado <-primo(num Por Valor)
	
	Definir i, contador Como Entero;
	contador=0;

	Para i<-1 Hasta num Con Paso 1 Hacer
		Si num MOD i= 0 Entonces
			contador = contador +1
		FinSi
	Fin Para
	
	Si contador=2 Entonces
		Escribir num, " Es un n�mero primo"
	SiNo
		Escribir num, " No es un n�mero primo"
	FinSi
	
Fin Funcion

Algoritmo Ejercicio5SubProcesos_Funciones
	
	Definir num Como Entero;
	
	Escribir "Ingrese un n�mero:"
	Leer num;
	
	Escribir "�El n�mero ", num , " es primo?" primo(num)
	
FinAlgoritmo
