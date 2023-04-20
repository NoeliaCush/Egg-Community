Algoritmo EjercicioEXTRA4_CondicionalDoble
	
	//La empresa "Te llevo a todos lados" está destinada al alquiler de autos y tiene un sistema 
	//de tarifa que consiste en cobrar el alquiler por hora. Si el cliente devuelve el auto dentro 
	//de las 2 horas de uso el valor que corresponde pagar es de $400 pesos y la nafta va de 
	//regalo. Cuando el cliente regresa a la empresa pasadas las 2 horas, se ingresan la 
	//cantidad de litros de nafta gastados y el tiempo transcurrido en horas. Luego, se le cobra 
	//40 pesos por litro de nafta gastado, y la hora se fracciona en minutos, cobrando un total 
	//de $5,20 el minuto de uso. Realice un programa que permita registrar esa información y el 
	//total a pagar por el cliente.
	
	Definir hora Como Entero;
	Definir cant_ltrs, tarifa Como Real;
	
	Escribir "Ingrese el tiempo transcurrido: ";
	Leer hora;
	Escribir "Ingrese la cantidad de litros de nafta gastados: ";
	Leer cant_ltrs;
	
	tarifa <-0;
	
	Si hora<=2  Entonces
		tarifa <- 400;
	SiNo
		hora <- hora*60;
		tarifa = (cant_ltrs*40)+(hora*5.20);
	Fin Si
	
	Escribir "El total que debe abonar es: ", tarifa;
	

	
FinAlgoritmo
