Algoritmo EjercicioEXTRA2_CondicionalDoble
	
	//Una tienda ofrece para los meses de septiembre, octubre y noviembre un descuento del 
	//10% sobre el total de la compra que realiza un cliente. Solicitar al usuario que ingrese un 
	//mes y el importe de la compra. El programa debe calcular cuál es el monto total que se 
	//debe cobrar al cliente e imprimirlo por pantalla. 
	
	Definir mes Como Entero;
	Definir val_compra, desc, total Como Real;
	
	Escribir "Ingrese el mes en el que realizó la compra: ";
	Escribir "1. SEPTIEMBRE";
	Escribir "2. OCTUBRE";
	Escribir "3. NOVIEMBRE";
	Leer mes;
	
	Escribir "Ingrese el importe de su compra: ";
	Leer val_compra;
	
	desc<- 0.10;
	total <-0;
	
	Si mes=1 O mes=2 O mes=3 Entonces
		total <- val_compra- (val_compra*desc);
	SiNo
		Escribir "EL MES QUE INGRESÓ NO ES VÁLIDO";
	Fin Si
	
	Escribir "El monto total que debe abonar el cliente es: ", total;
	
	
FinAlgoritmo
