                    // Salida y entrada de datos:

/* console.log: imprime la salida por consola
console.log("abc");
console.log(123);
console.log([1,2,3,4]);*/

/* console.error(): registra mensaje error en la consola 
console.error("Mensaje de error");*/

/* console.warn: registra un mensaje de advertencia 
console.warn("Mensaje de advertencia");*/

/* console.clear(): limpia la consola 
console.clear();*/

/* console.time(): saber la cantidad de tiempo empleado por bloque 
console.time('abc');*/

/* console.timeEnd(): termina el temporizador para saber el tiempo empleado en un bloque 
console.timeEnd('abc'); */

/* console.table(): crea una tabla dentro de la consola 
console.table({'a':1,'b':2});*/

/* console.count(): cuenta el número que la función alcanza con este método 
for(let i=0; i<5;i++){
    console.count(i);
}*/

/* console custom 
const spacing = '10px';
const styles = `padding: ${spacing}; background-color: black;
color: yellow; font-style: italic; border: 1px solid black; font-size: 2em;`;
console.log('%cEGG', styles); */

                  // Objeto Window

/* window.prompt(): solicita al usuario que introduzca un texto 
window.prompt("Ingrese su nombre:"); */

/* window.alert(): muestra un diálogo de alerta con contenido y un botón OK 
window.alert("¡Saludos desde JavaScript!");*/

/*var nombre = window.prompt("¿Cuál es tu nombre?", "Noelia");
window.alert("Tu nombre es: " + nombre);*/

                  // Variables en JavaScript

/* var variable: no se coloca un tipo de dato a la variable cuando se declara 
var precio1 = 5;
var precio2 = 6;
var total = precio1 + precio2;
window.alert("El precio total es: " + total); */

/* let: permite que al declarar una variable solo de acceda dentro de un 
bloque en concreto 
function varPrueba(){
    var x = 31;
    if (true){
        var x = 71;
        console.log(x);
    }
    console.log(x);
}
function letPrueba(){
    let x =31;
    if (true){
        let x =71;
        console.log(x);
    }
    console.log(x);
}*/

/* const: declara una constante, especificando su vaor en la
misma sentencia en la que se declara 
const PI = 3.141592653589793;*/

                  // Template Strings

/* creación de template strings: se usa símbolo de acento grave `` 
var cadena = `Esto es un template String`; */

/* uso de los template strings:
1. concatenación de valores: permite colocar expresiones encerradas 
entre llaves ${expresion} logrando volvar lo que se quiera dentro
de una cadena:
var nombre = 'Miguel Angel';
var apellidos = 'Alvarez';
var profesion = 'Desarrollador';
var perfil = `<b>${nombre} ${apellidos}</b> es ${profesion}`;

En las expresiones se coloca el código que se quiera volcar dentro
de la cadena: 

var suma= `45 + 832 = ${45+832}`;
window.alert(suma);

var operando1 = 7;
var operando2 = 9;
var multiplicación = `La multiplicación entre ${operando1} y ${operando2}
equivale a ${operando1 * operando2}`;
window.alert(multiplicación);

2. saltos de línea dentro de cadenas

var textLargo = `Esto es un texto
con varias líneas`;
window.alert(textLargo); */

                  // Tipos de datos en JavaScript
            
/* numéricos: enteros o reales
var numero = 123; */
/* string: cadenas de texto 
var cadena = '123';*/
/* boolean: valores lógicos como true o false 
var bandera = true;*/
/* null: cuando el dato no existe
var nulo = null;*/
/* undefined: cuando no se le asigna valor a una variable 
var flag;*/

/* typeof: se obtiene el tipo de dato que tiene la variable 
console.log(typeof 42);
console.log(typeof 'blubber');
console.log(typeof true);*/

                  // Condicionales en JavaScript

