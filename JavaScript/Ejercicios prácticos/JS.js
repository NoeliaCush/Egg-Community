/*1) Escribir un algoritmo en el cual se consulte al usuario que ingrese
¿cómo está el día de hoy? (soleado, nublado, lloviendo).
 A continuación, mostrar por pantalla un mensaje que indique
“El día de hoy está ...”, completando el mensaje con el dato
que ingresó el usuario.

var clima= window.prompt('¿Cómo está el día allá?', 'soleado, nublado, lloviendo');
window.alert('El día de hoy está...' + clima); */

/* 2) Conocido el número en matemática PI π, pedir al usuario que ingrese el valor del radio 
de una circunferencia y calcular y mostrar por pantalla el área y perímetro. Recuerde que 
para calcular el área y el perímetro se utilizan las siguientes fórmulas: 
area = PI * radio2 
perimetro = 2 * PI * radio  

const PI = 3.141592653589793;
var radio = window.prompt('Ingrese el valor de radio', 5);
var area = window.alert('El valor del área es igual a ' +(PI*(radio^2)));
var perimetro = window.alert('El valor del perímetro es igual a ' +(2*PI*radio));*/

/* 3) Escriba un programa en donde se pida la edad del usuario. Si el usuario es mayor de 
edad se debe mostrar un mensaje indicándolo.  

var edad = window.prompt('¿Cuántos años tenés?', 24);
if(edad >=18){
   window.alert('Su edad es '+ edad +' ¡Usted es mayor de edad!');
}else{
    window.alert('Su edad es '+ edad +' ¡Usted no cumple con la mayoría de edad!');
}*/

/* 4) Realiza un programa que sólo permita introducir los caracteres ‘S’ y ‘N’. Si el usuario 
ingresa alguno de esos dos caracteres se deberá de imprimir un mensaje por pantalla 
que diga “CORRECTO”, en caso contrario, se deberá imprimir “INCORRECTO”

var respuesta = window.prompt('Ingrese una respuesta', 'S o N');
if(respuesta == 'S' || respuesta == 'N'){
    window.alert('CORRECTO');
}else {
    window.alert('INCORRECTO');
}*/

/* 5) Construir un programa que simule un menú de opciones para realizar las cuatro 
operaciones aritméticas básicas (suma, resta, multiplicación y división) con dos valores 
numéricos enteros. El usuario, además, debe especificar la operación con el primer 
carácter de la operación que desea realizar: ‘S' o ‘s’ para la suma, ‘R’ o ‘r’ para la resta, ‘M’ 
o ‘m’ para la multiplicación y ‘D’ o ‘d’ para la división.

var num1 = window.prompt('Ingrese un número', 10);
var num2 = window.prompt('Ingrese otro numero', 2);

var opcion = window.prompt(`Ingrese la operación que desee realizar:
                        Suma (S)
                        Resta(R)
                        Multiplicacion(M)
                        Division(D)`);

switch(opcion){
    case 'S':
    case 's':
        window.alert('El resultado de la suma es '+ (parseInt(num1)+parseInt(num2)));
        break;
    case 'R':
    case 'r':
        window.alert('El resultado de la resta es ' + (num1-num2));
        break;
    case 'M':
    case 'm':
        window.alert('El resultado de la multiplicacion es ' +(num1*num2));
        break;
    case 'D':
    case 'd':

        window.alert('El resultado de la division es ' + (num1/num2));
    break;
    default:
        window.alert('La opción ingresada no es válida');
}*/

/* 6) Realizar un programa que, dado un número entero, visualice en pantalla si es par o impar. 
En caso de que el valor ingresado sea 0, se debe mostrar “el número no es par ni impar”

var numero = window.prompt('Ingrese un número', 10);
auxnum = parseInt(numero);

if(auxnum==0){
    window.alert('El número ' + numero +' ¡no es par ni impar!');
}else if(auxnum%2 == 1){
    window.alert('El número ' + numero + ' ¡es IMPAR!');
}else if (auxnum%2 == 0){
    window.alert('El número ' + numero + ' ¡es PAR!');
}*/

/* 7) Escriba un programa en el cual se ingrese un valor límite positivo, y a continuación 
solicite números al usuario hasta que la suma de los números introducidos supere el 
límite inicial. 

var limite = window.prompt('Ingrese un número para establecer como límite', 10);
var auxLimite = parseInt(limite);

for(let i=0; i <=auxLimite; i++){
    var numero = window.prompt('Ingrese un número');
    var auxNum = parseInt(numero);

    i += auxNum;

    if(i>auxLimite){
        window.alert('La suma de los valores ingresados ( ' + i + ' ) ha superado el límite ( ' + auxLimite + ' ).');
    }
}*/

