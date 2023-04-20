DROP DATABASE IF EXISTS personal;
CREATE DATABASE personal CHARACTER SET utf8mb4;
USE personal;

CREATE TABLE departamento (
  id_depto INT AUTO_INCREMENT PRIMARY KEY, 
  nombre_depto VARCHAR(20) NOT NULL,
  ciudad VARCHAR(15) NULL,
  codigo_director VARCHAR(12) NULL
);


CREATE TABLE empleado (
  id_empleado INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre CHAR(30) NOT NULL,
  sexo_empleado CHAR(1) NOT NULL,
  fecha_nacimiento DATE NOT NULL,
  fecha_incorporacion DATE NOT NULL,
  salario FLOAT NOT NULL,
  comision FLOAT NOT NULL,
  cargo VARCHAR(15) NOT NULL,
  cod_jefe VARCHAR(12) NULL,  
	id_depto INT UNSIGNED NOT NULL,
  FOREIGN KEY (id_depto) REFERENCES departamento(id_depto)
  );


-- Insertar datos en la tabla `departamento`

INSERT INTO `departamento` VALUES (1000,'GERENCIA','CIUDAD REAL','31.840.269');
INSERT INTO `departamento` VALUES (1500,'PRODUCCIÓN','CIUDAD REAL','16.211.383');
INSERT INTO `departamento` VALUES (2000,'VENTAS','CIUDAD REAL','31.178.144');
INSERT INTO `departamento` VALUES (2100,'VENTAS','BARCELONA','16.211.383');
INSERT INTO `departamento` VALUES (2200,'VENTAS','VALENCIA','16.211.383');
INSERT INTO `departamento` VALUES (2300,'VENTAS','MADRID','16.759.060');
INSERT INTO `departamento` VALUES (3000,'INVESTIGACIÓN','CIUDAD REAL','16.759.060');
INSERT INTO `departamento` VALUES (3500,'MERCADEO','CIUDAD REAL','22.222.222');
INSERT INTO `departamento` VALUES (4000,'MANTENIMIENTO','CIUDAD REAL','333.333.333');
INSERT INTO `departamento` VALUES (4100,'MANTENIMIENTO','BARCELONA','16.759.060');
INSERT INTO `departamento` VALUES (4200,'MANTENIMIENTO','VALENCIA','16.759.060');
INSERT INTO `departamento` VALUES (4300,'MANTENIMIENTO','MADRID','16.759.060');

-- Insertar datos en la tabla `empleado`

