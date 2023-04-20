Algoritmo Ejercicio4_HacerMientasQue
	
	Definir clave Como Caracter
	Definir intento Como Entero
	
	intento =3
	Escribir "Tenes "  intento " intentos"
	
	Repetir
		Escribir "Ingresa la clave"
		Leer clave
		Si clave = "EUREKA"
			intento=3-3
			Escribir "Tiene acceso al sistema"
			Limpiar Pantalla
		SiNo
			intento = intento -1
			Escribir "Tenes " intento " intentos menos"
		FinSi
	Mientras Que intento <>0
	
	
	
FinAlgoritmo
