DROP DATABASE IF EXISTS connections;
CREATE DATABASE connections;
USE connections;

CREATE TABLE tabla1 (
nombre VARCHAR(100)
);

INSERT INTO tabla1 VALUES ('Noelia');

SELECT * FROM tabla1;