/* IF: condicional lógico que evalúa el camino a tomar en base
a la evaluación de una condición 
let edad = 15;
let altura = 166;
if(edad>18 && altura>160){
    console.log("Podes subirte :D");
}else{
    console.log("No podés subirte D:");
}

Se puede agregar la condición ELSE IF 

var a = prompt("Ingrese el valor de a");

if(a==2){
    console.log("a es igual a 2");
}else if(a<2){
    console.log("a es menor que 2");
}else{
    console.log("a es mayor que 2");
}*/

/* IF TERNARIO: permite ahorrar líneas y caracteres al
escribir los scripts varibale = (condición) ? valor1 : valor2;*/

/* SWITCH: evalúa una expresión y lo compara con una instancia case
var expr = window.prompt("Ingrese lo que quiere comprar: ");
switch(expr){
    case 'Naranjas':
        console.log('El kilogramo de narnajas cuesta $0.59');
    break;
    case 'Mangos':
    case 'Papayas':
        console.log('El kilogramo de mangos y papayas cuesta $2.79');
    break;
    default:
        console.log('Lo lamentamos, por el momento no disponemos de ' + expr +
        '.');
} */

                  // Estructuras repetitivas

/* WHILE: evalúa la condición antes de ejecutar la sentencia 
let a=0;
while(a != 10){
    console.log(++a);
}*/

/* DO WHILE: evalúa la condición después de ejecutar la sentencia 
let a=0;
do{
    console.log(++a);
}while(a!=10);*/

/* FOR: repote una o más instrucciones de un determinado número deveces.
Se usa cuando se sabe con seguridad el número de veces que se quiere 
ejecutar
for([expresion-inicial]; [condicion]; [expresion-final]){} 

for(let i = 0; i <10; i++){
    console.log("El valor de i es " + i);
}*/

/* BREAK: termina el bucle actual y transfiere el control del 
programa a la siguente sentencia 

for(let i = 0; i < 10; i++){
    if (i == 5){
        break;
    }
    console.log("Estamos por la vuelta " + i);
}*/

/* CONTINUE: continúa la sentencia de la iteración actual y continúa
la ejecución la ejecución del bucle con la siguiente iteración.
No termina la ejecución sino que regresa a la condición (WHILE)
o salta a la expresión actualizada (FOR) 

for(let i = 0; i < 10; i++){
    if (i == 5){
        continue;
    }
    console.log("Estamos por la vuelta " + i);
}*/

/* LABEL: proporciona una sentencia con identificador con el que se
referir al usar las sentencias de BREAK y CONTINUE
label o etiqueta: sentencia

label: for(let i = 0; i < 10; i++){
    for (let j = 0; j < 10; j++){
        if (i == 4 && j ==4){
            console.log("Vamos a contar ambos for");
            break label;
        }
        console.log(i+j+10*i);
    }
}*/

                  // Funciones en JavaScript

/* SINTAXIS de la función: 
function nombreFunción(){
    instrucciones de la nombreFunción
    ...
}

function holaMundo(){
    console.log('Hola Mundo');
}

holaMundo();*/

/* Donde se colocan las funciones JavaScript 
a) Colocar la función en el mismo bloque de script
b) Colocar la función en otro bloque de script*/

/*Parámetros de las funciones: son los valores de entrada que
recibe una función 

function escribirBienvenida(nombre){
    console.log('Hola ' + nombre);
}
let nombre = 'Agustin';
escribirBienvenida(nombre);*/

/* Devolver valores en funciones: pueden retornar valores 

function media(valor1, valor2){
    let resultado;
    resultado = (valor1 + valor2) / 2;
    return resultado;
}

let miMedia = media(12,8);
console.log(miMedia);*/

/* Funciones FECHA: sintaxis MAS concisa para crear funciones
let func = (arg1, arg2,...,argN) => expresion 

let sum = (a,b) => a+b;
console.log(sum(1,2));

let double = n => n * 2;
console.log(double(3));

let saludar = () => console.log("¡Hola!");
saludar()*/

                  // Objetos

/* Son una colección de propiedad que su ves son una asociación entre
un nombre y un valor, siendo el valor una función (conociendose como método)
JavaScript USA los objetos y NO programa orientado a ellos */

