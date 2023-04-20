Algoritmo EjercicioEXTRA10_CondicionalesAnidadas
	
	//Una verdulería ofrece las manzanas con descuento según la siguiente tabla:
	//Nº DE KILOS COMPRADOS % DESCUENTO
	//0 - 2 <- 0%
	//2.01 - 5 <- 10%
	//5.01 - 10 <-15%
	//10.01 en adelante 20%
	//Determinar cuánto pagará una persona que compre manzanas en esa verdulería
	
	Definir cant_mzna, desc, total Como Real;
	
	Escribir "Indique la cantidad de kilos de manzana comprados: ";
	Leer cant_mzna;
	
	desc <- 0;
	total <- 0;
	
	Si (cant_mzna>=0 Y cant_mzna<=2) Entonces
		desc <- 0;
		total <- cant_mzna - (cant_mzna*desc);
	SiNo
		Si (cant_mzna>=2.01 Y cant_mzna<=5) Entonces
			desc <- 0.10;
			total <- cant_mzna - (cant_mzna*desc);
		SiNo
			Si (cant_mzna>=5.01 Y cant_mzna<=10) Entonces
				desc <- 0.15;
				total <- cant_mzna - (cant_mzna*desc);
			SiNo
				Si cant_mzna>=10.01 Entonces
					desc <- 0.20;
					total <- cant_mzna - (cant_mzna*desc)
				Fin Si
			Fin Si
		Fin Si
	Fin Si
	
	Escribir "El total a pagar es: ", total;
	
	
	
	
FinAlgoritmo
