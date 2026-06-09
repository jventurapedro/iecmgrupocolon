

drop database if exists ejercicio17;

create database ejercicio17 character set latin1 collate latin1_spanish_ci;

use ejercicio17;

create table datos (codigo varchar(6) PRIMARY KEY, empresa varchar(40), direccion varchar(40), poblacion varchar(15), estatus varchar(10), facturacion float());

LOAD DATA INFILE 'C:/ejemplos/ejercicio_17/ejercicio17.csv' INTO TABLE datos
		FIELDS TERMINATED BY  ';'			/* separador de campos	*/
		LINES TERMINATED BY '\n'			/* separador de filas	*/




