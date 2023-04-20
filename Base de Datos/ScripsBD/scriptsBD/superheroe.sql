DROP DATABASE IF EXISTS superheroe;
CREATE DATABASE superheroe CHARACTER SET utf8mb4;
USE superheroe;

CREATE TABLE creador (
  id_creador INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
  nombre VARCHAR(20) NOT NULL
);


CREATE TABLE personaje (
  id_personaje INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre_real VARCHAR(20) NOT NULL,
  personaje VARCHAR(20) NOT NULL,
  inteligencia INT(10) NOT NULL,
  fuerza VARCHAR(10) NOT NULL,
  velocidad INT(11) NOT NULL,
  poder INT(11) NOT NULL,
  aparicion INT(11) NOT NULL,
  ocupacion VARCHAR(30) NULL,
  id_creador INT UNSIGNED NOT NULL,
  FOREIGN KEY (id_creador) REFERENCES creador(id_creador)
);

INSERT INTO creador (nombre) VALUE ('Marvel');
INSERT INTO creador (nombre) VALUE ('DC Comics');
select * FROM creador;

INSERT INTO personaje (nombre_real, personaje, inteligencia, fuerza, velocidad, poder, aparicion, ocupacion, id_creador) VALUE ('Bruce Banner', 'Hulk', 160, '600 mil', 75, 98, 1962, 'Fisico Nuclear', 1);
INSERT INTO personaje (nombre_real, personaje, inteligencia, fuerza, velocidad, poder, aparicion, ocupacion, id_creador) VALUE ('Tony Stark', 'Iron Man', 170, '200 mil', 70, 123, 1963, 'Inventor Industrial', 1);
INSERT INTO personaje (nombre_real, personaje, inteligencia, fuerza, velocidad, poder, aparicion, ocupacion, id_creador) VALUE ('Thor Odinson', 'Thor', 145, 'infinita', 100, 235, 1962, 'Rey de Asgard', 1);
INSERT INTO personaje (nombre_real, personaje, inteligencia, fuerza, velocidad, poder, aparicion, ocupacion, id_creador) VALUE ('Wanda Maximoff', 'Bruja Escarlata', 170, '100 mil', 90, 345, 1964, 'Bruja', 1);
INSERT INTO personaje (nombre_real, personaje, inteligencia, fuerza, velocidad, poder, aparicion, ocupacion, id_creador) VALUE ('Carol Danvers', 'Capitana Marvel', 157, '250 mil', 85, 128, 1968, 'Oficial de inteligencia', 1);
INSERT INTO personaje (nombre_real, personaje, inteligencia, fuerza, velocidad, poder, aparicion, ocupacion, id_creador) VALUE ('Thanos', 'Thanos', 170, 'infinita', 40, 306, 1973, 'Adorador de la muerte', 1);
INSERT INTO personaje (nombre_real, personaje, inteligencia, fuerza, velocidad, poder, aparicion, ocupacion, id_creador) VALUE ('Peter Parker', 'Spider Man', 165, '25 mil', 80, 74, 1962, 'Fotógrafo', 1);
INSERT INTO personaje (nombre_real, personaje, inteligencia, fuerza, velocidad, poder, aparicion, ocupacion, id_creador) VALUE ('Steve Rogers', 'Capitan America', 145, 600, 45, 60, 1941, 'Oficial Federal', 1);
INSERT INTO personaje (nombre_real, personaje, inteligencia, fuerza, velocidad, poder, aparicion, ocupacion, id_creador) VALUE ('Bobby Drake', 'Ice Man', 140, '2 mil', 64, 122, 1963, 'Contador', 1);
INSERT INTO personaje (nombre_real, personaje, inteligencia, fuerza, velocidad, poder, aparicion, ocupacion, id_creador) VALUE ('Barry Allen', 'Flash', 160, '10 mil', 120, 168, 1956, 'Cientifico Foerence', 2);
INSERT INTO personaje (nombre_real, personaje, inteligencia, fuerza, velocidad, poder, aparicion, ocupacion, id_creador) VALUE ('Bruce Wayne', 'Batman', 170, 500, 32, 47, 1939, 'Hombre de negocios', 2);
INSERT INTO personaje (nombre_real, personaje, inteligencia, fuerza, velocidad, poder, aparicion, ocupacion, id_creador) VALUE ('Clark Kent', 'Superman', 166, 'infinita', 120, 182, 1948, 'Reportero', 1);
INSERT INTO personaje (nombre_real, personaje, inteligencia, fuerza, velocidad, poder, aparicion, ocupacion, id_creador) VALUE ('Diana Prince', 'Mujer Maravilla', 160, 'infinita', 95, 127,1949, 'Princesa guerrera', 2);

select * From personaje;

UPDATE personaje SET id_creador = 2 where id_personaje = 11;

UPDATE personaje SET aparicion = 1938 where id_personaje = 11;

select * From personaje;

DELETE FROM personaje where id_personaje = 9;

