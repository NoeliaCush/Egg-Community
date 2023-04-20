
//Realizar una función que reciba un numero ingresado por el usuario y averigüe si el número es
//primo o no. Un número es primo cuando es divisible sólo por 1 y por sí mismo, por ejemplo: 2, 
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
		Escribir num, " Es un número primo"
	SiNo
		Escribir num, " No es un número primo"
	FinSi
	
Fin Funcion

Algoritmo Ejercicio5SubProcesos_Funciones
	
	Definir num Como Entero;
	
	Escribir "Ingrese un número:"
	Leer num;
	
	Escribir "¿El número ", num , " es primo?" primo(num)
	
FinAlgoritmo