INSERT INTO `empleado` VALUES (222,'José Giraldo','M','1985-01-20','2000-11-01',1200000,400000,'Asesor','22.222.222',3500);
INSERT INTO `empleado` VALUES (333,'Pedro Blanco','M','1987-10-28','2000-10-01',800000,3000000,'Vendedor','31.178.144',2000);
INSERT INTO `empleado` VALUES (444,'Jesús Alfonso','M','1988-03-14','2000-10-01',800000,3500000,'Vendedor','31.178.144',2000);
INSERT INTO `empleado` VALUES (555,'Julián Mora','M','1989-07-03','2000-10-01',800000,3100000,'Vendedor','31.178.144',2200);
INSERT INTO `empleado` VALUES (666,'Manuel Millán','M','1990-12-08','2004-06-01',800000,3700000,'Vendedor','31.178.144',2300);
INSERT INTO `empleado` VALUES (777,'Marcos Cortez','M','1986-06-23','2000-04-16',2550000,500000,'Mecánico','333.333.333',4000);
INSERT INTO `empleado` VALUES (782,'Antonio Gil','M','1980-01-23','2010-04-16',850000,1500000,'Técnico','16.211.383',1500);
INSERT INTO `empleado` VALUES (219,'Melissa Roa','F','1960-06-19','2001-03-16',2250000,2500000,'Vendedor','31.178.144',2100);
INSERT INTO `empleado` VALUES (111,'Irene Díaz','F','1979-09-28','2004-06-01',1050000,200000,'Mecánico','333.333.333',4200);
INSERT INTO `empleado` VALUES (383,'Luis Pérez','M','1956-02-25','2000-01-01',5050000,0,'Director','31.840.269',1500);
INSERT INTO `empleado` VALUES (060,'Darío Casas','M','1960-04-05','1992-11-01',4500000,500000,'Investigador','31.840.269',3000);
INSERT INTO `empleado` VALUES (802,'William Daza','M','1982-10-09','1999-12-16',2250000,1000000,'Investigador','16.759.060',3000);
INSERT INTO `empleado` VALUES (221,'Carla López','F','1975-05-11','2005-07-16',4500000,500000,'Jefe Mercadeo','31.840.269',3500);
INSERT INTO `empleado` VALUES (331,'Carlos Rozo','M','1975-05-11','2001-09-16',750000,500000,'Vigilante','31.840.269',3500);
INSERT INTO `empleado` VALUES (099,'Diana Solarte','F','1957-11-19','1990-05-16',1250000,500000,'Secretaria','31.840.269',1000);
INSERT INTO `empleado` VALUES (144,'Rosa Angulo','F','1957-03-15','1998-08-16',3250000,3500000,'Jefe Ventas','31.840.269',2000);
INSERT INTO `empleado` VALUES (269,'María Rojas','F','1959-01-15','1990-05-16',6250000,1500000,'Gerente',NULL,1000);
INSERT INTO `empleado` VALUES (343,'Elisa Rojas','F','1979-09-28','2004-06-01',3000000,1000000,'Jefe Mecánicos','31.840.269',4000);
INSERT INTO `empleado` VALUES (334,'Marisol Pulido','F','1979-10-01','1990-05-16',3250000,1000000,'Investigador','16.759.060',3000);
INSERT INTO `empleado` VALUES (335,'Ana Moreno','F','1992-01-05','2004-06-01',1200000,400000,'Secretaria','16.759.060',3000);
INSERT INTO `empleado` VALUES (336,'Carolina Ríos','F','1992-02-15','2000-10-01',1250000,500000,'Secretaria','16.211.383',1500);
INSERT INTO `empleado` VALUES (337,'Edith Muñoz','F','1992-03-31','2000-10-01',800000,3600000,'Vendedor','31.178.144',2100);
INSERT INTO `empleado` VALUES (338,'Abel Gómez','M','1939-12-24','2000-10-01',1050000,200000,'Mecánico','333.333.333',4300);
INSERT INTO `empleado` VALUES (689,'Mario Llano','M','1945-08-30','1990-05-16',2250000,2500000,'Vendedor','31.178.144',2300);
INSERT INTO `empleado` VALUES (785,'Joaquín Rosas','M','1947-07-07','1990-05-16',2250000,2500000,'Vendedor','31.178.144',2200);
INSERT INTO `empleado` VALUES (898,'Iván Duarte','M','1955-08-12','1998-05-16',1050000,200000,'Mecánico','333.333.333',4100);

-- Punto a) Consultas sobre la base de datos PERSONAL:
-- 1. Obtener los DATOS COMPLETOS de los EMPLEADOS
SELECT * FROM empleado;

-- 2. Obtener los DATOS COMPLETOS de los DEPARTAMENTOS
SELECT * FROM departamento;

-- 3. Listar el NOMBRE de los DEPARTAMENTOS
SELECT nombre_depto FROM departamento GROUP BY nombre_depto;

-- 4. Obtener el NOMBRE y el SALARIO de TODOS los EMPLEADOS
SELECT nombre, salario FROM empleado;

-- 5. Listar TODAS las COMISIONES
SELECT comision FROM empleado;

-- 6. Obtener los datos de los EMPLEADOS cuyo CARGO sea "Secretaria"
SELECT * FROM empleado WHERE cargo = "Secretaria";

-- 7. Obtener los datos de los EMPLEADOS VENDEDORES, ordenados por NOMBRE ALFABETICAMENTE
SELECT * FROM empleado WHERE cargo = "Vendedor" ORDER BY nombre ASC;

-- 8. Obtener NOMBRE y CARGO de todos los EMPLEADOS, ORDENADOS por SALARIO de MENOR A MAYOR
SELECT nombre, cargo, salario FROM empleado ORDER BY salario ASC;

-- 9. Elabore un LISTADO donde cada fila figura 'NOMBRE' y 'CARGO' para las RESPECTIVAS TABLAS DE EMPLEADOS
SELECT nombre AS 'Nombre', cargo AS 'Cargo' FROM empleado;

-- 10. Listar los SALARIOS y COMISIONES de los EMPLEADOS  del DEPARTAMENTO 2000, ordenado por comisión de menor a mayor
SELECT salario, comision FROM empleado WHERE id_depto = 2000 ORDER BY comision ASC;

-- 11. Obtener el VALOR TOTAL A PAGAR que resulta de SUMAR el SALARIO y la COMISION de los empleados del dto 3000 una BONIFICACION DE 500, en orden ALFABETICO del EMPLEADO
SELECT (salario + comision + 500) AS 'VALOR TOTAL A PAGAR'  FROM empleado ORDER BY nombre ASC;

