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
-- Table structure for table `registroproduccion`
--

DROP TABLE IF EXISTS `registroproduccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registroproduccion` (
  `idProduccion` int NOT NULL AUTO_INCREMENT,
  `idAnimal` int DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `tipoProducto` varchar(100) DEFAULT NULL,
  `cantidad` float DEFAULT NULL,
  `observaciones` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idProduccion`),
  KEY `idAnimal` (`idAnimal`),
  CONSTRAINT `registroproduccion_ibfk_1` FOREIGN KEY (`idAnimal`) REFERENCES `animali` (`idAnimal`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registroproduccion`
--

LOCK TABLES `registroproduccion` WRITE;
/*!40000 ALTER TABLE `registroproduccion` DISABLE KEYS */;
INSERT INTO `registroproduccion` VALUES (1,1,'2024-10-29','Leche',25.5,'Ordeño matutino'),(2,1,'2024-10-29','Leche',20.3,'Ordeño vespertino'),(3,4,'2024-10-29','Leche',22.5,'Ordeño matutino'),(4,6,'2024-10-29','Leche',18.3,'Ordeño vespertino'),(5,7,'2024-10-29','Leche',24,'Ordeño matutino'),(6,9,'2024-10-29','Leche',21.5,'Ordeño vespertino'),(7,10,'2024-10-29','Leche',19.8,'Ordeño matutino'),(8,4,'2024-10-28','Leche',23,'Ordeño matutino'),(9,6,'2024-10-28','Leche',17.5,'Ordeño vespertino');
/*!40000 ALTER TABLE `registroproduccion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-13 11:46:50