/* 8) Escribir un programa que lea números enteros hasta teclear 0 (cero). Al finalizar el 
programa se debe mostrar el máximo número ingresado, el mínimo, y el promedio de 
todos ellos. 


var numero;
var suma = 0;
var cantidad = 0;
var flag = true;
var max = 0;
var min = 0;

do{
    var numero = window.prompt('Ingrese un número: ');
    var auxNum = parseInt(numero);

    suma += auxNum;

    if(auxNum != 0) {
        cantidad ++
    }

    if(flag==true){
        max = auxNum;
        min = auxNum;
        flag = false;
    } else if(auxNum > max){
        max = auxNum;

    }else if (auxNum < min && auxNum !=0){
        min = auxNum;
    }

}while((auxNum) != 0);

window.alert(`¡Programa Finalizado!
El máximo número ingresado es: ${max},
El mínimo número ingresado es: ${min},
El promedio de los números ingresados es: ${(suma/cantidad)}`);*/

/* 9) Realizar un programa que pida una frase y el programa deberá mostrar la frase con un 
espacio entre cada letra. La frase se mostrara así: H o l a. Nota: recordar el 
funcionamiento de la función Substring()

const frase = window.prompt("Por favor, ingrese una frase");
let i = 0;
let nuevaFrase = "";

for(i = 0; i <= frase.length -1; i++){
    nuevaFrase += (frase.substring(i,i+1)) + " ";
}

window.alert(`La frase quería así:
${nuevaFrase}`); */

/* 10) Escribir una función flecha que reciba una palabra
y la devuelva al revés. 

let revertir = (frase) => {
    
    var frase = window.prompt('Por favor, ingrese una frase');

    return frase.split("").reverse().join("")
}

window.alert('La frase quedaría así: ' + revertir());*/

/* 11) Escribir una función que reciba un String y devuelva la palabra más larga. 
String Ejemplo: “Guia de JavaScript”
Resultado esperado : “JavaScript 

let frase = window.prompt('Por favor ingrese una frase');

const palabraMasLarga = (frase) =>{

    const separar = frase.split(" ");
    let palabraMasLarga = separar [0];
    for ( const palabra of separar){
        if(palabra.length >= palabraMasLarga){
            palabraMasLarga = palabra;
        }
    }
    return palabraMasLarga;
}

const palabra = palabraMasLarga(frase);

window.alert('La palabra más larga es: ' + palabra); */

/* 12) Escribir una función flecha de JavaScript que reciba un argumento y retorne el tipo de 
dato. 

var argumento = () => {
    return typeof(window.prompt('Por favor, ingrese un argumento'))
};

window.alert('El tipo de dato ingresado es: ' + argumento());*/

/* 13) Crear un objeto persona, con las propiedades nombre, edad, sexo
('H' hombre, 'M' mujer, 'O' otro), peso y altura.
A continuación, muestre las propiedades del objeto JavaScript.

function Persona (nombre, edad, sexo, peso, altura){
    this.nombre = nombre;
    this. edad = edad;
    this.sexo = sexo;
    this.peso = peso;
    this.altura = altura;
    this.mostrarPersona = mostrarPersona;
}

var noe = new Persona('Noelia Cruz', 24, 'F', 84, 167);

function mostrarPersona(){
    var resultado = (`Datos personales:
    Nombre completo: ${this.nombre}
    Edad: ${this.edad} años
    Sexo: ${this.sexo}
    Peso: ${this.peso} kg
    Altura: ${this.altura} cm`);

   window.alert(resultado);
}

noe.mostrarPersona();*/

/* 14) Crear un objeto libro que contenga las siguientes propiedades:
 ISBN, Título, Autor, Número de páginas.
 Crear un método para cargar un libro pidiendo los datos al usuario y luego
  informar mediante otro método el número de ISBN, el título,
  el autor del libro y el numero de páginas 

function Libro (isbn, titulo, autor, numeroPag){
    this.isbn = isbn;
    this.titulo = titulo;
    this.autor = autor;
    this.numeroPag = numeroPag;
    this.cargarLibro = cargarLibro;
    this.mostrarLibro = mostrarLibro;
}

var libro1 = new Libro();

function cargarLibro(){
    this.isbn = window.prompt('Ingrese el número ISBN');
    this.titulo = window.prompt('Ingrese el titulo del libro');
    this.autor = window.prompt('Ingrese el nombre del autor');
    this.numeroPag= window.prompt('Ingrese la cantidad de páginas que tiene el libro');
}

libro1.cargarLibro();

function mostrarLibro(){
    var resultado = (`Datos del libro:
    ISBN: ${this.isbn}
    Título: ${this.titulo}
    Autor: ${this.autor}
    Número de páginas: ${this.numeroPag}`);

   window.alert(resultado);
}

libro1.mostrarLibro();*/

