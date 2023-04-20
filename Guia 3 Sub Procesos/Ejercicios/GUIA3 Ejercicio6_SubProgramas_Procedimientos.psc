//Realizar un procedimiento que permita intercambiar el valor de dos variables de tipo entero. 
//La variable A, debe terminar con el valor de la variable B.


Proceso Ejercicio6SubProgramas_Procedimientos
	Definir num1, num2, inter Como Entero
	Escribir "Por favor ingrese dos numeros"
	Leer num1
	Leer num2
	po2(num1, num2,inter)
	Escribir num2 " " inter
	
FinProceso
SubProceso po2 (num1, num2 Por Valor, inter Por Referencia)
	inter<-num1
	num1<-num2
	num2<-num1
FinSubProceso
