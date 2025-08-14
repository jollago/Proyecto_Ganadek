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
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleado` (
  `idEmpleado` int NOT NULL,
  `idHorario` int DEFAULT NULL,
  `idFinca` int DEFAULT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `puesto` varchar(100) DEFAULT NULL,
  `fechaContratacion` date DEFAULT NULL,
  `salario` float DEFAULT NULL,
  `idUsuario` int DEFAULT NULL,
  `estado` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idEmpleado`),
  KEY `idHorario` (`idHorario`),
  KEY `idFinca` (`idFinca`),
  KEY `fk_usuario` (`idUsuario`),
  CONSTRAINT `empleado_ibfk_1` FOREIGN KEY (`idHorario`) REFERENCES `horario` (`idHorario`),
  CONSTRAINT `empleado_ibfk_2` FOREIGN KEY (`idFinca`) REFERENCES `finca` (`idFinca`),
  CONSTRAINT `fk_usuario` FOREIGN KEY (`idUsuario`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
INSERT INTO `empleado` VALUES (1,1,1,'Pedro','Ramírez','pedro.ramirez@email.com','Vaquero','2023-01-15',1200000,NULL,'Activo'),(2,2,1,'Ana','Gómez','ana.gomez@email.com','Veterinaria','2023-02-01',2500000,NULL,'Activo'),(3,3,2,'Carlos','Martínez','carlos.martinez@email.com','Capataz','2023-03-15',1800000,NULL,'Inactivo'),(4,4,2,'Laura','Sánchez','laura.sanchez@email.com','Administradora','2023-04-01',2000000,1,'Activo'),(5,5,1,'Miguel','Torres','miguel.torres@email.com','Vigilante','2023-05-15',1300000,NULL,'Inactivo'),(6,6,1,'Sandra','Jiménez','sandra.jimenez@email.com','Ordeñadora','2023-06-01',1400000,NULL,'Activo'),(7,7,2,'Roberto','Díaz','roberto.diaz@email.com','Tractorista','2023-07-15',1600000,NULL,'Activo'),(8,8,2,'Carmen','Vargas','carmen.vargas@email.com','Auxiliar Veterinaria','2023-08-01',1500000,NULL,'Inactivo'),(9,9,1,'Jorge','Luna','jorge.luna@email.com','Mayordomo','2023-09-15',1700000,NULL,'Activo');
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
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
