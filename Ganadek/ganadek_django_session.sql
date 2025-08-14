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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('5rw2ixcu4t3i2l5f5ce8hy04ybc20mzv','e30:1uXPyu:vzDIoiyBXJSYkaBIOKER3fS8E6m5bri9x_gmWwjaSXQ','2025-07-17 19:52:28.440604'),('9orve4ptjgou2dzbn1rf20xocfq8u2a7','e30:1uXPvO:ABPFSlbseEZ693lsHHRw5HGACIO3qaKjRGnVuzYM1Nw','2025-07-17 19:48:50.023379'),('a34mmknrooe682vl8zos7d34sd58pby6','e30:1uXPzC:FnGEYEEy_OOFCyboHh7cEt4GdbCQGiFa5nlDhUkmyvE','2025-07-17 19:52:46.997074'),('gfrlnoxdrwq8su7xiwa1dwjyg3f61rem','e30:1uXPxv:CQ48rBwsAzjvX3wmISwNdi33jR96bkfmGKZ1v2GdzRg','2025-07-17 19:51:27.356278'),('gk5qjljksy8ks2fw9jtbtde07fv1sid0','.eJxVjMsOwiAQRf-FtSE8CnZcuu83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mL0FqcfseI6cF1J3THemsytbouc5S7Ig_a5dSIn9fD_Tso2Mu3ZkBvz-yBNZCPZjA6cwYL0WmTARVHQgV58CqNbEcXGYxzmUklAG_F-wMR4zhT:1umDOz:mjfOKB1YIyZeRjHMWqOJlXiHtq28funF_uPIsFLmBPk','2025-08-27 15:28:33.180631'),('ntq15aljj2k3awivvd8wnfvi2895xvyr','.eJxVjMsOwiAQRf-FtSE8CnZcuu83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mL0FqcfseI6cF1J3THemsytbouc5S7Ig_a5dSIn9fD_Tso2Mu3ZkBvz-yBNZCPZjA6cwYL0WmTARVHQgV58CqNbEcXGYxzmUklAG_F-wMR4zhT:1ufJg5:KEVm7_4OYmXhEF94PPvz0XBDRRHqGttsTm9r65q2h6E','2025-08-08 14:45:41.856964'),('tnpyx7jjsq0iuie6tk8rzpm20o22uji6','.eJxVjMsOwiAQRf-FtSE8CnZcuu83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mL0FqcfseI6cF1J3THemsytbouc5S7Ig_a5dSIn9fD_Tso2Mu3ZkBvz-yBNZCPZjA6cwYL0WmTARVHQgV58CqNbEcXGYxzmUklAG_F-wMR4zhT:1ueo48:WqhnbzrieDMuOTNLtsqJc4-rmQTXXTZ4Sepg0UMMHy8','2025-08-07 05:00:24.747427');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
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