/* Objetos y propiedades: definen las características del objeto
nombreObjeto.nombrePropiedad 

var miAuto = {
    marca : 'Ford',
    modelo : 'Mustang',
    anio : '1969',
}*/

/* Usar una función constructora:
1. Define el tipo de objeto definiendo una función constructora
function Auto(marca, modelo, anio){
    this.marca = marca;
    this.modelo = modelo;
    this.anio = anio;
}
2. Crea la instacia del objeto con el operador new
var miAuto = new Auto('Ford', 'Mustang', 1969); 

Se puede crear cualquier número de objetos Auto con las llamadas New
var auto1 = new Auto ('Nissan', '300ZX', 1992);
var auto2 = new Auto ('Mazda', 'Miata', 1990);

Un objeto puede tener una propiedad que es de otro objeto

function Persona(nombre, edad, sexo){
    this.nombre = nombre;
    this.edad = edad;
    this.sexo = sexo;
}

var agus = new Persona('Agustina Gomez', 33, 'F');
var valen = new Persona('Valentin Perez', 39, 'M');

function Auto(marca, modelo, anio, propietario){
    this.marca = marca;
    this.modelo = modelo;
    this.anio = anio;
    this.propietario = propietario;
}

var auto1 = new Auto ('Nissan', '300ZX', 1992, agus);
var auto2 = new Auto ('Mazda', 'Miata', 1990, valen);

Si luego se quiere averiguar el nombre del propietario del auto2
se puede acceder de esta manera:
auto2.propietario.nombre;*/

/* Definición de métodos: se definen como una función 
pero tienen que ser asignados como la propiedad de un objeto
var miObj = {
    miMetodo: function(parametros){
        ....
    }
};
Se llama al método de esta manera:
objeto.nombreMetodo(parametros); 

function mostrarAuto(){
    var resultado = (`Un hermoso ${this.anio} ${this.marca} ${this.modelo}`);
    console.log(resultado);
}

function Auto(marca, modelo, anio){
    this.marca = marca;
    this.modelo = modelo;
    this.anio = anio;
    this.mostrarAuto = mostrarAuto;
}

var auto1 = new Auto ('Nissan', '300ZX', 1992);
var auto2 = new Auto ('Mazda', 'Miata', 1990);

auto1.mostrarAuto;
auto2.mostrarAuto;*/

                  // Objetos incorporados en JavaScript

/* Pueden utilizarse por las aplicaciones sin tener que declararlos, son;

- String para trabajar con cadenas de caracteres
- Date para trabajar con fechas
- Math para realizar funciones matemáticas
- Number para realizar algunas cosas con números
- Boolean trabajo con booleanos
- Array para trabajos con listas
*/

/* STRING: asigna un texto a una variable
Propiedades:
    
    Length: guarda el número de caracteres del String
    
        let cadena = "Hola;
        console.log(cadena.length);

Métodos de string:
    
    charAt(): Devuelve el caracter que hay en la posición indicada
        como "indice" (i). La posición inicia en 0;
    toString(): Convierte en cadena los objetos;
    indexOf(carácter,desde): devuelve la posición de la PRIMERA VEZ
        en la que se encuentra el "caracter" indicado
        por parámetros en un String
    lastIndexOf(caracter, desde): devuelve la posición desde el FINAL
        en donde se encuentra el "caracter" indicado por parámetros
    toLowerCase():pone todos los caracteres del string en MINUSCULA
    toUpperCase(): pone todos los caracteres del string en MAYUSCULA
    replace(substring_a_buscar, nuevoStr): reemplaza posiciones del texto
        de un string por otro texto. Se devuelve el RESULTANTE de hacer el 
        reemplazo
    substring(inicio, fin): devuelce el substring que empieza en el 
        caracter de "inicio" y termina en el caracter "fin"
    */

