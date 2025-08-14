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
-- Table structure for table `alerta`
--

DROP TABLE IF EXISTS `alerta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alerta` (
  `idAlerta` int NOT NULL AUTO_INCREMENT,
  `idFinca` int DEFAULT NULL,
  `tipoAlerta` varchar(100) DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  `fechaCreacion` date DEFAULT NULL,
  `fechaLimite` date DEFAULT NULL,
  `estado` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idAlerta`),
  KEY `idFinca` (`idFinca`),
  CONSTRAINT `alerta_ibfk_1` FOREIGN KEY (`idFinca`) REFERENCES `finca` (`idFinca`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alerta`
--

LOCK TABLES `alerta` WRITE;
/*!40000 ALTER TABLE `alerta` DISABLE KEYS */;
INSERT INTO `alerta` VALUES (1,1,'Vacunación','Vacunación contra la aftosa','2024-10-29','2024-11-15','Pendiente'),(2,1,'Mantenimiento','Mantenimiento de cercas','2024-10-29','2024-11-10','En proceso'),(3,2,'Desparasitación','Desparasitación general del ganado','2024-10-29','2024-11-20','Pendiente'),(4,2,'Mantenimiento','Revisión de bebederos','2024-10-29','2024-11-05','En proceso'),(5,1,'Reproducción','Chequeo de vacas inseminadas','2024-10-29','2024-11-12','Pendiente'),(6,1,'Inventario','Reposición de sal mineralizada','2024-10-29','2024-11-08','Pendiente'),(7,2,'Sanidad','Revisión de mastitis','2024-10-29','2024-11-03','En proceso'),(8,2,'Producción','Control de pesaje mensual','2024-10-29','2024-11-25','Pendiente'),(9,1,'Mantenimiento','Limpieza de establos','2024-10-29','2024-11-01','En proceso');
/*!40000 ALTER TABLE `alerta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-13 11:46:47
