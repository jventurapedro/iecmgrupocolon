

drop database if exists coches;

create database coches character set latin1 collate latin1_spanish_ci;

use coches;

create table datos (marca varchar(10), modelo varchar(10), anyo varchar(4), color varchar(10), matricula varchar(7) PRIMARY KEY);

insert into datos values ("Suzuki","Jimny", "2020", "Gris","0547NHB");

LOAD DATA INFILE 'C:/proyectos/base_coches.csv' INTO TABLE datos
		FIELDS TERMINATED BY  '\t'			/* separador de campos	*/
		LINES TERMINATED BY '\n'			/* separador de filas	*/