/* MATH: una de las clases NATIVAS de JavaScript
Métodos de Math: la sintaxis es "Math.metodo"
    
    abs(): Devuelve el valor ABSOLUTO de un número:
    ceil(): Devuelve un entero IGUAL o INMEDIATAMENTE SIGUENTE
        de un número;
    exp(): Retorna el resultado de elevar el número E por un número
    floor(): Devuelve un entero IGUAL o INMEDIATAMENTE ANTERIOR 
        de un número;
    max(): Retorna el MAYOR de dos números;
    min(): Retorna el MENOR de dos números;
    pow(): Recibe 2 números como PARAMETROS y devyelve el primer
    número ELEVADO al segundo número
    random(): Devuelve un número ALEATORIO entre 0 y 1;
    round(): REDONDEA al entero MAS PROXIMO;
    PI: permite tener el VALOR PI;
*/

/* DATE: se debe INSTANCIAR la CLASE date y se podrá realizar todas
operaciones necesarias.
Crear un objeto fecha con día y hora ACTUALES: miFecha = new Date()
Crear un objeto fecha con día y hora DISTINTOS: miFecha = new Date(año, mes,dia)

Métodos de Date:

    getDate(): Devuelve el día del mes;
    getDay(): Devuelve el día de la semana;
    getHours(): Retorna la hora;
    getMinutes(): Devuelve los minutos;
    getMonth(): Devuelve el mes;
    getFullYear(): Retorna el año con todos los digitos;
    setDate():Actualiza el día del mes;
    setHours(): Actualiza la hora;
    setMinutes(): Cambia los minutos;
    setFullYear(): Cambia el año de la fecha al número que recibe por parámetro;
*/

