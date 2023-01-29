-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: prueba
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.22.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `abono`
--

DROP TABLE IF EXISTS `abono`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `abono` (
  `id_abono` int NOT NULL AUTO_INCREMENT,
  `fk_id_pago` int DEFAULT NULL,
  `fk_id_paciente` int DEFAULT NULL,
  `nu_nabono` int DEFAULT NULL,
  `nu_monto` int DEFAULT NULL,
  `fh_abono` date DEFAULT NULL,
  PRIMARY KEY (`id_abono`),
  KEY `fk_id_pago` (`fk_id_pago`),
  KEY `fk_id_paciente` (`fk_id_paciente`),
  CONSTRAINT `abono_ibfk_1` FOREIGN KEY (`fk_id_pago`) REFERENCES `pagos` (`id_pago`),
  CONSTRAINT `abono_ibfk_2` FOREIGN KEY (`fk_id_paciente`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `abono`
--

LOCK TABLES `abono` WRITE;
/*!40000 ALTER TABLE `abono` DISABLE KEYS */;
INSERT INTO `abono` VALUES (1,1,3,1,500,'2023-01-27'),(2,1,3,2,500,'2023-01-28'),(3,2,4,1,500,'2023-01-28'),(4,3,9,1,1500,'2023-01-28');
/*!40000 ALTER TABLE `abono` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `citas`
--

DROP TABLE IF EXISTS `citas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citas` (
  `id_cita` int NOT NULL AUTO_INCREMENT,
  `fk_id_paciente` int DEFAULT NULL,
  `fh_cita` datetime DEFAULT NULL,
  `fk_id_dentista` int DEFAULT NULL,
  PRIMARY KEY (`id_cita`),
  KEY `fk_id_paciente` (`fk_id_paciente`),
  KEY `fk_id_dentista` (`fk_id_dentista`),
  CONSTRAINT `citas_ibfk_1` FOREIGN KEY (`fk_id_paciente`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `citas_ibfk_2` FOREIGN KEY (`fk_id_dentista`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citas`
--

LOCK TABLES `citas` WRITE;
/*!40000 ALTER TABLE `citas` DISABLE KEYS */;
INSERT INTO `citas` VALUES (1,3,'2023-01-23 13:00:00',2),(2,4,'2023-01-24 13:00:00',2),(3,9,'2023-01-25 14:00:00',2);
/*!40000 ALTER TABLE `citas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consulta`
--

DROP TABLE IF EXISTS `consulta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consulta` (
  `id_consulta` int NOT NULL AUTO_INCREMENT,
  `fk_id_paciente` int DEFAULT NULL,
  `fk_id_dentista` int DEFAULT NULL,
  `fk_id_tratamiento` int DEFAULT NULL,
  `tx_desc` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_consulta`),
  KEY `fk_id_paciente` (`fk_id_paciente`),
  KEY `fk_id_dentista` (`fk_id_dentista`),
  KEY `fk_id_tratamiento` (`fk_id_tratamiento`),
  CONSTRAINT `consulta_ibfk_1` FOREIGN KEY (`fk_id_paciente`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `consulta_ibfk_2` FOREIGN KEY (`fk_id_dentista`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `consulta_ibfk_3` FOREIGN KEY (`fk_id_tratamiento`) REFERENCES `tratamientos` (`id_tratamiento`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consulta`
--

LOCK TABLES `consulta` WRITE;
/*!40000 ALTER TABLE `consulta` DISABLE KEYS */;
INSERT INTO `consulta` VALUES (1,3,2,1,'Se restauró un diente dañado'),(2,4,2,4,'Se realizó una consulta rutinaria'),(3,9,2,2,'se cambiaron las ligas de los brakets');
/*!40000 ALTER TABLE `consulta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encuesta`
--

DROP TABLE IF EXISTS `encuesta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `encuesta` (
  `fk_id_consulta` int DEFAULT NULL,
  `val` tinyint(1) DEFAULT NULL,
  KEY `id_consulta` (`fk_id_consulta`),
  CONSTRAINT `encuesta_ibfk_1` FOREIGN KEY (`fk_id_consulta`) REFERENCES `consulta` (`id_consulta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encuesta`
--

LOCK TABLES `encuesta` WRITE;
/*!40000 ALTER TABLE `encuesta` DISABLE KEYS */;
INSERT INTO `encuesta` VALUES (2,1),(1,1),(3,1);
/*!40000 ALTER TABLE `encuesta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mat_consulta`
--

DROP TABLE IF EXISTS `mat_consulta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mat_consulta` (
  `id_matc` int NOT NULL AUTO_INCREMENT,
  `fk_id_material` int DEFAULT NULL,
  `fk_id_consulta` int DEFAULT NULL,
  `nu_cantidad` int DEFAULT NULL,
  PRIMARY KEY (`id_matc`),
  KEY `fk_id_consulta` (`fk_id_consulta`),
  KEY `fk_id_material` (`fk_id_material`),
  CONSTRAINT `mat_consulta_ibfk_1` FOREIGN KEY (`fk_id_consulta`) REFERENCES `consulta` (`id_consulta`),
  CONSTRAINT `mat_consulta_ibfk_2` FOREIGN KEY (`fk_id_material`) REFERENCES `materiales` (`id_material`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mat_consulta`
--

LOCK TABLES `mat_consulta` WRITE;
/*!40000 ALTER TABLE `mat_consulta` DISABLE KEYS */;
INSERT INTO `mat_consulta` VALUES (1,1,2,1),(2,2,2,2),(3,1,1,1),(4,5,3,1),(5,2,3,2);
/*!40000 ALTER TABLE `mat_consulta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materiales`
--

DROP TABLE IF EXISTS `materiales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materiales` (
  `id_material` int NOT NULL AUTO_INCREMENT,
  `tx_nombre` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nu_cantidad` int DEFAULT NULL,
  PRIMARY KEY (`id_material`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materiales`
--

LOCK TABLES `materiales` WRITE;
/*!40000 ALTER TABLE `materiales` DISABLE KEYS */;
INSERT INTO `materiales` VALUES (1,'Guantes desechables',487),(2,'Gasas',515),(5,'Ligas',174),(6,'cubrebocas',150),(7,'bracket',150),(8,'babero',130),(9,'Servilletas para limpiar',150),(10,'Isopos',240);
/*!40000 ALTER TABLE `materiales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagos`
--

DROP TABLE IF EXISTS `pagos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagos` (
  `id_pago` int NOT NULL AUTO_INCREMENT,
  `fk_id_paciente` int DEFAULT NULL,
  `nu_total` int DEFAULT NULL,
  PRIMARY KEY (`id_pago`),
  KEY `fk_id_paciente` (`fk_id_paciente`),
  CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`fk_id_paciente`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagos`
--

LOCK TABLES `pagos` WRITE;
/*!40000 ALTER TABLE `pagos` DISABLE KEYS */;
INSERT INTO `pagos` VALUES (1,3,1000),(2,4,500),(3,9,15000);
/*!40000 ALTER TABLE `pagos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persona` (
  `fk_id_usuario` int NOT NULL AUTO_INCREMENT,
  `tx_nombre` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tx_paterno` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tx_materno` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tx_telefono` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tx_sexo` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  KEY `fk_id_usuario` (`fk_id_usuario`),
  CONSTRAINT `persona_ibfk_1` FOREIGN KEY (`fk_id_usuario`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` VALUES (1,'Ale','Mas','Cast','5584799367','Masculino'),(2,'Carlos','Molina','Martínez','5554535251','Masculino'),(3,'Josue','Lopez','Hernandez','5556575859','Masculino'),(4,'Braulio','Adorno','Ortega','5556575860','Masculino'),(5,'Jose','Martínez','Molina','55545352561','Masculino'),(7,'Martin','Garcia','Lopez','5554535263','Masculino'),(9,'Laura','Juarez','Ramirez','5554535152','Femenino'),(10,'Marta','Rodriguez','Franco','5554535203','Femenino'),(11,'Alan','Escudero','Martinez','5554535251','Hombre'),(12,'Benito','Martinez','Ocasio','5554535250','Femenino');
/*!40000 ALTER TABLE `persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `preguntas`
--

DROP TABLE IF EXISTS `preguntas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `preguntas` (
  `id_pregunta` int NOT NULL AUTO_INCREMENT,
  `tx_pregunta` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fk_id_tipo_pregunta` int DEFAULT NULL,
  PRIMARY KEY (`id_pregunta`),
  KEY `fk_id_tipo_pregunta` (`fk_id_tipo_pregunta`),
  CONSTRAINT `preguntas_ibfk_1` FOREIGN KEY (`fk_id_tipo_pregunta`) REFERENCES `tipo_pregunta` (`id_tipo_pregunta`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `preguntas`
--

LOCK TABLES `preguntas` WRITE;
/*!40000 ALTER TABLE `preguntas` DISABLE KEYS */;
INSERT INTO `preguntas` VALUES (1,'¿Cómo considera que se encuentran las instalaciones de la Clínica Dental?',2),(2,'¿Considera usted que se cuenta con la suficiente tecnología para atender a los pacientes?',2),(3,'¿Considera que la pagína web ha sido de mucha ayuda para agendar, programar cita y llevar el control de su tratamiento?',2),(4,'¿Cuál es la probabilidad de que recomiendes la clínica a tus amigos o familiares?',2),(5,'¿Cuál es la probabilidad de que vuelvas para un seguimiento de su salud dental?',2),(6,'¿Considera usted que su Médico Dentista cuenta la suficiente higiene para realizar una consulta?',1),(7,'¿Cómo considera usted que fue la atención dada por su Dentista?',1),(8,'¿El Médico Dentista le brindó la información completa sobre su tratamiento?',1),(9,'¿Considera que los problemas por los que acudió a la consulta se han solucionado?',1),(10,'¿Recomendaría a su doctor? ',1);
/*!40000 ALTER TABLE `preguntas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `respuestas`
--

DROP TABLE IF EXISTS `respuestas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `respuestas` (
  `id_respuesta` int NOT NULL AUTO_INCREMENT,
  `fk_id_pregunta` int DEFAULT NULL,
  `fk_id_paciente` int DEFAULT NULL,
  `fk_id_dentista` int DEFAULT NULL,
  `nu_resp` int DEFAULT NULL,
  `fk_id_consulta` int DEFAULT NULL,
  PRIMARY KEY (`id_respuesta`),
  KEY `fk_id_pregunta` (`fk_id_pregunta`),
  KEY `fk_id_paciente` (`fk_id_paciente`),
  KEY `fk_id_dentista` (`fk_id_dentista`),
  KEY `fk_id_consulta` (`fk_id_consulta`),
  CONSTRAINT `respuestas_ibfk_1` FOREIGN KEY (`fk_id_pregunta`) REFERENCES `preguntas` (`id_pregunta`),
  CONSTRAINT `respuestas_ibfk_2` FOREIGN KEY (`fk_id_paciente`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `respuestas_ibfk_3` FOREIGN KEY (`fk_id_dentista`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `respuestas_ibfk_4` FOREIGN KEY (`fk_id_consulta`) REFERENCES `consulta` (`id_consulta`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `respuestas`
--

LOCK TABLES `respuestas` WRITE;
/*!40000 ALTER TABLE `respuestas` DISABLE KEYS */;
INSERT INTO `respuestas` VALUES (11,1,9,2,4,3),(12,2,9,2,4,3),(13,3,9,2,4,3),(14,4,9,2,4,3),(15,5,9,2,4,3),(16,6,9,2,4,3),(17,7,9,2,4,3),(18,8,9,2,4,3),(19,9,9,2,4,3),(20,10,9,2,4,3),(21,1,4,2,3,2),(22,2,4,2,3,2),(23,3,4,2,3,2),(24,4,4,2,3,2),(25,5,4,2,3,2),(26,6,4,2,3,2),(27,7,4,2,3,2),(28,8,4,2,3,2),(29,9,4,2,3,2),(30,10,4,2,3,2),(31,1,3,2,2,1),(32,2,3,2,2,1),(33,3,3,2,2,1),(34,4,3,2,2,1),(35,5,3,2,2,1),(36,6,3,2,1,1),(37,7,3,2,1,1),(38,8,3,2,1,1),(39,9,3,2,1,1),(40,10,3,2,1,1);
/*!40000 ALTER TABLE `respuestas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol`
--

DROP TABLE IF EXISTS `rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rol` (
  `id_rol` int NOT NULL,
  `tx_nombre` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol`
--

LOCK TABLES `rol` WRITE;
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
INSERT INTO `rol` VALUES (1,'administrador'),(2,'dentista'),(3,'cliente');
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_pregunta`
--

DROP TABLE IF EXISTS `tipo_pregunta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_pregunta` (
  `id_tipo_pregunta` int NOT NULL,
  `tx_pregunta` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_tipo_pregunta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_pregunta`
--

LOCK TABLES `tipo_pregunta` WRITE;
/*!40000 ALTER TABLE `tipo_pregunta` DISABLE KEYS */;
INSERT INTO `tipo_pregunta` VALUES (1,'dentista'),(2,'instalaciones');
/*!40000 ALTER TABLE `tipo_pregunta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tratamientos`
--

DROP TABLE IF EXISTS `tratamientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tratamientos` (
  `id_tratamiento` int NOT NULL AUTO_INCREMENT,
  `tx_nombre` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tx_desc` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nu_precio` int DEFAULT NULL,
  PRIMARY KEY (`id_tratamiento`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tratamientos`
--

LOCK TABLES `tratamientos` WRITE;
/*!40000 ALTER TABLE `tratamientos` DISABLE KEYS */;
INSERT INTO `tratamientos` VALUES (1,'Restauración Simple con Resina','Tratamiento realizado para lesiones causadas por caries, pequeñas fracturas que son restauradas con resina.',1000),(2,'Brakets','Tratamiento dental para el mejoramiento de la sonrisa del paciente.',15000),(3,'Éxodoncia simple ','Procedimiento quirúrgico el cual se extrae un diente por algún daño.',2500),(4,'Consulta General','Consulta General rutinaria, para continuar con algun tratamiento.',500);
/*!40000 ALTER TABLE `tratamientos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `tx_correo` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tx_password` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fk_id_rol` int DEFAULT NULL,
  `id_dentista` int DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `tx_correo` (`tx_correo`),
  KEY `fk_id_rol` (`fk_id_rol`),
  KEY `id_dentista` (`id_dentista`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`fk_id_rol`) REFERENCES `rol` (`id_rol`),
  CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`id_dentista`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'alemas@hotmail.com','pbkdf2:sha256:260000$OubWCzG0I8lzq95A$b145dd7231e1b441832e925f542a2982a3e9a83a1424cdc83c7cd1370205b382',1,5),(2,'dentista1@hotmail.com','pbkdf2:sha256:260000$w7X42TDMA5fM9Y8g$971632a04f3ed7a6d4c9faba60ff617af280c853bad9798c83e76b87dad77350',2,5),(3,'usuario1@hotmail.com','pbkdf2:sha256:260000$WjJ9LJ46tFwoYQeo$4a762fb2d95cc0a4d1191d960a9d9d0ab802934f0f3f6d99fbad3adb6dc63972',3,2),(4,'usuario2@hotmail.com','pbkdf2:sha256:260000$kgTKP5MNT7uOhLVo$489c38bfa0e03635be3ba8ddc6680281c8375a343ad1b13daf3488ebe0ba8468',3,2),(5,'dentista2@hotmail.com','pbkdf2:sha256:260000$Wugxw8JCxs1sp8UX$490923480cf6bb301a6b852ac119c4e3cf6fa9a307db6d51a6c2e3507e3fc597',2,2),(7,'usuario4@hotmail.com','pbkdf2:sha256:260000$CIoSBucdrLLdMaBo$8529252fa6fe469647d698135dac57275467ac606d05aa599166c9078366bea3',3,5),(9,'usuario5@hotmail.com','pbkdf2:sha256:260000$lHnGcHRA0pPM7roa$5b21bbede59c35bd0f6bef56ef8b368605b606c3569d675199777cfaf06c90b8',3,2),(10,'usuario6@hotmail.com','pbkdf2:sha256:260000$07ToQN2AqLd3yi4F$58944748a3d7074d0fbdab674feefb03df4ba4d659fcec2fc3445aabe8d04c6e',3,2),(11,'usuariox@mail.com','pbkdf2:sha256:260000$xMt08WLJnmWgLh8t$68a217a99e9e35d56819e4b8af8428894239bf05e5b84f1a327faee14a462da9',3,5),(12,'usuariof@hotmail.com','pbkdf2:sha256:260000$VyZDslUPWqld4XlV$cb355297e345901468f5e1e46cec5b1673a161290e45d6db1c5f883eb4a5f37a',3,NULL);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-29 17:33:16
