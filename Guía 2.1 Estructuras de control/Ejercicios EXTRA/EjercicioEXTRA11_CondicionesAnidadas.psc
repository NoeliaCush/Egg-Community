Algoritmo EjercicioEXTRA11_CondicionesAnidadas
	
	//El promedio de los trabajos prácticos de un curso se calcula en base a cuatro notas de las 
	//cuales se elimina la nota menor y se promedian las tres notas más altas. Escriba un 
	//programa que determine cuál es la nota eliminada y el promedio de los trabajos prácticos 
	//de un estudiante.
	
	Definir a, b, c, d, menor Como Enteros;
	Definir promedio Como Real
	
	promedio <- 0;
	menor <- 0;
	
	Escribir "Digite la primer nota:";
	Leer a;
	Escribir "Digite la segunda nota:";
	Leer b;
	Escribir "Digite la tercer nota: ";
	Leer c;
	Escribir "Digite la cuarta nota: ";
	Leer d;
	
	Si a<b Y a<c Y a<d Entonces
		menor <- a;
		promedio <- (b+c+d)/3;
	SiNo
		Si b<a Y b<c Y b<c Entonces
			menor <- b;
			promedio <- (a+c+d)/3;
		SiNo
			Si c<a Y c<b Y c<d Entonces
				menor <- c;
				promedio <- (a+b+d)/3;
			SiNo
				Si d<a Y d<b Y d<c Entonces
					menor <- d;
					promedio <- (a+b+c)/3;
				SiNo
					Escribir "ERROR";
				Fin Si
			Fin Si
		Fin Si
	Fin Si
	
	Escribir "La nota que ha sido eliminada fue: ", menor, " mientras que el promedio de los trabajos prácticos restantes es: ", promedio;
	
	
FinAlgoritmo
