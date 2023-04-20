DROP DATABASE IF EXISTS tienda;
CREATE DATABASE tienda CHARACTER SET utf8mb4;
USE tienda;

CREATE TABLE fabricante (
  codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL
);

CREATE TABLE producto (
  codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  precio DOUBLE NOT NULL,
  codigo_fabricante INT UNSIGNED NOT NULL,
  FOREIGN KEY (codigo_fabricante) REFERENCES fabricante(codigo)
);

INSERT INTO fabricante VALUES(1, 'Asus');
INSERT INTO fabricante VALUES(2, 'Lenovo');
INSERT INTO fabricante VALUES(3, 'Hewlett-Packard');
INSERT INTO fabricante VALUES(4, 'Samsung');
INSERT INTO fabricante VALUES(5, 'Seagate');
INSERT INTO fabricante VALUES(6, 'Crucial');
INSERT INTO fabricante VALUES(7, 'Gigabyte');
INSERT INTO fabricante VALUES(8, 'Huawei');
INSERT INTO fabricante VALUES(9, 'Xiaomi');

INSERT INTO producto VALUES(1, 'Disco duro SATA3 1TB', 86.99, 5);
INSERT INTO producto VALUES(2, 'Memoria RAM DDR4 8GB', 120, 6);
INSERT INTO producto VALUES(3, 'Disco SSD 1 TB', 150.99, 4);
INSERT INTO producto VALUES(4, 'GeForce GTX 1050Ti', 185, 7);
INSERT INTO producto VALUES(5, 'GeForce GTX 1080 Xtreme', 755, 6);
INSERT INTO producto VALUES(6, 'Monitor 24 LED Full HD', 202, 1);
INSERT INTO producto VALUES(7, 'Monitor 27 LED Full HD', 245.99, 1);
INSERT INTO producto VALUES(8, 'Portátil Yoga 520', 559, 2);
INSERT INTO producto VALUES(9, 'Portátil Ideapd 320', 444, 2);
INSERT INTO producto VALUES(10, 'Impresora HP Deskjet 3720', 59.99, 3);
INSERT INTO producto VALUES(11, 'Impresora HP Laserjet Pro M26nw', 180, 3);

-- CONSULTAS SOBRE LA BASE DE DATOS
-- 1. Lista de NOMBRE de TODOS los produtos que hay en la tabla PRODUCTO
SELECT 
    nombre AS 'Producto'
FROM
    producto;

-- 2. Lista de los NOMBRES y los PRECIOS de la tabla PRODUCTO
SELECT 
    nombre, precio
FROM
    producto;

-- 3. Lista TODAS las COLUMNAS de la tabla PRODUCTO
SHOW COLUMNS FROM producto;

-- 4. Lista de los NOMBRES y los PRECIOS de TODOS los PRODUCTOS de la tabla PRODUCTO, REDONDEANDO el valor del PRECIO
SELECT 
    nombre, ROUND(precio)
FROM
    producto;

-- 5. Lista el CÓDIGO de los FABRICANTES que tienen PRODUCTOS en la tabla PRODUCTO
SELECT 
    codigo_fabricante
FROM
    producto;
 
-- 6. Lista el CÓDIGO de los FABRICANTES que tienen PRODUCTOS en la TABLA PRODUCTO, SIN MOSTRAR los repetivos
SELECT 
    codigo_fabricante, nombre AS 'Producto'
FROM
    producto
GROUP BY producto;

-- 7. Lista los NOMBRES de los fabricantes ORDENADOS de forma ASCENDENTE
SELECT 
    nombre AS 'Fabricante'
FROM
    fabricante
ORDER BY nombre ASC;

-- 8. Lista los NOMBRES de los PRODUCTOS en 1° LUGAR por el NOMBRE de forma ASC y en 2° LUGAR por el
-- PRECIO de forma DESC
SELECT 
    nombre AS 'Producto', precio AS 'Precio'
FROM
    producto
ORDER BY nombre ASC , precio DESC;

