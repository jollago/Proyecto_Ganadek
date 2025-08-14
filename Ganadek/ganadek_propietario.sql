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
-- Table structure for table `propietario`
--

DROP TABLE IF EXISTS `propietario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `propietario` (
  `cedulaPropietario` int NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `telefono` varchar(13) DEFAULT NULL,
  `correo` varchar(50) DEFAULT NULL,
  `direccion` varchar(50) DEFAULT NULL,
  `tipoDocumento` enum('CC','NIT','Pasaporte') NOT NULL DEFAULT 'CC',
  `departamento` varchar(100) DEFAULT NULL,
  `municipio` varchar(100) DEFAULT NULL,
  `contactoAlterno` varchar(100) DEFAULT NULL,
  `fechaRegistro` date DEFAULT NULL,
  `estado` enum('Activo','Inactivo') DEFAULT 'Activo',
  `fotoDocumento` varchar(255) DEFAULT NULL,
  `observaciones` text,
  PRIMARY KEY (`cedulaPropietario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `propietario`
--

LOCK TABLES `propietario` WRITE;
/*!40000 ALTER TABLE `propietario` DISABLE KEYS */;
INSERT INTO `propietario` VALUES (1001,'Juan Pérez','3121234567','juan.perez@email.com','Calle 123 #45-67','CC',NULL,NULL,NULL,NULL,'Activo',NULL,NULL),(1002,'María López','3139876543','maria.lopez@email.com','Carrera 89 #12-34','CC',NULL,NULL,NULL,NULL,'Activo',NULL,NULL),(1003,'luis','3015654856','luis92@gmail.com','cll33 #33-33','CC',NULL,NULL,NULL,NULL,'Activo',NULL,NULL),(1004,'yhui','3427586451',' ',NULL,'CC',NULL,NULL,NULL,NULL,'Activo',NULL,NULL),(1005,'perla','3201456521','xzcvgxcv@email.com','sxdvfdsgv','CC',NULL,NULL,NULL,NULL,'Activo',NULL,NULL),(1006,'sdsad','4566456454',NULL,NULL,'CC',NULL,NULL,NULL,NULL,'Activo',NULL,NULL);
/*!40000 ALTER TABLE `propietario` ENABLE KEYS */;
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