/*
CONSULTAS PARA ACCEDER Y MANIPULAR INFORMACIÓN
**/

-- 1. SELECT 
SELECT personaje, id_creador FROM personaje;
select * From personaje;
select nombre_real from personaje;
SELECT nombre_real, (inteligencia + velocidad) FROM personaje;

	-- CLAUSULAS DE SELECT:
	-- 1. SELECT DISTINCT:
SELECT DISTINCT personaje, poder FROM personaje;
	-- 2. WHERE
SELECT personaje, inteligencia FROM personaje WHERE inteligencia = 170;
		-- OPERADORES RACIONALES 
			-- MAYOR QUE: 
SELECT * FROM personaje WHERE aparicion > 1960;
			-- MENOR QUE:
SELECT  * FROM personaje WHERE aparicion < 1960;
			-- IGUAL QUE:
SELECT * FROM personaje WHERE aparicion = 1962;
			-- MAYOR O IGUAL QUE:
SELECT * FROM personaje WHERE fuerza >= '600 mil';
			-- MENOR O IGUAL QUE:
SELECT * FROM personaje WHERE fuerza <= '600 mil';
			-- DISTINTO QUE
SELECT * FROM personaje WHERE fuerza <> '600 mil';
		-- OPERADORES LÓGICOS
			-- AND
SELECT * FROM personaje WHERE inteligencia = 170 AND inteligencia = 175;
			-- OR
SELECT * FROM personaje WHERE inteligencia = 170 OR inteligencia = 175;
			-- NOT
SELECT * FROM personaje WHERE NOT inteligencia = 170;
		-- OPERADORES PROPIOS SQL
			-- BETWEEN
SELECT * FROM personaje WHERE inteligencia BETWEEN 160 AND 170;
			-- IN
SELECT * FROM personaje WHERE aparicion IN (1962, 1963, 1964);
			-- LIKE
				-- CUALQUIERO NOMBRE QUE EMPIECE CON...
select * from personaje where nombre_real like 'B%';
				-- CUALQUIER NOMBRE QUE TERMINE CON...
SELECT * FROM personaje WHERE nombre_real like '%e';
				-- CUALQUIER NOMBRE QUE TENGA ... EN CUALQUIER POSICION
SELECT * FROM personaje WHERE nombre_real like '%an%';
				-- CUALQUIER NOMBRE QUE TENGA ... EN SEGUNDA POSICION
SELECT * FROM personaje WHERE nombre_real like '_a%';
				-- CUALQUIER NOMBRE QUE EMPIECE CON ... Y TENGA AL MENOS 2 DE LARGO
SELECT * FROM personaje WHERE nombre_real like 'c_%';
				-- CUALQUIER NOMBRE QUE EMPIECE CON ... Y TENGA AL MENOS 3 DE LARGO
SELECT * FROM personaje WHERE nombre_real like 't__%';
				-- CUALQUIER NOMBRE QUE EMPIECE CON ... Y TERMINE CON ...
SELECT * FROM personaje WHERE nombre_real like 'b%n%';

	-- 3. ORDER BY
		-- DESCENDENTE
select * from personaje order by inteligencia desc;
		-- ASCENDENTE
select * from personaje order by nombre_real asc;

	-- 4. GROUP BY
		-- MAX
SELECT MAX(fuerza) FROM personaje;
		-- MIN
SELECT MIN(aparicion) FROM personaje;
		-- AVG
SELECT AVG(inteligencia) FROM personaje;
		-- COUNT
SELECT COUNT(*) FROM personaje;

	-- 5. HAVING
SELECT  nombre_real, inteligencia FROM personaje GROUP BY inteligencia HAVING inteligencia > 50 ;

	-- 6. AS
SELECT personaje AS nombre_personaje FROM personaje;

	-- 7. ROUND
SELECT ROUND(AVG(inteligencia)) FROM personaje;

	-- 8. LIMIT
SELECT nombre_real FROM personaje LIMIT 5;

-- CONSULTAS MULTITABLAS
	-- 1. INNER JOIN
SELECT nombre, personaje FROM creador INNER JOIN personaje ON creador.id_creador = personaje.id_creador;
	-- 2. LEFT JOIN
SELECT nombre, personaje FROM creador LEFT JOIN personaje ON creador.id_creador = personaje.id_creador;
	-- 3. RIGHT JOIN
SELECT nombre, personaje FROM creador RIGHT JOIN personaje ON creador.id_creador = personaje.id_creador;
		
-- SUBCONSULTAS
-- ERROR SINTAXIS (? : SELECT nombre_real, inteligencia FROM personaje WHERE > (SELECT AVG(inteligencia) FROM personaje);

	-- CON DOS CONSULTAS DE POR MEDIO
SELECT AVG(poder) "poder medio" FROM personaje;
SELECT nombre_real, poder FROM personaje WHERE poder > 157.75;

	-- CON UNA SUBCONSULTA 
SELECT nombre_real, poder FROM personaje WHERE poder > (SELECT AVG(poder) FROM personaje);