-- 12. Muesta los empleados cuyo NOMBRE EMPIECE por la LETRA J
SELECT * FROM empleado WHERE nombre LIKE 'j%';

 /*
 13. Listar el SALARIO, la COMISION, el SALARIO TOTAL (salario + comision) y NOMBRE,
 de aquellos empleados que tengan COMISION SUPERIOR A 1000
*/

SELECT salario, comision, (salario + comision) AS 'SALARIO TOTAL', nombre FROM empleado WHERE comision > 1000;

-- 14. Obtener un listado SIMILAR AL ANTERIOR, pero de aquellos EMPLEADOS que NO tienen COMISION
SELECT salario AS 'Salario', comision AS 'Comision', (salario  + comision) AS 'Salario Total', nombre AS 'Nombre' from empleado WHERE NOT comision;

-- 15. Obtener la lista de los EMPLEADOS que ganan una COMISION SUPERIOR a su SUELDO
SELECT * FROM empleado WHERE comision > salario;

-- 16. Lista los EMPLEADOS cuya COMISION es MENOR O IGUAL al 30% de su SUELDO
SELECT * FROM empleado WHERE comision <= (salario * 0.30);

-- 17. Hallar los EMPLEADOS cuyo NOMBRE NO contiene la cadena "MA"
Select * FROM empleado WHERE nombre NOT LIKE '%ma%';

-- 18. Obtner los NOMBRES de los DEPARTAMENTOS que sean "VENTAS", "INVESTIGACION", "MANTENIMIENTO"
SELECT nombre_depto FROM departamento WHERE nombre_depto = "Ventas" OR nombre_depto = "Investigacion" OR nombre_depto = "Mantenimiento";

-- 19. Obtner los NOMBRES de los DEPARTAMENTOS que NO sean "VENTAS", NI "INVESTIGACION", NI "MANTENIMIENTO"
SELECT nombre_depto FROM departamento WHERE nombre_depto <> "Ventas" AND nombre_depto <> "Investigacion" AND nombre_depto <> "Mantenimiento";

-- 20. Mostrar el SALARIO MÁS ALTO de la EMPRESA
SELECT MAX(salario) AS 'Salario más alto de la empresa' FROM empleado;

-- 21. Mostrar el NOMBRE del ULTIMO EMPLEADO de la lista por orden alfabético
SELECT nombre AS 'Ultimo empleado de la lista' FROM empleado ORDER BY nombre DESC LIMIT 1;

-- 22. Hallar el SALARIO MÁS ALTO, el MÁS BAJO y la DIFERENCIA entre AMBOS;
SELECT MAX(salario) AS 'Salario más alto', MIN(salario) AS 'Salario más bajo', (MAX(salario) - MIN(salario)) AS 'Diferencia de salarios' FROM empleado;

-- 23. Hallar el SALARIO PROMEDIO POR DEPARTAMENTO
SELECT id_depto AS 'Departamento', ROUND(AVG(salario)) as 'Salario promedio por departamento' FROM empleado GROUP BY id_depto;

-- CONSULTAS CON HAVING

-- 24. Hallar los DEPARTAMENTOS que TIENEN más de 3 EMPLEADOS. MOSTRAR el NUMERO de empleados de ESE departamento
SELECT COUNT(id_empleado) AS 'Cantidad empleados', id_depto AS 'Departamentos' FROM empleado GROUP BY id_depto HAVING COUNT(id_empleado) > 3 ;

-- 25. Mostrar el CODIGO y NOMBRE de CADA JEFE, junto al NUMERO de EMPLEADOS que DIRIGE, SOLO los que TENGAN 2 O MÁS EMPLEADOS 
SELECT cod_jefe, COUNT(cod_jefe) "Empleados a Cargo " FROM empleado GROUP BY cod_jefe HAVING count(cod_jefe) >=2;

-- 26. Hallar los DEPARTAMENTOS que NO tienen Empleados
SELECT id_depto AS 'DEPARTAMENTO', COUNT(id_empleado) AS 'Cantidad empleados' FROM empleado HAVING COUNT(id_empleado) = NULL;

-- 27. Mostrar la lista de los EMPLEADOS cuyo SALARIO es MAYOR O IGUAL que el PROMEDIO de la empresa. Ordenarlo por DEPARTAMENTO
SELECT 
    *
FROM
    empleado
WHERE
    salario >= (SELECT 
            AVG(salario)
        FROM
            empleado)
ORDER BY id_depto ASC;