-- 9. Devulve una lista con las 5 PRIMERAS FILAS de la tabla FABRICANTE
SELECT 
    *
FROM
    producto
LIMIT 5;

-- 10. Lista el NOMBRE y el PRECIO del PRODUCTO MÁS BARATO
SELECT 
    nombre AS 'Producto', precio AS 'Precio'
FROM
    producto
ORDER BY precio ASC
LIMIT 1;

-- 11. Lista el NOMBRE y el PRECIO del PRODUCTO MÁS CARO
SELECT 
    nombre AS 'Producto', precio AS 'Precio'
FROM
    producto
ORDER BY precio DESC
LIMIT 1;

-- 12. Lista de NOMBRE de los PRODUCTOS que tienen un PRECIO MENOR O IGUAL A $120
SELECT 
    nombre AS 'Producto', precio
FROM
    producto
WHERE
    precio <= 120;

-- 13. Lista de los PRODUCTOS que tengan PRECIO ENTRE 60 Y 200. Utilizando el operador BETWEEN
SELECT 
    *
FROM
    producto
WHERE
    precio BETWEEN 60 AND 120;

-- 14.Lista TODOS los PRODUCTOS donde el CODIGO DEL FABRICANTE sea 1, 3 o 5 
SELECT 
    *
FROM
    producto
WHERE
    codigo_fabricante IN (1 , 3, 5);

-- 15. Devuelve una LISTA con el NOMBRE de TODOS los PRODUCTOS que CONTIENEN la CADENA PORTATIL en el nombre
SELECT 
    *
FROM
    producto
WHERE
    nombre LIKE '%portatil%';

-- CONSULTAS MULTITABLA

-- 1. Devuelve una lista con el CODIGO del PRODUCTO, NOMBRE del PRODUCTO, CODIGO del FABRICANTE y NOMBRE del FABRICANTE
SELECT 
    producto.codigo, producto.nombre, producto.codigo_fabricante, fabricante.nombre
FROM
    producto
        INNER JOIN
    fabricante ON producto.codigo_fabricante = fabricante.codigo;
    
-- 2. Devuelve una lista con el NOMBRE del producto, PRECIO y NOMBRE del FABRICANTE de TODOS los PRODUCTOS
-- de la base de datos. ORDENE el resultado por el NOMBRE del FABRICANTE, por ORDEN ALFABÉTICO
SELECT 
    producto.nombre, producto.precio, fabricante.nombre
FROM
    producto
        INNER JOIN
    fabricante ON producto.codigo_fabricante = fabricante.codigo
ORDER BY fabricante.nombre ASC;

-- 3. Devuelve el NOMBRE del PRODUCTO, su PRECIO y el NOMBRE de su FABRICANTE, del PRODUCTO MÁS BARATO
SELECT 
    producto.nombre as 'Producto', producto.precio AS 'Precio', fabricante.nombre 'Fabricante'
FROM
    producto
        INNER JOIN
    fabricante ON producto.codigo_fabricante = fabricante.codigo
ORDER BY precio ASC
LIMIT 1;

-- 4. Devuelve una lista de TODOS los PRODUCTOS del FABRICANTE LENOVO
SELECT 
    *
FROM
    producto
        INNER JOIN
    fabricante ON producto.codigo_fabricante = fabricante.codigo
WHERE
    fabricante.nombre LIKE '%lenovo%';

-- 5. Devuelve una lista de TODOS los PRODUCTOS del FABRICANTE CRUCIAL tengan un PRECIO MAYOR QUE 200
SELECT 
    *
FROM
    producto
        INNER JOIN
    fabricante ON producto.codigo_fabricante = fabricante.codigo
WHERE
    fabricante.nombre LIKE '%crucial%'
        AND precio > 200;

-- 6. Devuelv un listado con TODOS los productos de TODOS los fabricantes ASUS, HEWLETT-PACKHARD. Utilizando el operator IN
SELECT 
    *
