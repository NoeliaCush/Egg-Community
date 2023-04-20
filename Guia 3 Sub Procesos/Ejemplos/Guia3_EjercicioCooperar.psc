Algoritmo Practica
	
	//Realiza una función llamada Cooperar que reciba dos variables de tipo carácter, una variable debe 
	//contener el mensaje "Cooperando" y la otra "trabajamos mejor". La función debe concatenar 
	//ambos textos.
	
	Definir variable1, variable2 Como Caracter
	variable1<- "Cooperando"
	variable2<- " trabajamos mejor"
	
	Escribir cooperar(variable1, variable2)
	
FinAlgoritmo

Funcion palabra1 <- cooperar(variable1 Por Referencia, variable2 Por Referencia)
	Definir palabra1 Como Caracter
	palabra1<- Concatenar ( variable1, variable2)
	
Fin Funcion

