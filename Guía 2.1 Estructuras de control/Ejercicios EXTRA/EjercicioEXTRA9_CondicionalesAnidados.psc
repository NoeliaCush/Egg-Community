Algoritmo EjercicioEXTRA9_CondicionalesAnidados
	
	//Realice un programa que, dado un a�o, nos diga si es bisiesto o no. Un a�o es bisiesto 
	//bajo las siguientes condiciones: Un a�o divisible por 4 es bisiesto y no debe ser divisible 
	//por 100. Si un a�o es divisible por 100 y adem�s es divisible por 400, tambi�n resulta 
	//bisiesto. Nota: recuerde la funci�n mod de PseInt
	
	Definir anio Como Entero;
	Escribir "Digite un a�o:";
	Leer anio
	
	Si (anio MOD 4=0 O anio MOD 100=0) Entonces
		Escribir "El a�o es BISIESTO";
	SiNo
		Si (anio MOD 100=0 Y anio MOD 400=0) Entonces
			Escribir "El a�o es BISIESTO";
		SiNo
			Escribir "El a�o NO ES BISIESTO";
		FinSi
	Fin Si
	
FinAlgoritmo
