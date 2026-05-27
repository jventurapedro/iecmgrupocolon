-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: alumnosdb
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alumnos`
--

DROP TABLE IF EXISTS `alumnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alumnos` (
  `dni` varchar(9) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `direccion` varchar(40) DEFAULT NULL,
  `provincia` varchar(30) DEFAULT NULL,
  `telefono` varchar(9) DEFAULT NULL,
  `fecha_nacimiento` varchar(10) DEFAULT NULL,
  `fecha_alta` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`dni`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumnos`
--

LOCK TABLES `alumnos` WRITE;
/*!40000 ALTER TABLE `alumnos` DISABLE KEYS */;
INSERT INTO `alumnos` VALUES ('01245785F','Samuel Jurado',58,'Alborada, 12','Valencia','696546518','09/02/2000','\r'),('01254875K','Carlos Ruiz',49,'Eslovaquia, 12','Soria','669654146','03/11/2004','\r'),('02545875L','Juan Boadella',25,'Matadero, 34','Soria','953654544','08/07/2005','\r'),('02568424X','Jaime Lorenzo',14,'Ejercito, 27','Guadalajara','665845126','13/05/1996','23/06/2013'),('12451257F','Patricia Sanz',29,'Conseller, 2','Valencia','956546514','16/05/2007','\r'),('22569584E','Antonio Diaz',56,'Astorga, 12','Oviedo','986964565','06/12/1999','\r'),('32698542H','Jose Mariano',26,'Alpedrete, 1','Toledo','941654654','04/07/2008','\r'),('33652158F','Elvira Benart',37,'Plaza Real, 23','Soria','635645655','09/07/2010','\r'),('36236948T','Alicia Forner',32,'Moscu, 32','Toledo','942654694','03/05/1989','\r'),('36254147Z','Jorge Escribano',56,'Posada, 45','Teruel','604785324','24/05/1978','26/04/2010'),('36254256S','Camilo Beriyan',49,'Granadero, 56','Jaen','665416441','03/09/1998','\r'),('36452685S','Almudena Santos',24,'Ferrocarril, 2','Gijon','695191496','05/07/2003','\r'),('36995215Y','Javier Melero',75,'Laguna, 45','Malaga','667654654','09/04/1989','23/09/2009'),('39565875P','Ivanka Saries',19,'Martorell, 34','Soria','626544165','03/09/1995','\r'),('42654644M','Luis Gonzalez',24,'Pallarols, 67','Valencia','623165643','07/10/2008','\r'),('50149641W','Sergio Sanchez',41,'Puerta Sol, 12','Madrid','636584654','30/06/2010','\r'),('52125245D','Felix Aragones',65,'Usera, 56','Madrid','916546541','09/12/2001','\r'),('52362548A','Laura Rodriguez',32,'Calleja, 25','Madrid','916549684','25/02/1989','15/02/2007'),('52456854H','Sonia Lopez',24,'Cuesta, 56','Toledo','687654654','26/10/1999','08/01/2001'),('63325691K','Sofia Rosales',19,'Avd. Prado, 2','Salamanca','919645465','12/04/1978','15/08/2012'),('65467651E','Enrique Rubio',15,'La Estrella, 9','Madrid','636546544','05/09/2006','\r'),('65469395V','Rafael Mino',52,'Albarracin, 6','Jaen','953654647','09/04/2000','\r'),('65746454Q','Oscar Quintana',23,'Austrias, 45','Madrid','919832165','03/06/2011','\r'),('68476544T','Francisco Moles',82,'Cantabria, 34','Gijón','654611544','23/05/2009','\r'),('68769425O','Arancha Yuste',38,'Albufera, 3','Valencia','946519441','07/06/1994','\r'),('69352158D','Luisa Mercero',26,'Penarroya, 34','Madrid','916541565','03/09/1964','02/06/2000'),('69582364S','Pedro Martos',52,'Cadiz, 34','Soria','626544141','25/10/2006','\r'),('75623658G','Emilia Vazquez',35,'Benavides, 23','Soria','952654564','09/12/2008','\r'),('78542564A','Victor Alamo',56,'Mineria, 32','Oviedo','985546565','05/08/2011','\r'),('96265154P','Monica Santos',25,'Vinateros, 12','Madrid','916655285','23/07/2009','\r'),('y53064p','joao',NULL,NULL,NULL,'777777778',NULL,NULL),('y5350984p','joao',NULL,NULL,NULL,'898767878',NULL,NULL),('y5453062p','joao',NULL,NULL,NULL,'643567887',NULL,NULL),('y5453063p','joao',NULL,NULL,NULL,'643495466',NULL,NULL),('y5453064p','joao',NULL,NULL,NULL,'643495476',NULL,NULL),('y5453065p','joao',NULL,NULL,NULL,'643495477',NULL,NULL),('y5453067p','joao',NULL,NULL,NULL,'643495788',NULL,NULL),('y5453068p','joao',NULL,NULL,NULL,'643495888',NULL,NULL),('y5453069p','joao',NULL,NULL,NULL,'643495840',NULL,NULL);
/*!40000 ALTER TABLE `alumnos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-27 21:55:35
