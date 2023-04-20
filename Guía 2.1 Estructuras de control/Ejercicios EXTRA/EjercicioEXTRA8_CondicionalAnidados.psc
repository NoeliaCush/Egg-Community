Algoritmo EjercicioEXTRA8_CondicionalAnidados
	
	//Si se compran menos de cinco llantas el precio es de $3000 cada una, si se compran 
	//entre 5 y 10 el precio es de $2500, y si se compran más de 10 el precio es $2000. 
	//Obtener la cantidad de dinero que una persona tiene que pagar por cada una de las 
	//llantas que compra, y el monto total que tiene que pagar por el total de la compra.
	
	Definir cant_llantas, prec_unit, total Como Entero;
	
	Escribir "Ingrese la cantidad de llantas que va a comprar:"
	Leer cant_llantas;
	
	prec_unit <- 0;
	total <- 0;
	
	Si cant_llantas<5 Entonces
		prec_unit <- 3000;
		total <- cant_llantas*prec_unit;
	SiNo
		Si cant_llantas>=5 Y cant_llantas<=10 Entonces
			prec_unit <- 2500;
			total <- cant_llantas*prec_unit;
		Sino
			Si cant_llantas>10 Entonces
				prec_unit <- 2000;
				total <- cant_llantas*prec_unit;
			FinSi
		FinSi
	Fin Si
	
	Escribir "La persona debe pagar por CADA UNA ", prec_unit, " y debe abonar EN TOTAL ", total;
	
	
FinAlgoritmo
