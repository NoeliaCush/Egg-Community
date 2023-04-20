Algoritmo Ejercicio10_BuclesAnidados
	
	//Una compañía de seguros tiene contratados a n vendedores. Cada vendedor realiza 
	//múltiples ventas a la semana. La política de pagos de la compañía es que cada vendedor 
	//recibe un sueldo base más un 10% extra por comisiones de sus ventas. El gerente de la 
	//compañía desea saber, por un lado, cuánto dinero deberá pagar en la semana a cada 
	//vendedor por concepto de comisiones de las ventas realizadas, y por otro lado, cuánto 
	//deberá pagar a cada vendedor como sueldo total (sueldo base + comisiones). Para cada 
	//vendedor ingresar cuanto es su sueldo base, cuantas ventas realizó y cuanto cobró por
	//cada venta.
	
	
	Definir i, cant_empleados, j, cant_ventas Como Entero;
	Definir sueldo_base, cobro_porVenta, comision, total Como Real;
	
	comision <- 0.10;
	total <- 0;
	
	Escribir "Ingrese la cantidad de empleados que tiene su empresa: ";
	Leer cant_empleados;
	
	Para i <- 0 Hasta cant_empleados-1 Con Paso 1 Hacer
		Escribir "Ingrese un nuevo empleado"
		Escribir "Ingrese el sueldo base del empleado: ";
		Leer sueldo_base;
		
		Escribir "Ingrese la cantidad de ventas que el empleado realizó en la semana:"
		Leer cant_ventas;
		
		Para j<-0 Hasta cant_ventas-1 Con Paso 1 Hacer
			Escribir "Ingrese el valor que el empleado cobra por cada venta:";
			Leer cobro_porVenta;
		Fin Para
		
		comision <- cant_ventas*cobro_porVenta*0.10;
		Escribir "Ingrese cuánto es lo que le paga al empleado en concepto de comisiones de venta:", comision;
		
		total <- sueldo_base+comision;
		Escribir "Ingrese cuánto es lo que le paga al empleado en concepto de sueldo total: " total;
		
	Fin Para
	
	
	
FinAlgoritmo
