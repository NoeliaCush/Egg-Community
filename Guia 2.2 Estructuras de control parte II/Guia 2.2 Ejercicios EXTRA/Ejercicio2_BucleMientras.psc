
//Escriba un programa que solicite dos n�meros enteros (m�nimo y m�ximo). 
//A continuaci�n,se debe pedir al usuario que ingrese n�meros enteros situados
//entre el m�ximo y m�nimo.Cada vez que un n�mero se encuentre entre ese intervalo,
//se sumara uno a una variable.El programa terminar� cuando
//se escriba un n�mero que no pertenezca a ese intervalo, y 
//al finalizar se debe mostrar por pantalla la cantidad 
//de n�meros ingresados dentro del intervalo.

Algoritmo Ejercicio2_BucleMientras
	
	Definir min, max, num, contador Como Entero
	min = 2
	max = 20
	contador = 1
	
	Escribir "Ingrese un n�mero:"
	Leer num
	
	Mientras (num >min Y num<max) Hacer
		Escribir "Ingrese un n�mero:"
		Leer num
		contador = contador + 1
	Fin Mientras
	
	Escribir"La cantidad de n�meros ingresados fue: ", contador
	
FinAlgoritmo
