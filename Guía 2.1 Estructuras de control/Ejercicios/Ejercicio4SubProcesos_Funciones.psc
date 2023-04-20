Funcion veces_repite <- totalDeLetras(frase Por Referencia, letra Por Referencia)
	
	
	Definir veces_repite, contador, i  Como Entero
	
	contador = 0;
	
	
	Para i<-0 Hasta Longitud(frase) Hacer
		Si letra= Subcadena(frase,i,i) Entonces
			contador = contador +1;
		FinSi
	FinPara
	
	veces_repite = contador;
	
Fin Funcion

//Realizar un programa que pida al usuario una frase y una letra a buscar en esa frase. La 
//función debe devolver la cantidad de veces que encontró la letra. Nota: recordar el uso de la 
//función Subcadena().

Algoritmo Ejercicio4SubProcesos_Funciones
	
	Definir frase Como Cadena;
	Definir letra Como Caracter;
	
	Escribir "Ingrese una frase"
	Leer frase;
	
	Escribir "Ingrese una letra que desee buscar en la frase:"
	Leer letra;
	
	
	Escribir "La cantidad de letras que tiene la frase: ", frase, " es:" totalDeLetras(frase,letra)
	
	
	
	
	
FinAlgoritmo
