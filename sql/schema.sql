-- MySQL dump 10.13  Distrib 5.7.42, for Linux (x86_64)
--
-- Host: localhost    Database: assignment_2024
-- ------------------------------------------------------
-- Server version	5.7.42-0ubuntu0.18.04.1

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `assets`
--

DROP TABLE IF EXISTS `assets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `assets` (
  `_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `formhub_uuid` varchar(43) NOT NULL,
  `starttime` datetime NOT NULL,
  `endtime` datetime NOT NULL,
  `cd_survey_date` date NOT NULL,
  `_status` varchar(25) NOT NULL,
  `_submission_time` datetime NOT NULL,
  `__version__` varchar(35) NOT NULL,
  `meta_instance_id` varchar(55) NOT NULL,
  `_xform_id_string` varchar(35) NOT NULL,
  `_uuid` varchar(43) NOT NULL,
  `_validation_status` json DEFAULT NULL,
  `attachments` json DEFAULT NULL,
  `notes` json DEFAULT NULL,
  `tags` json DEFAULT NULL,
  `submitted_by` varchar(60) DEFAULT NULL,
  `business_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`_id`),
  UNIQUE KEY `_uuid` (`_uuid`),
  KEY `business_id` (`business_id`),
  CONSTRAINT `assets_ibfk_1` FOREIGN KEY (`business_id`) REFERENCES `businesses` (`_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `business_groups`
--

DROP TABLE IF EXISTS `business_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `business_groups` (
  `_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `biz_status` varchar(45) NOT NULL,
  `biz_operating` varchar(35) DEFAULT NULL,
  PRIMARY KEY (`_id`),
  UNIQUE KEY `uix_status_operating` (`biz_operating`,`biz_status`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `businesses`
--

DROP TABLE IF EXISTS `businesses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `businesses` (
  `_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `bda_name` varchar(45) NOT NULL,
  `cohort` varchar(35) NOT NULL,
  `program` varchar(35) NOT NULL,
  `group_id` bigint(20) DEFAULT NULL,
  `location_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`_id`),
  UNIQUE KEY `bda_name` (`bda_name`),
  KEY `group_id` (`group_id`),
  KEY `location_id` (`location_id`),
  CONSTRAINT `businesses_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `business_groups` (`_id`),
  CONSTRAINT `businesses_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `locations` (`_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clients` (
  `_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `client_name` varchar(45) NOT NULL,
  `client_id_manifest` varchar(45) NOT NULL,
  `location` varchar(45) NOT NULL,
  `clients_phone` varchar(45) NOT NULL,
  `clients_phone_smart_feature` varchar(45) NOT NULL,
  `gender` varchar(45) NOT NULL,
  `age` varchar(45) NOT NULL,
  `nationality` varchar(45) NOT NULL,
  `strata` varchar(45) NOT NULL,
  `disability` varchar(45) NOT NULL,
  `education` varchar(45) NOT NULL,
  `client_status` varchar(45) NOT NULL,
  `sole_income_earner` varchar(45) NOT NULL,
  `howrespble_pple` int(11) NOT NULL,
  `business_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`_id`),
  UNIQUE KEY `client_id_manifest` (`client_id_manifest`),
  KEY `business_id` (`business_id`),
  CONSTRAINT `clients_ibfk_1` FOREIGN KEY (`business_id`) REFERENCES `businesses` (`_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `geolocations`
--

DROP TABLE IF EXISTS `geolocations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `geolocations` (
  `_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  PRIMARY KEY (`_id`),
  UNIQUE KEY `uix_lat_long` (`latitude`,`longitude`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locations` (
  `_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `unique_id` varchar(45) NOT NULL,
  `biz_country_name` varchar(34) NOT NULL,
  `biz_region_name` varchar(35) NOT NULL,
  `geolocation_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`_id`),
  UNIQUE KEY `unique_id` (`unique_id`),
  KEY `geolocation_id` (`geolocation_id`),
  CONSTRAINT `locations_ibfk_1` FOREIGN KEY (`geolocation_id`) REFERENCES `geolocations` (`_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-01 22:40:50
