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
-- Table structure for table `animal`
--

DROP TABLE IF EXISTS `animal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animal` (
  `idAnimal` int NOT NULL AUTO_INCREMENT,
  `idUnidad` int DEFAULT NULL,
  `especie` enum('Bovino','Porcino','Avícola','Otro') NOT NULL,
  `raza` varchar(100) DEFAULT NULL,
  `sexo` enum('Macho','Hembra','Desconocido') DEFAULT NULL,
  `peso` decimal(8,2) DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `idMadre` int DEFAULT NULL,
  `idPadre` int DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `estado` enum('Vivo','Muerto','Vendido','Sacrificado','Enfermo','Otro') DEFAULT NULL,
  PRIMARY KEY (`idAnimal`),
  KEY `idUnidad` (`idUnidad`),
  KEY `idMadre` (`idMadre`),
  KEY `idPadre` (`idPadre`),
  CONSTRAINT `animal_ibfk_1` FOREIGN KEY (`idUnidad`) REFERENCES `unidad_productiva` (`idUnidad`),
  CONSTRAINT `animal_ibfk_2` FOREIGN KEY (`idMadre`) REFERENCES `animal` (`idAnimal`),
  CONSTRAINT `animal_ibfk_3` FOREIGN KEY (`idPadre`) REFERENCES `animal` (`idAnimal`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animal`
--

LOCK TABLES `animal` WRITE;
/*!40000 ALTER TABLE `animal` DISABLE KEYS */;
INSERT INTO `animal` VALUES (1,1,'Bovino','Holstein','Hembra',520.50,'2020-04-15',NULL,NULL,'luna.jpg','Vivo'),(2,1,'Bovino','Holstein','Macho',85.00,'2024-03-20',1,NULL,'estrella.jpg','Vivo'),(3,3,'Porcino','Landrace','Hembra',200.00,'2022-06-01',NULL,NULL,'margarita.jpg','Vivo'),(4,3,'Porcino','Landrace','Macho',18.00,'2024-06-15',3,NULL,'lechon.jpg','Vivo');
/*!40000 ALTER TABLE `animal` ENABLE KEYS */;
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