FROM
    producto
        INNER JOIN
    fabricante ON producto.codigo_fabricante = fabricante.codigo
WHERE
    fabricante.nombre IN ('asus' , 'hewlett-packard');
    
-- 7. Devuelve el listado con el NOMBRE del PRODUCTO, PRECIO y NOMBRE del FABRICANTE, de TODOS los PRODUCTOS
-- que tengan un PRECIO MAYOR O IGUAL A 180. ORDENE el resultado en 1° LUGAR por el precio DESC y en 2° por el NOMBRE ASC
SELECT 
    producto.nombre AS 'Producto', producto.precio AS 'Precio', fabricante.nombre AS 'Fabricante'
FROM
    producto
        INNER JOIN
    fabricante ON producto.codigo_fabricante = fabricante.codigo
WHERE
    producto.precio >= 180
ORDER BY producto.precio DESC , producto.nombre ASC;

-- CONSULTAS MULTITABLA (UILIZANDO LEFT AND RIGHT JOIN)
/*
1. Devuelve un listado de TODOS los FABRICANTES que existen en la base de datos, JUNTO con los PRODUCTOS
que tiene CADA UNO de ellos. El listado deberá MOSTRAR también aquellos fabricantes que NO TIENEN PRODUCTOS
asociados.
*/
SELECT 
    *
FROM
    fabricante
        LEFT JOIN
    producto ON producto.codigo_fabricante = fabricante.codigo;

-- 2. Devuelve un listado dondo SOLO aparezcan aquellos FABRICANTES que NO TIENEN ningún producto asociado
SELECT 
    *
FROM
    fabricante
        LEFT JOIN
    producto ON producto.codigo_fabricante = fabricante.codigo
WHERE
    producto.nombre IS NULL;
    
-- SUBCONSULTAS Con operadores BASICOS de comparación

-- 1. Devuelve TODOS los productos del FABRICANTE LENOVO (SIN usar INNER JOIN)
SELECT 
    *
FROM
    producto
WHERE
    codigo_fabricante IN (SELECT 
            codigo
        FROM
            fabricante
        WHERE
            nombre LIKE 'Lenovo%'); 

-- 2. Devuelve TODOS los datos de los PRODUCTOS que tienen el MISMO PRECIO que el PRODUCTO MÁS CARO del fabricante LENOVO
SELECT 
    *
FROM
    producto
WHERE
    precio = (SELECT 
            producto.precio
        FROM
            producto,
            fabricante
        WHERE
            producto.codigo_fabricante = fabricante.codigo
                AND fabricante.nombre = 'lenovo'
        ORDER BY producto.precio DESC
        LIMIT 1);
        
-- 3. Lista el NOMBRE del producto MAS ccaro del FABRICANTE LENOVO

SELECT 
    producto.nombre, producto.precio
FROM
    producto,
    fabricante
WHERE
    producto.codigo_fabricante = fabricante.codigo
        AND fabricante.nombre = 'LENOVO'
ORDER BY producto.precio DESC
LIMIT 1;

-- 4. Lista los PRODUCTOS del fabricante ASUS que tienen un PRECIO SUPERIOR al precio medio de TODOS sus PRODUCTOS
SELECT 
    *
FROM
    fabricante,
    producto
WHERE
    fabricante.nombre = 'ASUS'
        AND producto.precio > (SELECT 
            AVG(producto.precio)
        FROM
            producto,
            fabricante
        WHERE
            producto.codigo_fabricante = fabricante.codigo
                AND fabricante.nombre = 'ASUS');
                
-- SUBCONSULTAS CON IN Y NOT IN

-- 1. Devuelve los NOMBRES de los FABRICANTES que tienen productos ASOCIADOS (UTILIZANDO un IN o un NOT IN)
SELECT 
    fabricante.nombre, producto.nombre
FROM
    fabricante,
    producto
WHERE
    producto.codigo_fabricante = fabricante.codigo
        AND producto.nombre IN (fabricante.nombre);
        
	









