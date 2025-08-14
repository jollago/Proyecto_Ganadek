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
-- Table structure for table `trazabilidad`
--

DROP TABLE IF EXISTS `trazabilidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trazabilidad` (
  `idTrazabilidad` int NOT NULL AUTO_INCREMENT,
  `idAnimal` int DEFAULT NULL,
  `tipoEvento` varchar(100) DEFAULT NULL,
  `fechaEvento` date DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idTrazabilidad`),
  KEY `idAnimal` (`idAnimal`),
  CONSTRAINT `trazabilidad_ibfk_1` FOREIGN KEY (`idAnimal`) REFERENCES `animali` (`idAnimal`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trazabilidad`
--

LOCK TABLES `trazabilidad` WRITE;
/*!40000 ALTER TABLE `trazabilidad` DISABLE KEYS */;
INSERT INTO `trazabilidad` VALUES (1,1,'Nacimiento','2022-03-15','Nacimiento registrado'),(2,1,'Vacunación','2024-10-01','Primera vacuna aplicada'),(3,4,'Vacunación','2024-10-12','Vacuna triple aplicada'),(4,5,'Pesaje','2024-10-15','Control mensual de peso'),(5,6,'Tratamiento','2024-10-18','Desparasitación realizada'),(6,7,'Reproducción','2024-10-20','Confirmación de preñez'),(7,8,'Movimiento','2024-10-25','Cambio de potrero'),(8,9,'Producción','2024-10-27','Inicio de lactancia'),(9,10,'Salud','2024-10-29','Control veterinario general');
/*!40000 ALTER TABLE `trazabilidad` ENABLE KEYS */;
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
