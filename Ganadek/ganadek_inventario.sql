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
-- Table structure for table `inventario`
--

DROP TABLE IF EXISTS `inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventario` (
  `idInventario` int NOT NULL AUTO_INCREMENT,
  `idFinca` int DEFAULT NULL,
  `tipoItem` varchar(100) DEFAULT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `unidadMedida` varchar(50) DEFAULT NULL,
  `cantidad` float DEFAULT NULL,
  `fechaUltimaActualizacion` date DEFAULT NULL,
  PRIMARY KEY (`idInventario`),
  KEY `idFinca` (`idFinca`),
  CONSTRAINT `inventario_ibfk_1` FOREIGN KEY (`idFinca`) REFERENCES `finca` (`idFinca`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventario`
--

LOCK TABLES `inventario` WRITE;
/*!40000 ALTER TABLE `inventario` DISABLE KEYS */;
INSERT INTO `inventario` VALUES (1,1,'Alimento','Concentrado','kg',1000,'2024-10-29'),(2,1,'Medicina','Antibiótico','ml',500,'2024-10-29'),(3,2,'Alimento','Sal mineralizada','kg',500,'2024-10-29'),(4,2,'Medicina','Desparasitante','ml',1000,'2024-10-29'),(5,1,'Herramienta','Cercas eléctricas','metros',2000,'2024-10-29'),(6,1,'Medicina','Vitaminas','ml',750,'2024-10-29'),(7,2,'Alimento','Melaza','kg',300,'2024-10-29'),(8,2,'Herramienta','Bebederos','unidad',15,'2024-10-29'),(9,1,'Medicina','Vacunas','dosis',100,'2024-10-29');
/*!40000 ALTER TABLE `inventario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-13 11:46:49
