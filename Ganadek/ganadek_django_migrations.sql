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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-07-03 06:13:41.372224'),(2,'auth','0001_initial','2025-07-03 06:13:42.495135'),(3,'admin','0001_initial','2025-07-03 06:13:42.749747'),(4,'admin','0002_logentry_remove_auto_add','2025-07-03 06:13:42.763097'),(5,'admin','0003_logentry_add_action_flag_choices','2025-07-03 06:13:42.780268'),(6,'contenttypes','0002_remove_content_type_name','2025-07-03 06:13:42.971438'),(7,'auth','0002_alter_permission_name_max_length','2025-07-03 06:13:43.092325'),(8,'auth','0003_alter_user_email_max_length','2025-07-03 06:13:43.178149'),(9,'auth','0004_alter_user_username_opts','2025-07-03 06:13:43.189829'),(10,'auth','0005_alter_user_last_login_null','2025-07-03 06:13:43.305101'),(11,'auth','0006_require_contenttypes_0002','2025-07-03 06:13:43.311269'),(12,'auth','0007_alter_validators_add_error_messages','2025-07-03 06:13:43.329751'),(13,'auth','0008_alter_user_username_max_length','2025-07-03 06:13:43.452589'),(14,'auth','0009_alter_user_last_name_max_length','2025-07-03 06:13:43.574341'),(15,'auth','0010_alter_group_name_max_length','2025-07-03 06:13:43.607149'),(16,'auth','0011_update_proxy_permissions','2025-07-03 06:13:43.624746'),(17,'auth','0012_alter_user_first_name_max_length','2025-07-03 06:13:43.750544'),(18,'sessions','0001_initial','2025-07-03 06:13:43.820704'),(19,'tasks','0001_initial','2025-07-21 03:18:12.671567'),(20,'tasks','0002_alter_alerta_options_alter_animal_options_and_more','2025-07-21 03:20:30.187106'),(21,'tasks','0003_finca_estado','2025-07-21 03:22:45.447796'),(22,'tasks','0004_finca_fecha_creacion','2025-07-21 03:31:14.141909'),(23,'tasks','0005_animali_authgroup_authgrouppermissions_and_more','2025-07-23 04:12:36.003697'),(24,'tasks','0006_alter_empleado_options','2025-07-24 19:40:29.927143'),(25,'tasks','0007_alter_empleado_options_alter_finca_options','2025-07-24 19:40:55.205266'),(26,'tasks','0008_alter_finca_hectareas_alter_finca_latitud_and_more','2025-07-24 19:55:59.226070'),(27,'tasks','0009_alter_finca_hectareas','2025-07-24 20:01:05.230954');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
