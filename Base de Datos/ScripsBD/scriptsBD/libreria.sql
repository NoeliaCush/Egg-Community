-- 1) Crear la base de datos libreria
CREATE DATABASE IF NOT EXISTS libreria;

#seleccionar la base de datos
USE libreria;
SELECT * FROM autor;

SELECT * FROM libro;

SELECT * FROM editorial;


-- listaAutores = em.createQuery("Select a from Autor a").getResultList();