/* 15) Escribe un programa JavaScript para calcular
el área y el perímetro de un objeto Círculo con la propiedad radio.
Nota: Cree dos métodos para calcular el área y el perímetro.
El radio del círculo lo proporcionará el usuario 

var radio = window.prompt('Por favor, ingrese un valor');
var auxRadio = parseInt(radio);

window.alert('El valor del radio es ' + auxRadio);

const calcularPerimetro = (auxRadio) => {
    return (Math.PI*2*auxRadio);
}

const perimetro = calcularPerimetro(auxRadio);

const calcularArea = (auxRadio) =>{
    return (Math.PI*Math.pow(auxRadio,2));
}

const area = calcularArea(auxRadio);

window.alert(`Para un círculo cuyo radio es ${auxRadio} su
área es ${area}
perímetro es ${perimetro}`); */

/* 16) Realizar un programa que rellene dos vectores al mismo tiempo,
con 5 valores aleatorios y los muestre por pantalla 

var a = new Array(5);
var b = new Array(5);

for (var i=0; i<5; i++){
    a[i] = Math.round(Math.random()*10);
    b[i] = Math.round(Math.random()*10);
}

window.alert(`El primer vector [${a}] 
El segundo vector [${b}]`);*/

/* 17) Realizar un programa que elimine los dos últimos elementos de un array.
Mostrar el resultado 

var a = [2,4,5,7,8];

window.alert('El tamaño del array es: ' + a.length);

a.splice(3,2);

window.alert ('El array queda de la siguiente manera: ' + a);*/

/* 18) A partir del siguiente array:
var valores = [true, 5, false, "hola", "adios", 2]:
a) Determinar cual de los dos elementos de texto es mayor
b) Utilizando exclusivamente los dos valores booleanos del array,
determinar los operadores necesarios para obtener un resultado true
y otro resultado false
c) Determinar el resultado de las cinco operaciones
matemáticas realizadas con los dos elementos numéricos

var valores = [true, 5, false, "hola", "adios", 2];

var maximo = "";
for (let i = 0; i <valores.length; i++){
    if(typeof(valores[i]) == "string"){
        if(valores[i].length > maximo.length){
            maximo = valores[i];
        }
    }
}

window.alert('El elemento de texto mayor es ' + maximo);

var valor1 = valores[0];
var valor2 = valores[2];
var resultado = valor1 || valor2;
window.alert(resultado);
resultado = valor1 && valor2;
window.alert(resultado);

var num = parseInt(valores[1]);
var num1 = parseInt(valores[5]);
var opcion = window.prompt(`Ingrese la operación que desee realizar:
s = suma;
r = resta;
m = multiplicacion;
d = division;`);

switch(opcion){
    case 's':
        window.alert('El resultado de la suma es ' + (num + num1));
        break;
    case 'r':
        window.alert('El resultado de la resta es ' + (num - num1));
        break;
    case 'm':
        window.alert('El resultado de la multiplicacion es ' +(num * num1));
        break;
    case 'd':
        window.alert('El resultado de la division es ' + (num / num1));
        break;
}*/

/* 19) Realizar un programa en Java donde se creen dos arreglos: el primero será un arreglo A 
de 50 números reales, y el segundo B, un arreglo de 20 números, también reales. El 
programa deberá inicializar el arreglo A con números aleatorios y mostrarlo por pantalla. 
Luego, el arreglo A se debe ordenar de menor a mayor y copiar los primeros 10 números 
ordenados al arreglo B de 20 elementos, y rellenar los 10 últimos elementos con el valor 
0.5. Mostrar los dos arreglos resultantes: el ordenado de 50 elementos y el combinado 
de 20.

var a = [];
var b = [];

for (let i = 0; i<=50; i++){
    a[i] = (Math.random()*10).toFixed(2);
}

window.alert(`El arrglo A: ${a}` );

//Ordenar de menor a mayor el arrglo a

window.alert(`El A arreglo ordenado: ${a.sort()}`);

for(let i = 0; i <=20; i++){
    b[i] = (Math.random()*10).toFixed(2);
}

window.alert(`A: ${a.slice(1,11)}`);

window.alert(b.concat(a.slice(1,11)));*/

/* 20) Realizar un programa que obtenga la siguiente matriz [[3], [6], [9], [12], [15]]
y devuelve y muestre el siguiente array [6, 9, 12, 15, 18]. 


var arr = [[3], [6], [9], [12], [15]];

var resultado = arr.flatMap((x) => parseInt(x) + 3);

window.alert(resultado);*/

/* 21) Escribir un programa para obtener un array de las propiedades de un objeto Persona. 
Las propiedades son nombre, edad, sexo ('H' hombre, 'M' mujer, 'O' otro), peso y altura. 

const persona = {
    nombre: "Noelia",
    edad: 24,
    sexo: "M",
    peso: 85,
    altura: 167,
};

window.alert(`[${Object.values(persona)}]`);*/

/* 22) Escribir un programa de JavaScript que al clickear un botón muestre un mensaje a 
elección. 

function mostrarMensaje(){
    window.alert("Este es un mensaje enviado desde JavaScript");
} */