/* ARRAYS: son objetos SIMILARES a una lista cuyo prototipo proporciona
métodos para efecutar operaciones de recorrido y de mutación.

Declaración:
    Hay dos sintaxis para crear un array vacío:
        let arr = new Array();
        let arr = [];
    Se puede suministrar elementos iniciales entre los corchetes:
        let frutas = ["Manzana", "Naranja", "Uva"];
    Los elementos son enumerados desde el 0 y es posible obetener un elemento
    por su número entre corchetes:
        let frutas = ["Manzana", "Naranja", "Uva"];
        console.log(frutas[0]);
        console.log(frutas[1]);
        console.log(frutas[2]);
    Se puede REEMPLAZAR un elemento:
        frutas[2] = "Pera";
    Se puede AGREGAR uno al array:
        frutas[3] = "Limon";
    Un array puede almacenar elementos de CUALQUIER TIPO
        let frutas = ["Manzana", 1, true, function()];
    La cuenta TOTAL de elemtnos en el array es su longitud
        console.log(frutas.length);

Bucles: una forma de ITERAR los items de un array es con un bucle for:
    let frutas = ["Manzana", "Naranja", "Uva"];
    for (let i = 0; i < frutas.length; i++){
        console.log( frutas[i] );
    }

.ForEach: método que recorre un array de INICIO a FIN y ejecuta una FUNCION
    sobre CADA elemento dentro del array.
    Su sentencia es:
        array.forEach(function(valorActual, indice, array){}, thisValor);
    Los parámetros son:
        - function: funcion a ejecutar por cada elemento. Recibe tres argumentos:
            + valorActual: el elemento que es procesado por el array
            + index: índice del elemento actual siendo procesado en el array
            + array: el vector que en el forEach está siendo aplicado
        - thisValor: valor que se usará cuando se ejecute el callback
        
Imprimir el contenido de un array: permite mostrar los elementos de un array
    function mostrarElementosArray(elemento, indice, array){
        console.log("a [ " + indice + " ] = " + elemento);
    }
    Si se hiciera todo junto dentro del ForEach:
        let array = [2,5,9];
        array.forEeach(function mostrarElementosArray(elemento, indice, array){
            console.log("a [ " + indice + " ] = " + elemento);
        })

For Of: es un BUCLE que itera SOBRE un elemento, tomara cada uno de los
    elementos y los almacenará en una variable temporal.
    for (let empleado of empleados){
        console.log(empleado.nombre);
        console.log(empleado.apellido);
    }

For In: itera SOBRE los elementos DENTRO DE UN DATO. 
    Por ejemplo se puede usar un for of para recorrer la lista de empleados
    y luego se toma un empleado con el for in para recorrer cada una de las 
    propiedades del empleado.

    for (let empleado of empleados){
        for (let dato in empleado){
            console.log(empleado[dato]);
        }
    }

Métodos objeto Array:

    splice(): permite insetar, remover y reemplazar elemento de un array.
        arr.splice(inicio[, cantEliminar, elem1,...,elemN])
        Luego, devuelve un array con los elementos removidos.
    slice(): devuelve una copia de una PARTE del array dentro de uno nuevo,
        emplezando desde INICIO hasta FIN (fin no incluido)
        arr.slice([inicio], [fin]);
    slipt(): separa la string EN elementos según el delimitante "delim" dado 
        y los devuelve como un array
        let nombres = 'Bilbo, Gandalf, Nazgul';
        let arr = nombres.split(', ');
        for ( let name of arr){
            console.log(`Un mensaje para ${name},`);
        }
    sort(fn): ordena el array cambiando el orden de los elementos
        El criterio de reordamiento se debe proporcionar una función con argumento
        la cual tendrá que comparar dos valores arbitrarios y devolver un resultado
    map(): crea un nuevo array con los resultados de la llamada a la
        función indicada aplicados a cada uno de sus elementos. Su sintaxis:
        let result = arr.map(function(elemento, indice, array){

        })
        console.log(result);
    flat(): crea una nueva matriz con todos los elementos de sub-array
        concatenados hasta la profundidad especificada
        var nuevoArray = arr.flat([profundidad]);
    flatMap(): devuelve im mievp array formado al aplicar una función de 
        devolución de llamada determinada a cada elemento de la matriz
        var arrayNuevo = array.flatMap(function(elemento, indice, array){

        })

Métodos extras de array:

    concat(): une dos o más arrays
        var arraytotal = array1.concat(array2);
    join(): junta los elementos de un array en una cadena con un separador
        var fruta = ["Kiwi", "Limon", "Otra"];
        var ej = fruta.join();
    pop(): borra el último elemento del array y devuelve su contenido
        var a = frutar.pop();
    push(): añade nuevos elementos al array y devuelve su nueva longitud
        var a = frutas.push("Uva");
    shift(): elimina el primer elemento del array y devuelve el elemento
        var a = frutas.shift();
    find():devuelve el valor del primer eleento del array que cumple la 
        función de prueba proporcionada
        const array1 = [5,12,8,130,44];
        const encontrado = array1.find(elemento => elemento >10);
        console.log(encontrado);
    unshift(): añade elementos al inicio del array y devuelve la nueva longitud
        var frutas = ["Banana", "Naranja", "Manzana"];
        frutas.unshift("Limon", "Anana"); */


                  // Objetos Map y Set

/* Estructuras de datos aprendidas:
- Objetos para almacenar colecciones de datos ordenados mediante una clave
- Arrays para almacenar colecciones ordenadas de datos */

/* Map: es una collección de datos identificados por claves pero que 
permite claves de cualquier tipo.
Los métodos y propiedades son:
    - new Map(): crea el mapa
    - map.set(clave, valor): almacema eñ valor asociado a la clave;
    - map.get(clave): devuelve el valor de la clave;
    - map.has(clave): devuelve true si la clave existe en map, false si no
    - map.delete(clave): elimina el valor de la clave
    - map.clear(): elimina todo el mapa
    - map.size(): devuelve la cantidad actual de elementos

Iteración sobre map: para recorrer hay 3 métodos
    - map.keys(): devuelve un iterable para las claves;
    - map.values(): duvuelve un iterable para los valores;
    - map.entries(): devuelve un iterable para las entradas; */


/* Set: cada valo puede aparecer solo una vez. Sus principales métodos son:
    - new Set: crea el set;
    - set.add(valor): agrega un valor, y devuelve el set en si;
    - set.delete(valor): elimina el valor, y devuelve true si el valor existía
        al momento de la llamada, sino, devuelve false;
    - set.has(valor): devuelve true si el valor existe en el set, sino,
        devuelve false;
    - set.clear(): elimina todo el contenido del set;
    - set.size: es la cantidad de elementos;

Iteración sobre set: recorre Set con for of o usando forEach*/


                  // Json
            
