Algoritmo ejrecicio8
	
	definir estudiantes, contadorreprobados, i, cont_aproParcial Como Entero
	
	definir notaintegrador, notaexpocicion, notaparcial,notafinal,sumadesaprobados, cont_integApr, max_notaExp como real
	sumadesaprobados<- 0
	contadorreprobados <- 0	
	cont_integApr <-0
	max_notaExp <- 0;
	cont_aproParcial <- 0;
	
	escribir "ingrese la cantidad de esutdiantes: "
	leer estudiantes
	
	Para i <- 1 Hasta estudiantes Con Paso 1 Hacer
		escribir"ingrese las nota del examen integrador: ";
		leer notaintegrador
		Escribir "Ingrese la nota de exposición: ";
		leer notaexpocicion
		Escribir "Leer nota de parcial:";
		leer notaparcial
		notafinal<- (notaexpocicion+notaintegrador+notaparcial)/3
		
		si notafinal < 6.5 Entonces
			contadorreprobados = contadorreprobados+1
			sumadesaprobados = sumadesaprobados+notafinal
		FinSi
		
		Si notaintegrador>=7.5 Entonces
			cont_integApr <- cont_integApr+1
		Fin Si
		
		Si notaexpocicion>max_notaExp Entonces
			max_notaExp <- notaexpocicion
		FinSi
		
		Si (notaparcial>= 4 Y notaparcial<=7.5) Entonces
			cont_aproParcial <- cont_aproParcial+1
		
		Fin Si
		
	Fin Para
	
	escribir "La cantidad de estudiantes reporbados fue: ", contadorreprobados;
	Escribir "La suma de notas de los estudiantes reprobados fue: ", sumadesaprobados;
	Escribir "La Nota promedio final de los estudiantes que reprobaron del curso fue : ", sumadesaprobados / contadorreprobados;
	
	Escribir "==============";
	
	Escribir "El procentaje de alumnos que tienen una nota de integrador mayor (o igual) a 7.5 es: ", cont_integApr*100/estudiantes, " %";
	
	Escribir "=========";
	
	Escribir "La mayor nota obtenida en las exposiciones fue: " max_notaExp;
	
	Escribir "======"
	
	Escribir "El total de estudiantes que obtuvieron en el parcial una nota entre 4 y 7.5 fue: ", cont_aproParcial;
	
FinAlgoritmo

	

