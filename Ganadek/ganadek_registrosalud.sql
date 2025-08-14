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
-- Table structure for table `registrosalud`
--

DROP TABLE IF EXISTS `registrosalud`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registrosalud` (
  `idSalud` int NOT NULL AUTO_INCREMENT,
  `idAnimal` int DEFAULT NULL,
  `tipoTratamiento` varchar(100) DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `veterinario` varchar(100) DEFAULT NULL,
  `observaciones` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idSalud`),
  KEY `idAnimal` (`idAnimal`),
  CONSTRAINT `registrosalud_ibfk_1` FOREIGN KEY (`idAnimal`) REFERENCES `animali` (`idAnimal`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrosalud`
--

LOCK TABLES `registrosalud` WRITE;
/*!40000 ALTER TABLE `registrosalud` DISABLE KEYS */;
INSERT INTO `registrosalud` VALUES (1,1,'Vacunación','Vacuna contra la aftosa','2024-10-01','Dr. Ana Gómez','Aplicación rutinaria'),(2,2,'Desparasitación','Desparasitación trimestral','2024-10-15','Dr. Ana Gómez','Sin reacciones adversas'),(3,4,'Control','Revisión general','2024-10-10','Dr. Ana Gómez','Estado óptimo'),(4,5,'Vacunación','Vacuna triple','2024-10-12','Dr. Carlos López','Aplicación completa'),(5,6,'Desparasitación','Desparasitación oral','2024-10-15','Dr. Ana Gómez','Tratamiento preventivo'),(6,7,'Curación','Tratamiento de cojera','2024-10-18','Dr. Carlos López','En recuperación'),(7,8,'Control','Revisión dental','2024-10-20','Dr. Ana Gómez','Estado normal'),(8,9,'Vacunación','Refuerzo vacunal','2024-10-22','Dr. Carlos López','Según calendario'),(9,10,'Vitaminas','Suplementación vitamínica','2024-10-25','Dr. Ana Gómez','Refuerzo general');
/*!40000 ALTER TABLE `registrosalud` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-13 11:46:48
