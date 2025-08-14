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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=153 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add usuario',7,'add_usuario'),(26,'Can change usuario',7,'change_usuario'),(27,'Can delete usuario',7,'delete_usuario'),(28,'Can view usuario',7,'view_usuario'),(29,'Can add inventario',8,'add_inventario'),(30,'Can change inventario',8,'change_inventario'),(31,'Can delete inventario',8,'delete_inventario'),(32,'Can view inventario',8,'view_inventario'),(33,'Can add animal',9,'add_animal'),(34,'Can change animal',9,'change_animal'),(35,'Can delete animal',9,'delete_animal'),(36,'Can view animal',9,'view_animal'),(37,'Can add empleado',10,'add_empleado'),(38,'Can change empleado',10,'change_empleado'),(39,'Can delete empleado',10,'delete_empleado'),(40,'Can view empleado',10,'view_empleado'),(41,'Can add registroalimenticio',11,'add_registroalimenticio'),(42,'Can change registroalimenticio',11,'change_registroalimenticio'),(43,'Can delete registroalimenticio',11,'delete_registroalimenticio'),(44,'Can view registroalimenticio',11,'view_registroalimenticio'),(45,'Can add registroreproduccion',12,'add_registroreproduccion'),(46,'Can change registroreproduccion',12,'change_registroreproduccion'),(47,'Can delete registroreproduccion',12,'delete_registroreproduccion'),(48,'Can view registroreproduccion',12,'view_registroreproduccion'),(49,'Can add mover ganado',13,'add_moverganado'),(50,'Can change mover ganado',13,'change_moverganado'),(51,'Can delete mover ganado',13,'delete_moverganado'),(52,'Can view mover ganado',13,'view_moverganado'),(53,'Can add finca',14,'add_finca'),(54,'Can change finca',14,'change_finca'),(55,'Can delete finca',14,'delete_finca'),(56,'Can view finca',14,'view_finca'),(57,'Can add alerta',15,'add_alerta'),(58,'Can change alerta',15,'change_alerta'),(59,'Can delete alerta',15,'delete_alerta'),(60,'Can view alerta',15,'view_alerta'),(61,'Can add horario',16,'add_horario'),(62,'Can change horario',16,'change_horario'),(63,'Can delete horario',16,'delete_horario'),(64,'Can view horario',16,'view_horario'),(65,'Can add propietario',17,'add_propietario'),(66,'Can change propietario',17,'change_propietario'),(67,'Can delete propietario',17,'delete_propietario'),(68,'Can view propietario',17,'view_propietario'),(69,'Can add madre',18,'add_madre'),(70,'Can change madre',18,'change_madre'),(71,'Can delete madre',18,'delete_madre'),(72,'Can view madre',18,'view_madre'),(73,'Can add registrosalud',19,'add_registrosalud'),(74,'Can change registrosalud',19,'change_registrosalud'),(75,'Can delete registrosalud',19,'delete_registrosalud'),(76,'Can view registrosalud',19,'view_registrosalud'),(77,'Can add padre',20,'add_padre'),(78,'Can change padre',20,'change_padre'),(79,'Can delete padre',20,'delete_padre'),(80,'Can view padre',20,'view_padre'),(81,'Can add trazabilidad',21,'add_trazabilidad'),(82,'Can change trazabilidad',21,'change_trazabilidad'),(83,'Can delete trazabilidad',21,'delete_trazabilidad'),(84,'Can view trazabilidad',21,'view_trazabilidad'),(85,'Can add registroproduccion',22,'add_registroproduccion'),(86,'Can change registroproduccion',22,'change_registroproduccion'),(87,'Can delete registroproduccion',22,'delete_registroproduccion'),(88,'Can view registroproduccion',22,'view_registroproduccion'),(89,'Can add potrero',23,'add_potrero'),(90,'Can change potrero',23,'change_potrero'),(91,'Can delete potrero',23,'delete_potrero'),(92,'Can view potrero',23,'view_potrero'),(93,'Can add animali',24,'add_animali'),(94,'Can change animali',24,'change_animali'),(95,'Can delete animali',24,'delete_animali'),(96,'Can view animali',24,'view_animali'),(97,'Can add auth group',25,'add_authgroup'),(98,'Can change auth group',25,'change_authgroup'),(99,'Can delete auth group',25,'delete_authgroup'),(100,'Can view auth group',25,'view_authgroup'),(101,'Can add auth group permissions',26,'add_authgrouppermissions'),(102,'Can change auth group permissions',26,'change_authgrouppermissions'),(103,'Can delete auth group permissions',26,'delete_authgrouppermissions'),(104,'Can view auth group permissions',26,'view_authgrouppermissions'),(105,'Can add auth permission',27,'add_authpermission'),(106,'Can change auth permission',27,'change_authpermission'),(107,'Can delete auth permission',27,'delete_authpermission'),(108,'Can view auth permission',27,'view_authpermission'),(109,'Can add auth user',28,'add_authuser'),(110,'Can change auth user',28,'change_authuser'),(111,'Can delete auth user',28,'delete_authuser'),(112,'Can view auth user',28,'view_authuser'),(113,'Can add auth user groups',29,'add_authusergroups'),(114,'Can change auth user groups',29,'change_authusergroups'),(115,'Can delete auth user groups',29,'delete_authusergroups'),(116,'Can view auth user groups',29,'view_authusergroups'),(117,'Can add auth user user permissions',30,'add_authuseruserpermissions'),(118,'Can change auth user user permissions',30,'change_authuseruserpermissions'),(119,'Can delete auth user user permissions',30,'delete_authuseruserpermissions'),(120,'Can view auth user user permissions',30,'view_authuseruserpermissions'),(121,'Can add django admin log',31,'add_djangoadminlog'),(122,'Can change django admin log',31,'change_djangoadminlog'),(123,'Can delete django admin log',31,'delete_djangoadminlog'),(124,'Can view django admin log',31,'view_djangoadminlog'),(125,'Can add django content type',32,'add_djangocontenttype'),(126,'Can change django content type',32,'change_djangocontenttype'),(127,'Can delete django content type',32,'delete_djangocontenttype'),(128,'Can view django content type',32,'view_djangocontenttype'),(129,'Can add django migrations',33,'add_djangomigrations'),(130,'Can change django migrations',33,'change_djangomigrations'),(131,'Can delete django migrations',33,'delete_djangomigrations'),(132,'Can view django migrations',33,'view_djangomigrations'),(133,'Can add django session',34,'add_djangosession'),(134,'Can change django session',34,'change_djangosession'),(135,'Can delete django session',34,'delete_djangosession'),(136,'Can view django session',34,'view_djangosession'),(137,'Can add lote avicola',35,'add_loteavicola'),(138,'Can change lote avicola',35,'change_loteavicola'),(139,'Can delete lote avicola',35,'delete_loteavicola'),(140,'Can view lote avicola',35,'view_loteavicola'),(141,'Can add madrei',36,'add_madrei'),(142,'Can change madrei',36,'change_madrei'),(143,'Can delete madrei',36,'delete_madrei'),(144,'Can view madrei',36,'view_madrei'),(145,'Can add padrei',37,'add_padrei'),(146,'Can change padrei',37,'change_padrei'),(147,'Can delete padrei',37,'delete_padrei'),(148,'Can view padrei',37,'view_padrei'),(149,'Can add unidad productiva',38,'add_unidadproductiva'),(150,'Can change unidad productiva',38,'change_unidadproductiva'),(151,'Can delete unidad productiva',38,'delete_unidadproductiva'),(152,'Can view unidad productiva',38,'view_unidadproductiva');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
