-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: pokedex
-- ------------------------------------------------------
-- Server version	5.7.22-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `habilidades`
--

DROP TABLE IF EXISTS `habilidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `habilidades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome_habilidade` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=234 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habilidades`
--

LOCK TABLES `habilidades` WRITE;
/*!40000 ALTER TABLE `habilidades` DISABLE KEYS */;
INSERT INTO `habilidades` VALUES (1,'Adaptability'),(2,'Aerilate'),(3,'Aftermath'),(4,'Air Lock'),(5,'Analytic'),(6,'Anger Point'),(7,'Anticipation'),(8,'Arena Trap'),(9,'Aroma Veil'),(10,'Aura Break'),(11,'Bad Dreams'),(12,'Battery'),(13,'Battle Armor'),(14,'Battle Bond'),(15,'Beast Boost'),(16,'Berserk'),(17,'Big Pecks'),(18,'Blaze'),(19,'Bulletproof'),(20,'Cheek Pouch'),(21,'Chlorophyll'),(22,'Clear Body'),(23,'Cloud Nine'),(24,'Color Change'),(25,'Comatose'),(26,'Competitive'),(27,'Compound Eyes'),(28,'Contrary'),(29,'Corrosion'),(30,'Cursed Body'),(31,'Cute Charm'),(32,'Damp'),(33,'Dancer'),(34,'Dark Aura'),(35,'Dazzling'),(36,'Defeatist'),(37,'Defiant'),(38,'Delta Stream'),(39,'Desolate Land'),(40,'Disguise'),(41,'Download'),(42,'Drizzle'),(43,'Drought'),(44,'Dry Skin'),(45,'Early Bird'),(46,'Effect Spore'),(47,'Electric Surge'),(48,'Emergency Exit'),(49,'Fairy Aura'),(50,'Filter'),(51,'Flame Body'),(52,'Flare Boost'),(53,'Flash Fire'),(54,'Flower Gift'),(55,'Flower Veil'),(56,'Fluffy'),(57,'Forecast'),(58,'Forewarn'),(59,'Friend Guard'),(60,'Frisk'),(61,'Full Metal Body'),(62,'Fur Coat'),(63,'Gale Wings'),(64,'Galvanize'),(65,'Gluttony'),(66,'Gooey'),(67,'Grass Pelt'),(68,'Grassy Surge'),(69,'Guts'),(70,'Harvest'),(71,'Healer'),(72,'Heatproof'),(73,'Heavy Metal'),(74,'Honey Gather'),(75,'Huge Power'),(76,'Hustle'),(77,'Hydration'),(78,'Hyper Cutter'),(79,'Ice Body'),(80,'Illuminate'),(81,'Illusion'),(82,'Immunity'),(83,'Imposter'),(84,'Infiltrator'),(85,'Innards Out'),(86,'Inner Focus'),(87,'Insomnia'),(88,'Intimidate'),(89,'Iron Barbs'),(90,'Iron Fist'),(91,'Justified'),(92,'Keen Eye'),(93,'Klutz'),(94,'Leaf Guard'),(95,'Levitate'),(96,'Light Metal'),(97,'Lightning Rod'),(98,'Limber'),(99,'Liquid Ooze'),(100,'Liquid Voice'),(101,'Long Reach'),(102,'Magic Bounce'),(103,'Magic Guard'),(104,'Magician'),(105,'Magma Armor'),(106,'Magnet Pull'),(107,'Marvel Scale'),(108,'Mega Launcher'),(109,'Merciless'),(110,'Minus'),(111,'Misty Surge'),(112,'Mold Breaker'),(113,'Moody'),(114,'Motor Drive'),(115,'Moxie'),(116,'Multiscale'),(117,'Multitype'),(118,'Mummy'),(119,'Natural Cure'),(120,'Neuroforce'),(121,'No Guard'),(122,'Normalize'),(123,'Oblivious'),(124,'Overcoat'),(125,'Overgrow'),(126,'Own Tempo'),(127,'Parental Bond'),(128,'Pickpocket'),(129,'Pickup'),(130,'Pixilate'),(131,'Plus'),(132,'Poison Heal'),(133,'Poison Point'),(134,'Poison Touch'),(135,'Power Construct'),(136,'Power of Alchemy'),(137,'Prankster'),(138,'Pressure'),(139,'Primordial Sea'),(140,'Prism Armor'),(141,'Protean'),(142,'Psychic Surge'),(143,'Pure Power'),(144,'Queenly Majesty'),(145,'Quick Feet'),(146,'Rain Dish'),(147,'Rattled'),(148,'Receiver'),(149,'Reckless'),(150,'Refrigerate'),(151,'Regenerator'),(152,'Rivalry'),(153,'RKS System'),(154,'Rock Head'),(155,'Rough Skin'),(156,'Run Away'),(157,'Sand Force'),(158,'Sand Rush'),(159,'Sand Stream'),(160,'Sand Veil'),(161,'Sap Sipper'),(162,'Schooling'),(163,'Scrappy'),(164,'Serene Grace'),(165,'Shadow Shield'),(166,'Shadow Tag'),(167,'Shed Skin'),(168,'Sheer Force'),(169,'Shell Armor'),(170,'Shield Dust'),(171,'Shields Down'),(172,'Simple'),(173,'Skill Link'),(174,'Slow Start'),(175,'Slush Rush'),(176,'Sniper'),(177,'Snow Cloak'),(178,'Snow Warning'),(179,'Solar Power'),(180,'Solid Rock'),(181,'Soul-Heart'),(182,'Soundproof'),(183,'Speed Boost'),(184,'Stakeout'),(185,'Stall'),(186,'Stamina'),(187,'Stance Change'),(188,'Static'),(189,'Steadfast'),(190,'Steelworker'),(191,'Stench'),(192,'Sticky Hold'),(193,'Storm Drain'),(194,'Strong Jaw'),(195,'Sturdy'),(196,'Suction Cups'),(197,'Super Luck'),(198,'Surge Surfer'),(199,'Swarm'),(200,'Sweet Veil'),(201,'Swift Swim'),(202,'Symbiosis'),(203,'Synchronize'),(204,'Tangled Feet'),(205,'Tangling Hair'),(206,'Technician'),(207,'Telepathy'),(208,'Teravolt'),(209,'Thick Fat'),(210,'Tinted Lens'),(211,'Torrent'),(212,'Tough Claws'),(213,'Toxic Boost'),(214,'Trace'),(215,'Triage'),(216,'Truant'),(217,'Turboblaze'),(218,'Unaware'),(219,'Unburden'),(220,'Unnerve'),(221,'Victory Star'),(222,'Vital Spirit'),(223,'Volt Absorb'),(224,'Water Absorb'),(225,'Water Bubble'),(226,'Water Compaction'),(227,'Water Veil'),(228,'Weak Armor'),(229,'White Smoke'),(230,'Wimp Out'),(231,'Wonder Guard'),(232,'Wonder Skin'),(233,'Zen Mode');
/*!40000 ALTER TABLE `habilidades` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-11 22:48:42