/* Es un formato que almacena información estructurada y se utiliza 
principalmente para transferir datos entre un servidor y un cliente */

/* Sintaxis Json: está constituido por dos estructuras:
    - Una colección de pares de nombre/valor (objeto);
    - Una lista ordenada de valores (arreglos, vectores, listas o sequencias);

Objetos: 
    - Las Keys deben ser cadenas de caractees;
    - Los values son un tipo de datos JSON válido, puede tener la forma
    de un arreglo, objeto, cadena, booleano, número o nulo
    
Un objeto Json comienza y termina con LLAVES {} pero puede tener dos o más
pares de claves/valor dentro con una coma para separarlos

Array: puede contener objetos Json

Métodos Json:
    Convertir Json a Objeto: esta acción se suele denominar parsear. Se analiza
        un string que contiene un Json válido y devuelve un objeto JavaScript con
        dicha información correctamente estructurada;
    Convertir Objeto a Json: se puede realizar fácilmente haciendo uso del
        método JSON.stringify() y se puede utilizar para transformar un objeto
        de javascript Json rápidamente;

Manejo de errores:
        try{
            throw "miExcepcion";
        } catch(e){
            logMyErrors(e);
        }

        function isValidJSON(text){
            try{
                JSON.parse(text);
                return true;
            } catch{
                return false; }}
*/

                  // Introducción a DOM

/* Se dota de potencia y flexibilidad a una página que nos da un lenguaje
de programaciónn para crear documentos y páginas mucho más ricas, que brinden
una experiencia más completa y con el que se puedan automatizar un gran 
abanico de tareas y acciones.
Por lo que DOM es una estructura en la que se pueden añadir en JS nuevas 
etiquetas, modificando eliminando otras, cambiando sus atributos, añadiendo
clases, cambiando el contenido del texto, etc.

Objeto Window, métodos:
    alert(texto): presenta una ventana de alerta donde se puede leer el texto
    back(): ve a una página atrás en el historial de páginas visitas
    captureEvents(eventos): captura los eventos que se indiquen por parámetro;
    close(): cierra la ventana;
    confirm(texto): muestra una ventana de confirmación y permite aceptar o rechazar
    find(): muestra una ventanilla de búsqueda;
    home(): va a la página de inicio que haya configurada
    promp(): muestra una caja de dialogo para pedir un dato
    setInterval(): define un script que  sea indefinidamente en casa intervalo
    setTimeOut(): define un scrpt para que se ejecute luego de un tiempo deter
    clearInterval(): elimina la ejecución de sentencias asociadas a un intervalo
        del metodo setInterval()
    cleatTimeOut() :elimina la ejecución de sentencias asociadas a un intervalo
        del metodo setTimeOut()

Objeto Document: para acceder se necesita un objeto llamado document que
representa el árbol DOM de la página o pestaña del navegador donde nos encontramos
Hay dos tipos distintos de elementos:
    - Element siendo la representación genérica de una etiqueta: HTMLElement
    - Node: pude ser Element o un nodo de texto

Seleccionar elementos del DOM: si se quiere modificar un elemento de la página
HTML se tiene que buscar dicho elemento identificandolo con los atributos de id
o la clase.

Métodos tradicionales: permiten devolver un array donde se podrá elegir el
elemento en cuestión.
    Estos prmiten buscar elementos en la página dependiendo de los atributos id,
clss, name o de la propia etiqueta
    .getElementsById(id): busca el elemento HTML con el id, sino devuelve null.
    En un documento HTML no debería haber más de un elemento con un mismo id, por
    lo que siempre devolverá un solo elemento
        const page = document.getElementsById("page");
    .getElementsByClassName(class): busca elementos con la clase class
    
    .getElementsByName(name): busca elementos con el atributo name
    .getElementsByTagName(tag): cierra la ventana


    


*/



