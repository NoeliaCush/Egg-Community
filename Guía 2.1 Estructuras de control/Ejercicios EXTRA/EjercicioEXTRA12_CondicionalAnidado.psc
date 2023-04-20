//Una empresa tiene personal de distintas áreas con distintas condiciones de contratación y 
//formas de pago. El departamento de contabilidad necesita calcular los sueldos semanales 
//(lunes a viernes) en base a las 3 modalidades de sueldo: 
//a) comisión
//b) salario fijo + comisión, y
//c) salario fijo
//a) Para la modalidad salario por comisión se debe ingresar el monto total de las ventas 
//realizadas en la semana, y el 40% de ese monto total corresponde al salario del 
//empleado.
//b) Para la condición de salario fijo + comisión, se debe ingresar el valor que se paga por 
//hora, la cantidad de horas trabajadas semanalmente y el monto total de las ventas en 
//esa semana. En este tipo de contrato las horas extras no están contempladas y se fija 
//como máximo 40 horas por semana. La comisión por las ventas se calcula como 25% 
//del valor de venta total.
//c) Finalmente, para la modalidad de salario fijo se debe ingresar el valor que se paga por 
//hora y la cantidad de horas trabajadas en la semana. En el caso de exceder las 40 
//horas semanales, las horas extras se deben pagar con un extra del 50% del valor de la 
//hora. Realizar un menú de opciones para poder elegir el tipo de contrato que tiene un 
//empleado.

Algoritmo EjercicioEXTRA_CondicionalesAnidados
	
	Definir modalidad Como Entero;
	Definir total_ventas, valor_hora, cant_hs, comision, hs_extra Como Real;
	
	total_ventas <- 0;
	valor_hora <- 0;
	cant_hs <- 0;
	comision <- 0;
	
	Escribir "Digite la modalidad de sueldo que desea calcular:";
	Escribir " 1 - Comisión";
	Escribir " 2 - Salario fijo + comisión";
	Escribir " 3 - Salario fijo";
	Leer modalidad
	
	Segun modalidad Hacer
		1:
			Escribir "Ingrese el monto total de las ventas realizadas en la semana";
			Leer total_ventas
			comision <- total_ventas*0.4;
			Escribir "El sueldo semanal para esta modalidad es: ", comision;
		2:
			Escribir "Ingrese el valor que se paga por hora:";
			Leer valor_hora;
			Escribir "Ingrese la cantidad de horas que se trabajaron en la semana:";
			Leer cant_hs;
			Si cant_hs<=40 Entonces
				total_ventas <- valor_hora*cant_hs;
			SiNo
				Escribir "La cantidad de horas superan las fijadas para esta modalidad";
			Fin Si
			Escribir "El monto total de las ventas en la semana fue:" total_ventas;
			comision <- total_ventas*0.25
			Escribir "El sueldo semanal para esta modalidad es:", (total_ventas + comision);
		3:
			Escribir "Ingrese el valor que se paga por hora:";
			Leer valor_hora;
			Escribir "Ingrese la cantidad de horas que se trabajaron en la semana:";
			Leer cant_hs;
			Si cant_hs>40 Entonces
				hs_extra <- valor_hora*0.5
				total_ventas <- (valor_hora*cant_hs)+hs_extra;
			SiNo
				total_ventas <- valor_hora*cant_hs;
			Fin Si
			Escribir "El sueldo semanal para esta modalidad es:", total_ventas;
		
		De Otro Modo:
			Escribir "La opción ingresada no es válida";
	Fin Segun
	
FinAlgoritmo
