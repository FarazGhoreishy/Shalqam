-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: shalqam
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `favorites`
--

DROP TABLE IF EXISTS `favorites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favorites` (
  `user_id` int NOT NULL,
  `item_id` int NOT NULL,
  `fav_id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`fav_id`),
  UNIQUE KEY `fav_id_UNIQUE` (`fav_id`),
  KEY `user_id_idx` (`user_id`),
  KEY `item_id_idx` (`item_id`),
  CONSTRAINT `item_id` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorites`
--

LOCK TABLES `favorites` WRITE;
/*!40000 ALTER TABLE `favorites` DISABLE KEYS */;
/*!40000 ALTER TABLE `favorites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `name` longtext NOT NULL,
  `category` longtext NOT NULL,
  `main_link` longtext NOT NULL,
  `price` mediumtext NOT NULL,
  PRIMARY KEY (`item_id`),
  UNIQUE KEY `item_id_UNIQUE` (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (80,'هدست گیمینگ ریزر KRAKEN X','هدست و هدفون','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_%D9%87%D8%AF%D8%B3%D8%AA-%DA%AF%DB%8C%D9%85%DB%8C%D9%86%DA%AF-%D8%B1%DB%8C%D8%B2%D8%B1-KRAKEN-X~id~2926787','۱,۳۶۰,۰۰۰'),(81,'Razer Blackshark V2 Pro','هدست و هدفون','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_Razer-Blackshark-V2-Pro~id~4197417','۶,۹۹۰,۰۰۰'),(82,'Blackshark V2 Headset','هدست و هدفون','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_Blackshark-V2-Headset~id~4172655','۴,۱۹۰,۰۰۰'),(83,'TSCO TH 5127 Wired Gaming Headset','هدست و هدفون','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_TSCO-TH-5127-Wired-Gaming-Headset~id~2883522','۳۷۸,۰۰۰'),(92,'Huawei EchoLife HG8245Q2 Optical Network Terminal','تجهیزات شبکه','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_Huawei-EchoLife-HG8245Q2-Optical-Network-Terminal~id~7370373','۱,۴۲۰,۰۰۰'),(93,'HUAWEI EchoLife HG8245C Optical Network Terminal','تجهیزات شبکه','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_HUAWEI-EchoLife-HG8245C-Optical-Network-Terminal~id~4438285','۹۴۰,۰۰۰'),(94,'مودم فیبر نوری فایبرهوم AN5506-02FG','تجهیزات شبکه','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_%D9%85%D9%88%D8%AF%D9%85-%D9%81%DB%8C%D8%A8%D8%B1-%D9%86%D9%88%D8%B1%DB%8C-%D9%81%D8%A7%DB%8C%D8%A8%D8%B1%D9%87%D9%88%D9%85-AN5506-02FG~id~4977080','۱,۳۸۵,۰۰۰'),(95,'Huawei HS8546V5 dual fiber optic modem','تجهیزات شبکه','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_Huawei-HS8546V5-dual-fiber-optic-modem~id~7789415','۲,۲۰۰,۰۰۰'),(96,'کتونی آدیداس مردانه کد 33','کیف و کفش','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_%DA%A9%D8%AA%D9%88%D9%86%DB%8C-%D8%A2%D8%AF%DB%8C%D8%AF%D8%A7%D8%B3-%D9%85%D8%B1%D8%AF%D8%A7%D9%86%D9%87-%DA%A9%D8%AF-33~id~5056885','۳۹۰,۰۰۰'),(97,'کتونی زنانه و مردانه آدیداس استیر Adidas Astir','کیف و کفش','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_%DA%A9%D8%AA%D9%88%D9%86%DB%8C-%D8%B2%D9%86%D8%A7%D9%86%D9%87-%D9%88-%D9%85%D8%B1%D8%AF%D8%A7%D9%86%D9%87-%D8%A2%D8%AF%DB%8C%D8%AF%D8%A7%D8%B3-%D8%A7%D8%B3%D8%AA%DB%8C%D8%B1-Adidas-Astir-~id~14308288','۲,۶۳۰,۰۰۰'),(98,'کفش آدیداس مردانه Q46228','کیف و کفش','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_%DA%A9%D9%81%D8%B4-%D8%A2%D8%AF%DB%8C%D8%AF%D8%A7%D8%B3-%D9%85%D8%B1%D8%AF%D8%A7%D9%86%D9%87-Q46228~id~4859141','۱۵۵,۰۰۰'),(99,'کفش آدیداس مردانه کد 865','کیف و کفش','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_%DA%A9%D9%81%D8%B4-%D8%A2%D8%AF%DB%8C%D8%AF%D8%A7%D8%B3-%D9%85%D8%B1%D8%AF%D8%A7%D9%86%D9%87-%DA%A9%D8%AF-865~id~7966960','۲۴۹,۰۰۰'),(100,'پازل 500 تکه راونزبرگر مدل سگ های وفادار من','اسباب بازی','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_%D9%BE%D8%A7%D8%B2%D9%84-500-%D8%AA%DA%A9%D9%87-%D8%B1%D8%A7%D9%88%D9%86%D8%B2%D8%A8%D8%B1%DA%AF%D8%B1-%D9%85%D8%AF%D9%84-%D8%B3%DA%AF-%D9%87%D8%A7%DB%8C-%D9%88%D9%81%D8%A7%D8%AF%D8%A7%D8%B1-%D9%85%D9%86~id~8231378','۸۲۰,۰۰۰'),(101,'پازل 500 تکه راونزبرگر مدل گل‌ها و کلاه‌ها','اسباب بازی','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_%D9%BE%D8%A7%D8%B2%D9%84-500-%D8%AA%DA%A9%D9%87-%D8%B1%D8%A7%D9%88%D9%86%D8%B2%D8%A8%D8%B1%DA%AF%D8%B1-%D9%85%D8%AF%D9%84-%DA%AF%D9%84%E2%80%8C%D9%87%D8%A7-%D9%88-%DA%A9%D9%84%D8%A7%D9%87%E2%80%8C%D9%87%D8%A7~id~15676854','۱,۱۰۰,۰۰۰'),(102,'پازل 500 تکه راونزبرگر مدل کشتی‌های درخشان','اسباب بازی','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_%D9%BE%D8%A7%D8%B2%D9%84-500-%D8%AA%DA%A9%D9%87-%D8%B1%D8%A7%D9%88%D9%86%D8%B2%D8%A8%D8%B1%DA%AF%D8%B1-%D9%85%D8%AF%D9%84-%DA%A9%D8%B4%D8%AA%DB%8C%E2%80%8C%D9%87%D8%A7%DB%8C-%D8%AF%D8%B1%D8%AE%D8%B4%D8%A7%D9%86~id~15676855','۱,۱۰۰,۰۰۰'),(103,'پازل500 تکه راونزبرگر مدل اتاق موسیقی','اسباب بازی','https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_%D9%BE%D8%A7%D8%B2%D9%84500-%D8%AA%DA%A9%D9%87-%D8%B1%D8%A7%D9%88%D9%86%D8%B2%D8%A8%D8%B1%DA%AF%D8%B1-%D9%85%D8%AF%D9%84-%D8%A7%D8%AA%D8%A7%D9%82-%D9%85%D9%88%D8%B3%DB%8C%D9%82%DB%8C~id~8227387','۷۵۰,۰۰۰');
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `links`
--

DROP TABLE IF EXISTS `links`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `links` (
  `link_id` int NOT NULL AUTO_INCREMENT,
  `item_id` int NOT NULL,
  `link` longtext NOT NULL,
  PRIMARY KEY (`link_id`),
  UNIQUE KEY `link_id_UNIQUE` (`link_id`),
  KEY `item_id_to_links_idx` (`item_id`),
  CONSTRAINT `item_id_to_links` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=339 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `links`
--

LOCK TABLES `links` WRITE;
/*!40000 ALTER TABLE `links` DISABLE KEYS */;
INSERT INTO `links` VALUES (267,80,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%85%d8%a7%db%8c-%d8%b1%db%8c%d8%b2%d8%b1~eitemid~2926787~exid~151440502~fp~ZEZiaUkvSG96Mit5akk1NXp6a3V4R1ZOeVdwM0JLWmMwNHY4MjRKTTFJOD0!'),(268,80,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%aa%da%a9-%d8%b3%db%8c%d8%b3%d8%aa%d9%85~eitemid~2926787~exid~121918010~fp~TFhSRkFDMVFVVTl4TVFqcGZhbktCdXlaT2UxRGxwWjM4cnpnU21PbjJmcz0!'),(269,80,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%a2%d8%b4%db%8c%d9%84-%d8%b1%d8%a7%db%8c%d8%a7%d9%86~eitemid~2926787~exid~163835356~fp~d3FxMjRGODNFY1lMS3hMYUlGVStuMHhiQTRHR2dmKzVId3hrUWw0VjRJcz0!'),(270,80,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%be%d8%a7%d9%84-%d8%a7%d8%b3%d8%aa%d9%88%d8%b1~eitemid~2926787~exid~143605036~fp~S1E1ZlpoTVBadUphMXhNTTNSUlo0VzdLMnJKN0xQS2ZnNW94bGNkSkQ1MD0!'),(271,81,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%aa%d8%a7%d9%be-%d8%b1%d8%a7%db%8c%d8%a7%d9%86~eitemid~4197417~exid~186047701~fp~d3hRV2drSzFGNVRlRE1kYXhhUVkzdWZZdjF3SUZNZXJNd3NlTjgxOWNnUT0!'),(272,81,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%aa%da%a9-%d8%b3%db%8c%d8%b3%d8%aa%d9%85~eitemid~4197417~exid~121306010~fp~RHdHUlFlT1pzUkMrdDhVOHlodHNPejNBS2xMNnFmZ2tTZGRvVzBqQkVuMD0!'),(273,81,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%85%d8%a7%db%8c-%d8%b1%db%8c%d8%b2%d8%b1~eitemid~4197417~exid~183449205~fp~STNTeXBkMlgxK1ArSVp5NkRCMERRa0dzcURsaHNkVnI4aE1XYXdmSVQzRT0!'),(274,81,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%aa%da%a9%d8%a7%d9%81~eitemid~4197417~exid~81792472~fp~L2MzSXZraTl6ejJCNFZRSVdKRVVVUyt1UnlIR3R6R3F0WnBZaE8xK3FIQT0!'),(275,82,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%aa%d8%a7%d9%be-%d8%b1%d8%a7%db%8c%d8%a7%d9%86~eitemid~4172655~exid~185221975~fp~NDZyeVh4T3FkTktnLzlia1d4eTJkM0Q5L2tpL1prUVpxazRXSnlZam9vVT0!'),(276,82,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%85%d8%a7%db%8c-%d8%b1%db%8c%d8%b2%d8%b1~eitemid~4172655~exid~162157768~fp~bkFjdzdiT3NjZWVOTG5IZFZLd0MyMHdlZ0VqS2FERi9GQkNzUlRWMTJvbz0!'),(277,82,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%aa%da%a9-%d8%b3%db%8c%d8%b3%d8%aa%d9%85~eitemid~4172655~exid~114953684~fp~aVJiTENJdmlnV0tzZDd6RFFJdE1Ba3JETHY4VFdpaitUZTd4cGNyM21Ndz0!'),(278,82,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%aa%da%a9%d8%a7%d9%81~eitemid~4172655~exid~54704920~fp~anFrMCs3L1FDSndkZk4zTjJma0x0WW81aVYrc296MVBZUncxVEZVWDhEOD0!'),(279,83,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%aa%d8%a7%d9%be-%d8%b1%d8%a7%db%8c%d8%a7%d9%86~eitemid~2883522~exid~132603492~fp~YTBOQ25ZclB2allHMFBRaGpCTVVhOEh2bFgwbUJ0NEtwNnBkbzNwR0R5OD0!'),(280,83,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%85%d8%b1%da%a9%d8%b2-%da%a9%d9%86%d8%aa%d8%b1%d9%84-%da%a9%d8%a7%d9%85%d9%be%db%8c%d9%88%d8%aa%d8%b1-%d9%be%d8%a7%d8%b1%d8%b3%db%8c%d8%a7%d9%86~eitemid~2883522~exid~102266948~fp~ZjBwdjZwTlB3UlZUOVpTVUlHek1IY0dmcGxRNnRKL0h2UHFkYyt5dDNHYz0!'),(281,83,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%81%d8%b1%d9%88%d8%b4%da%af%d8%a7%d9%87-%d8%aa%d8%ae%d9%81%db%8c%d9%81%d8%a7%d9%86~eitemid~2883522~exid~177550704~fp~dWd4YTFnNjI1RFIrVXZqcyt6Vkd5VjhKRmIxYWxqK1cveWxkY2hVSisyND0!'),(282,83,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%af%db%8c%d8%ac%db%8c-%da%a9%d8%a7%d9%84%d8%a7~eitemid~2883522~exid~27935098~fp~cmQ0MGZDT1VaQWRReEFlVHB1K0xib2lXOHMvMnllTGd2d0hNNENsMlR2MD0!'),(307,92,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%a2%db%8c-%d8%aa%db%8c-%d8%b4%d8%a8%da%a9%d9%87~eitemid~7370373~exid~144471559~fp~UTkvZ1UweTdjcVkwWC9tY3FpMDRiRTZKcUlXMHhYc204ZWdmem5PeWlwYz0!'),(308,92,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%84%d8%a7%db%8c%d9%86-%d9%86%d8%aa~eitemid~7370373~exid~167657575~fp~d2d2Qmx3MHpOQjFuRFVQODUreVZwUjAwWFg0dlcrQy9rbVdyWDlhTStkRT0!'),(309,92,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%af%db%8c%d8%ac%db%8c-%da%a9%d8%a7%d9%84%d8%a7~eitemid~7370373~exid~171962574~fp~SC9lalpBQm5haWNnclhCREFYSG0veitSbXZMSFVVM0V2clZHU0lIdEozND0!'),(310,93,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%a2%db%8c-%d8%aa%db%8c-%d8%b4%d8%a8%da%a9%d9%87~eitemid~4438285~exid~71903553~fp~RkN5ZVZ4UmZyQnRWeTZMTEFHNVpNUVdzcXZ5N2I5QXVWSml0UWNwZndQdz0!'),(311,93,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%84%d8%a7%db%8c%d9%86-%d9%86%d8%aa~eitemid~4438285~exid~167565999~fp~My8zUTB0RElibFd1ZXVpTFpWaFdQNG1DeThZSmk5Wk9tbE83aThJTTNCdz0!'),(312,93,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%85%d8%b1%da%a9%d8%b2-%da%a9%d9%86%d8%aa%d8%b1%d9%84-%da%a9%d8%a7%d9%85%d9%be%db%8c%d9%88%d8%aa%d8%b1-%d9%be%d8%a7%d8%b1%d8%b3%db%8c%d8%a7%d9%86~eitemid~4438285~exid~144377599~fp~NWQ2aXJPczlhcDZhaGVCSDg0UUlFdTZNL2lFNGFEajhlM2Q5WTFHbyttQT0!'),(313,94,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%84%d8%a7%db%8c%d9%86-%d9%86%d8%aa~eitemid~4977080~exid~167590666~fp~UXJYSkQzd2F2VDh1c0J6WW53TVdDbE5TVEZwYmZjMU0yUjI5b2Uvd3RFWT0!'),(314,94,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%aa%da%a9%d9%86%d9%88%d9%84%db%8c%d9%86%da%a9~eitemid~4977080~exid~177101253~fp~UVRQc3BoL2JIaUtmdVFVZTlFQkdrWEpkMFZRbzZZdUFleU9CWENqZ0Y0MD0!'),(315,94,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%af%db%8c%d8%ac%db%8c-%da%a9%d8%a7%d9%84%d8%a7~eitemid~4977080~exid~123132543~fp~bENLLzBDQXlCQXdMVHVUaVExMmVJdjl5VkY4SnlyRFVFZ2pwVlJ2SFdBcz0!'),(316,95,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%84%d8%a7%db%8c%d9%86-%d9%86%d8%aa~eitemid~7789415~exid~167566001~fp~QXN2WjZpRFV3c1Vpd2lDRzNneGp5SkhlcHJUREQ1MG12NUxHVmVjNVdNaz0!'),(317,95,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%db%8c%d8%a7%d8%b3-%d8%a7%d8%b1%d8%aa%d8%a8%d8%a7%d8%b7~eitemid~7789415~exid~169235815~fp~RFl3dlR6cjc0VHVkQ05uQkVKM1llSWk5K3gvam5ZaFVEM3pJL0xaZG5qVT0!'),(318,95,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%a8%d8%b1%d9%82%da%86%db%8c~eitemid~7789415~exid~117812347~fp~cytSamZRSHZ2ajVreG9KN0N1dElVMGFJL0RKdC9kTFR4dXJ6N2ZkYWZnZz0!'),(319,96,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%85%db%8c%d9%86%db%8c-%da%a9%d8%a7%d9%84%d8%a7~eitemid~5056885~exid~181262261~fp~R2FGTW5kNFJDdmJNditHNmRyUXp0TVRlbVpCRU5Jei91NXl6ZFlxVzljbz0!'),(320,96,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%a8%d8%a7-%d8%b3%d9%84%d8%a7%d9%85~eitemid~5056885~exid~178370532~fp~L3lLcGJGODVWeW91V1RnZnRCVkNRYjdkT2IwVFZzY3Jlb2ExbmJTYzk0ND0!'),(321,96,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%da%a9%d9%81%d8%b4-%d9%be%d8%a7%d8%b1%d8%b3%d8%a7~eitemid~5056885~exid~178187070~fp~MU45bDRRUFFUaGEwTHJTcXRCbnFPeVJlckdRYy92K2VtRmVHY3ZXaG1ZST0!'),(322,97,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%da%a9%d8%a7%d8%b1%d8%a7%d9%86-%da%a9%d8%aa%d9%88%d9%86%db%8c~eitemid~14308288~exid~181428404~fp~Y0FBWFJQNXdtbXFMbkxHRmZGOEFWOFloSm1LVXJyL0lFNUdLZXdjZlZ0ST0!'),(323,97,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%da%a9%d8%a7%d8%b1%d8%a7%d9%86-%da%a9%d8%aa%d9%88%d9%86%db%8c~eitemid~14308288~exid~181428405~fp~aEdjV3VZSEtNYjdXOTJOM0RvaHRWOHgxeHU5eEpOemJXWGNNRTBHRmdzdz0!'),(324,97,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%da%a9%d8%a7%d8%b1%d8%a7%d9%86-%da%a9%d8%aa%d9%88%d9%86%db%8c~eitemid~14308288~exid~181428406~fp~b1c0VmdMSlRnTjdNNEJMbkFPMGRBblo4Q3VHS2w4aXNtTTNmYm42QlRlST0!'),(325,98,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%a8%d8%a7-%d8%b3%d9%84%d8%a7%d9%85~eitemid~4859141~exid~189991737~fp~aXZtOWxJOTMxTnJHRjlhYTdFbEkyR2JyWkVuZjVabXR4STBpa1gycFBZUT0!'),(326,98,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%81%d8%b1%d9%88%d8%b4%da%af%d8%a7%d9%87-%d9%87%d8%b1%d8%aa-%da%a9%d8%a7%d9%84%d8%a7~eitemid~4859141~exid~178143360~fp~Sms3OTZ1VStScytXTEQwK0Z4TGE2bTJjTkFpS0l2RzJyVSt4TGVvU0dqUT0!'),(327,98,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%85%db%8c%d9%86%db%8c-%da%a9%d8%a7%d9%84%d8%a7~eitemid~4859141~exid~186903256~fp~ZGR4dnE4Z240SmNYNzYvR3hYV2RURWNZTzdUUjF1VUNBYjVYT3lCcmptQT0!'),(328,99,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%a8%d8%a7-%d8%b3%d9%84%d8%a7%d9%85~eitemid~7966960~exid~188959535~fp~QlZTNEdKZ3NETURTWmNRRnFMZGwwSmY4bmhVQVVHaVk5eFBLT05jVkE3Yz0!'),(329,99,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d9%85%db%8c%d9%86%db%8c-%da%a9%d8%a7%d9%84%d8%a7~eitemid~7966960~exid~189561352~fp~dnNyWHVVWWVNK2VZYlJiaFlON3lIMWVGUEhFNFZoYy95NlN3U0lwclg4TT0!'),(330,99,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%a8%d8%a7-%d8%b3%d9%84%d8%a7%d9%85~eitemid~7966960~exid~129050792~fp~ZW8vU1MvUlNiTTJjcmFxb0tXeDJMbGl3blVtWnE0MGpLVmoxUmRiMTNUST0!'),(331,100,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%af%db%8c%d8%ac%db%8c-%da%a9%d8%a7%d9%84%d8%a7~eitemid~8231378~exid~143408378~fp~RUpQS0d0bWl1a0RlVG91VWgyYmIyeFlOdW5WeE44V09hby9QSVRqenp0dz0!'),(332,100,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%db%8c%d9%88%db%8c%d9%88-%d9%86%db%8c-%d9%86%db%8c~eitemid~8231378~exid~190359391~fp~WWh6WTRxS21MZWQ0c2xSZWc3OGtvc0cwakpzNS9jRUlTUGZMcWN0dGVyaz0!'),(333,101,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%af%db%8c%d8%ac%db%8c-%da%a9%d8%a7%d9%84%d8%a7~eitemid~15676854~exid~180485611~fp~RkNRVEJIYkJ0aXlOZFR0ZUlWVFhzOVNON2ZNR2NkQnNWQjJ0NDJ4WHlPWT0!'),(334,101,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%db%8c%d9%88%db%8c%d9%88-%d9%86%db%8c-%d9%86%db%8c~eitemid~15676854~exid~190367162~fp~eGtOb2dkZ3ByT0hES25McDlQcVZraFVkUUZuYmpzUThCbzQrbUZadmkvYz0!'),(335,102,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%af%db%8c%d8%ac%db%8c-%da%a9%d8%a7%d9%84%d8%a7~eitemid~15676855~exid~180485613~fp~eVBCYS9GYjBqSDA1YURIQmNNbkYyQngrdlFRZ2xaZWlWRWpaN1V2NXRJaz0!'),(336,102,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%db%8c%d9%88%db%8c%d9%88-%d9%86%db%8c-%d9%86%db%8c~eitemid~15676855~exid~190367251~fp~SVlmVzI5UlVLd05OblRsSzlNVDBCdjhmbWFTYU1NTW44QnFHOWszVVlVTT0!'),(337,103,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%d8%af%db%8c%d8%ac%db%8c-%da%a9%d8%a7%d9%84%d8%a7~eitemid~8227387~exid~142057603~fp~TWxzeVE5SGFxcGZIQjlVUUdvOVU1Yjg4emMwRG5Da1M2SWpjNmVvcnlZaz0!'),(338,103,'http://emalls.ir/%d8%ae%d8%b1%db%8c%d8%af_%db%8c%d9%88%db%8c%d9%88-%d9%86%db%8c-%d9%86%db%8c~eitemid~8227387~exid~190367254~fp~eWp5RVdMVmtyL2xULzdacUlNdi9wd0xRNnM1bkdtajdMWE1tUDM0eityUT0!');
/*!40000 ALTER TABLE `links` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` varchar(64) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (11,'test_user','13d249f2cb4127b40cfa757866850278793f814ded3c587fe5889e889a7a9f6c','Fname','Lname','test@email.com');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-06 20:45:56
