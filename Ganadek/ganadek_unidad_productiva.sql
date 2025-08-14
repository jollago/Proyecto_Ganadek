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
-- Table structure for table `unidad_productiva`
--

DROP TABLE IF EXISTS `unidad_productiva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unidad_productiva` (
  `idUnidad` int NOT NULL AUTO_INCREMENT,
  `idFinca` int NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `tipoUnidad` enum('Potrero','Galpón','Jaula','Corral','Otro') NOT NULL,
  `especie_destinada` enum('Bovino','Porcino','Avícola','Mixta') NOT NULL,
  `area` decimal(10,2) DEFAULT NULL,
  `capacidad_maxima` int DEFAULT NULL,
  `descripcion` text,
  `fuenteAgua` varchar(100) DEFAULT NULL,
  `tipoPasto` varchar(100) DEFAULT NULL,
  `tipoConstruccion` varchar(100) DEFAULT NULL,
  `sistemaVentilacion` varchar(100) DEFAULT NULL,
  `sistemaAlimentacion` varchar(100) DEFAULT NULL,
  `temperaturaControlada` tinyint(1) DEFAULT NULL,
  `iluminacion` tinyint(1) DEFAULT NULL,
  `estado` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`idUnidad`),
  KEY `idFinca` (`idFinca`),
  CONSTRAINT `unidad_productiva_ibfk_1` FOREIGN KEY (`idFinca`) REFERENCES `finca` (`idFinca`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unidad_productiva`
--

LOCK TABLES `unidad_productiva` WRITE;
/*!40000 ALTER TABLE `unidad_productiva` DISABLE KEYS */;
INSERT INTO `unidad_productiva` VALUES (1,1,'Potrero Norte','Potrero','Bovino',3.50,25,'Área con buena sombra y acceso directo a agua natural.','Quebrada La Vieja','Brachiaria',NULL,NULL,NULL,NULL,NULL,'ocupado'),(2,1,'Potrero Sur','Potrero','Bovino',2.80,20,'Zona plana con pasto mejorado y cerca eléctrica.','Pozo profundo','Kikuyo',NULL,NULL,NULL,NULL,NULL,'ocupado'),(3,2,'Galpón Recría','Galpón','Porcino',1.20,80,'Galpón techado con sistema de alimentación semiautomático.',NULL,NULL,'Metálico','Natural','Semiautomático',1,1,'ocupado'),(4,2,'Galpón Engorde','Galpón','Porcino',1.50,100,'Área cerrada para etapa final de engorde con buena ventilación.',NULL,NULL,'Mixto','Mecánico','Automático',1,1,'ocupado'),(5,2,'Jaulas Ponedoras A','Jaula','Avícola',0.80,120,'Jaulas de alambre para gallinas ponedoras con recolección automática.',NULL,NULL,'Metálico','Natural','Automático',1,1,'disponible'),(6,2,'Nave de Engorde 1','Galpón','Avícola',2.00,500,'Galpón grande para pollos de engorde con control climático.',NULL,NULL,'Metálico','Mecánico','Automático',1,1,'disponible');
/*!40000 ALTER TABLE `unidad_productiva` ENABLE KEYS */;
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
