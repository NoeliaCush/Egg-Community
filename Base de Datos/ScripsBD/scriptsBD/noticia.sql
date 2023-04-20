DROP DATABASE IF EXISTS noticia;
CREATE DATABASE noticia;

#seleccionar la base de datos
USE noticia;

CREATE TABLE portal (
  id INT AUTO_INCREMENT ,
  titulo VARCHAR(255),
  cuepo VARCHAR(255),
  PRIMARY KEY(id)
);