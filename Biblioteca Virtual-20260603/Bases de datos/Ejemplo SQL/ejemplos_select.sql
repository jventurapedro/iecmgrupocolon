

drop database if exist coches;

create database coches character set latin1 collate latin1_spanish_ci;

use coches;

create table datos (marca varchar(10), modelo varchar(10), anyo varchar(4), color varchar(10), matricula varchar(7) PRIMARY KEY);

insert into datos values ("Suzuki","Jimny", "2020", "Gris","0547NHB");

LOAD DATA INFILE 'C:/proyectos/base_coches.csv' INTO TABLE datos
		FIELDS TERMINATED BY  '\t'			/* separador de campos	*/
		LINES TERMINATED BY '\n'			/* separador de filas	*/


select * from datos /* Muestra un listado de toda la tabla */

    /* Mostrar un listado parcial filtrando por año */

select marca, modelo from datos where anyo="2008" 

    /* Mostrar un listado parcial filtrando por año y color */

select marca, modelo from datos where anyo="2008" and color="Rojo"

    /* Mostrar un listado parcial filtrando por inicio */

select marca, modelo from datos where color="R%" 

    /* Mostrar un listado parcial ordenando por año */

select marca, modelo from datos order by anyo





