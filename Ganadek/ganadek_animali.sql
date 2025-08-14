-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ganadek
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `animali`
--

DROP TABLE IF EXISTS `animali`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animali` (
  `idAnimal` int NOT NULL,
  `idPotrero` int DEFAULT NULL,
  `especie` varchar(100) DEFAULT NULL,
  `raza` varchar(100) DEFAULT NULL,
  `sexo` varchar(50) DEFAULT NULL,
  `peso` varchar(50) DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `idMadre` int DEFAULT NULL,
  `idPadre` int DEFAULT NULL,
  `imagen` varchar(200) DEFAULT NULL,
  `estado` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idAnimal`),
  KEY `idPotrero` (`idPotrero`),
  KEY `idMadre` (`idMadre`),
  KEY `idPadre` (`idPadre`),
  CONSTRAINT `animali_ibfk_1` FOREIGN KEY (`idPotrero`) REFERENCES `potrero` (`idPotrero`),
  CONSTRAINT `animali_ibfk_2` FOREIGN KEY (`idMadre`) REFERENCES `madrei` (`idMadre`),
  CONSTRAINT `animali_ibfk_3` FOREIGN KEY (`idPadre`) REFERENCES `padrei` (`idPadre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animali`
--

LOCK TABLES `animali` WRITE;
/*!40000 ALTER TABLE `animali` DISABLE KEYS */;
INSERT INTO `animali` VALUES (1,1,'Bovino','Holstein','Hembra','450','2022-03-15',1,1,'vaca1.jpg','Activo'),(2,1,'Bovino','Holstein','Macho','500','2022-01-20',2,1,'toro1.jpg','Activo'),(3,2,'Bovino','Jersey','Hembra','400','2023-05-10',2,2,'vaca2.jpg','Activo'),(4,1,'Bovino','Brahman','Hembra','480','2022-06-20',3,3,'vaca3.jpg','Activo'),(5,2,'Bovino','Simmental','Macho','520','2022-08-15',4,4,'toro2.jpg','Activo'),(6,3,'Bovino','Charolais','Hembra','470','2023-01-10',5,5,'vaca4.jpg','Activo'),(7,1,'Bovino','Gyr','Hembra','430','2023-03-05',6,6,'vaca5.jpg','Activo'),(8,2,'Bovino','Normando','Macho','510','2023-04-12',7,7,'toro3.jpg','Activo'),(9,3,'Bovino','Pardo Suizo','Hembra','460','2023-07-20',8,8,'vaca6.jpg','Activo'),(10,1,'Bovino','Jersey','Hembra','420','2023-09-15',9,9,'vaca7.jpg','Activo');
/*!40000 ALTER TABLE `animali` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-13 11:46:51
