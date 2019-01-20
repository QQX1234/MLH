-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: mei
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.16.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add good detail',7,'add_gooddetail'),(20,'Can change good detail',7,'change_gooddetail'),(21,'Can delete good detail',7,'delete_gooddetail'),(22,'Can add good list',8,'add_goodlist'),(23,'Can change good list',8,'change_goodlist'),(24,'Can delete good list',8,'delete_goodlist'),(25,'Can add user',9,'add_user'),(26,'Can change user',9,'change_user'),(27,'Can delete user',9,'delete_user'),(28,'Can add cart',10,'add_cart'),(29,'Can change cart',10,'change_cart'),(30,'Can delete cart',10,'delete_cart');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(10,'mei','cart'),(7,'mei','gooddetail'),(8,'mei','goodlist'),(9,'mei','user'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-01-14 11:34:21.454896'),(2,'auth','0001_initial','2019-01-14 11:34:21.945187'),(3,'admin','0001_initial','2019-01-14 11:34:22.168089'),(4,'admin','0002_logentry_remove_auto_add','2019-01-14 11:34:22.239359'),(5,'contenttypes','0002_remove_content_type_name','2019-01-14 11:34:22.313014'),(6,'auth','0002_alter_permission_name_max_length','2019-01-14 11:34:22.383619'),(7,'auth','0003_alter_user_email_max_length','2019-01-14 11:34:22.432197'),(8,'auth','0004_alter_user_username_opts','2019-01-14 11:34:22.442664'),(9,'auth','0005_alter_user_last_login_null','2019-01-14 11:34:22.477546'),(10,'auth','0006_require_contenttypes_0002','2019-01-14 11:34:22.480656'),(11,'auth','0007_alter_validators_add_error_messages','2019-01-14 11:34:22.491633'),(12,'auth','0008_alter_user_username_max_length','2019-01-14 11:34:22.521657'),(13,'mei','0001_initial','2019-01-14 11:34:22.613702'),(14,'sessions','0001_initial','2019-01-14 11:34:22.658501'),(15,'mei','0002_user','2019-01-15 13:19:16.086150'),(16,'mei','0003_cart','2019-01-17 08:32:28.611470'),(17,'mei','0004_auto_20190118_2054','2019-01-18 12:54:17.865010');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3orbb0vy25ykwkeeqbt5xgy292lgl87c','NjM0Nzc4NWVmNDRhYmRhYmY0NmUzZDk4ZTRiNGY4OWI1Zjc1NzIxZTp7InRva2VuIjoiZjhiZGE3M2FhOTM0OTJlOGM3N2E1YzA0MmNhMzg3ODUifQ==','2019-02-02 07:31:59.862269'),('mvczdq593895suphqh9lbzrkj6qrcalw','NzQ0NjFiNzc5ZmFmYTI1MGIzYTJjMGQxMmFmODAxODViYTFjYTBhMTp7InRva2VuIjoiNmI4NGRmMDMxMWQ0YzhkNTRkNWNhMGIxMTVmNTUzODgifQ==','2019-01-31 09:06:15.818453'),('zb7g43zcbgc3kpevreqbwpdrd9ivkkxb','NzBiMjZiOTFmOWYwMzgwNzEyNjE3NDg2ZjFiMTBiMWRlMzM4NTViYjp7InRva2VuIjoiYmM4ZTA2NDYyYzA3ZGI0NzBkMzlkZWRlZjEzMDM2Y2YifQ==','2019-02-02 11:15:27.592540');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mei_cart`
--

DROP TABLE IF EXISTS `mei_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mei_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `isselect` tinyint(1) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mei_cart_goods_id_0ca933fa_fk_mei_gooddetail_id` (`goods_id`),
  KEY `mei_cart_user_id_6d8533e1_fk_mei_user_id` (`user_id`),
  CONSTRAINT `mei_cart_goods_id_0ca933fa_fk_mei_gooddetail_id` FOREIGN KEY (`goods_id`) REFERENCES `mei_gooddetail` (`id`),
  CONSTRAINT `mei_cart_user_id_6d8533e1_fk_mei_user_id` FOREIGN KEY (`user_id`) REFERENCES `mei_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mei_cart`
--

LOCK TABLES `mei_cart` WRITE;
/*!40000 ALTER TABLE `mei_cart` DISABLE KEYS */;
INSERT INTO `mei_cart` VALUES (1,6,1,1,1),(2,2,1,2,1),(3,2,1,3,1),(4,1,1,4,1);
/*!40000 ALTER TABLE `mei_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mei_gooddetail`
--

DROP TABLE IF EXISTS `mei_gooddetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mei_gooddetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `productid` varchar(40) NOT NULL,
  `buyer` varchar(40) NOT NULL,
  `src1` varchar(80) NOT NULL,
  `src2` varchar(80) NOT NULL,
  `src3` varchar(80) NOT NULL,
  `src4` varchar(80) NOT NULL,
  `title` varchar(80) NOT NULL,
  `name` varchar(40) NOT NULL,
  `price` varchar(40) NOT NULL,
  `pri` varchar(40) NOT NULL,
  `original_price` varchar(40) NOT NULL,
  `index1` varchar(80) NOT NULL,
  `index2` varchar(80) NOT NULL,
  `index3` varchar(80) NOT NULL,
  `index4` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mei_gooddetail`
--

LOCK TABLES `mei_gooddetail` WRITE;
/*!40000 ALTER TABLE `mei_gooddetail` DISABLE KEYS */;
INSERT INTO `mei_gooddetail` VALUES (1,'product4','买手推荐','/static/img/product4_1_b.jpg','/static/img/product4_2_b.jpg','/static/img/product4_3_b.jpg','/static/img/product4_4_b.jpg','红色荔枝纹流苏翻盖双肩包','Tory Burch','￥2340','2340','￥4980','/static/img/product4_1_bs.jpg','/static/img/product4_2_bs.jpg','/static/img/product4_3_bs.jpg','/static/img/product4_4_bs.jpg'),(2,'product3','买手推荐','/static/img/product3_1_b.jpg','/static/img/product3_2_b.jpg','/static/img/product3_3_b.jpg','/static/img/product3_4_b.jpg','黑色荔枝纹Logo图案翻盖双肩包','Tory Burch','￥2190','2190','￥4380','/static/img/product3_1_bs.jpg','/static/img/product3_2_bs.jpg','/static/img/product3_3_bs.jpg','/static/img/product3_4_bs.jpg'),(3,'product2','买手推荐','/static/img/product2_1_b.jpg','/static/img/product2_2_b.jpg','/static/img/product2_3_b.jpg','/static/img/product3_4_b.jpg','黑色翻盖束带双肩包','Tory Burch','￥2540','2540','￥5080','/static/img/product2_1_bs.jpg','/static/img/product2_2_bs.jpg','/static/img/product2_3_bs.jpg','/static/img/product2_4_bs.jpg'),(4,'product1','买手推荐','/static/img/product1_1_b.jpg','/static/img/product1_2_b.jpg','/static/img/product1_3_b.jpg','/static/img/product1_4_b.jpg','红色荔枝纹拉链手提肩包','Tory Burch','￥2440','2440','￥4880','/static/img/product1_1_bs.jpg','/static/img/product1_2_bs.jpg','/static/img/product1_3_bs.jpg','/static/img/product1_4_bs.jpg');
/*!40000 ALTER TABLE `mei_gooddetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mei_goodlist`
--

DROP TABLE IF EXISTS `mei_goodlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mei_goodlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `productid` varchar(40) NOT NULL,
  `buyer` varchar(40) NOT NULL,
  `src1` varchar(80) NOT NULL,
  `src2` varchar(80) NOT NULL,
  `src3` varchar(80) NOT NULL,
  `title` varchar(80) NOT NULL,
  `name` varchar(40) NOT NULL,
  `price` varchar(40) NOT NULL,
  `original_price` varchar(40) NOT NULL,
  `index1` varchar(80) NOT NULL,
  `index2` varchar(80) NOT NULL,
  `index3` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mei_goodlist`
--

LOCK TABLES `mei_goodlist` WRITE;
/*!40000 ALTER TABLE `mei_goodlist` DISABLE KEYS */;
INSERT INTO `mei_goodlist` VALUES (1,'product4','买手推荐','/static/img/product4_1.jpg','/static/img/product4_2.jpg','/static/product4_3.jpg','红色荔枝纹流苏翻盖双肩包','Tory Burch','￥2,540','￥5,080','/static/\'img/product4_1_s.jpg','/static/\'img/product4_2_s.jpg','/static/\'img/product4_3_s.jpg'),(2,'product3','买手推荐','/static/img/product3_1.jpg','/static/img/product3_2.jpg','/static/product3_3.jpg','黑色荔枝纹Logo图案翻盖双肩包','Tory Burch','￥2,190','￥4,380','/static/\'img/product3_1_s.jpg','/static/\'img/product3_2_s.jpg','/static/\'img/product3_3_s.jpg'),(3,'product2','买手推荐','/static/img/product2_1.jpg','/static/img/product2_2.jpg','/static/product2_3.jpg','黑色翻盖束带双肩包','Tory Burch','￥2,540','￥5,080','/static/\'img/product2_1_s.jpg','/static/\'img/product2_2_s.jpg','/static/\'img/product2_3_s.jpg'),(4,'product1','买手推荐','/static/img/product1_1.jpg','/static/img/product1_2.jpg','/static/product1_3.jpg','红色荔枝纹拉链手提肩包','Tory Burch','￥2,440','￥4,880','/static/\'img/product1_1_s.jpg','/static/\'img/product1_2_s.jpg','/static/\'img/product1_3_s.jpg');
/*!40000 ALTER TABLE `mei_goodlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mei_user`
--

DROP TABLE IF EXISTS `mei_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mei_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(20) NOT NULL,
  `password` varchar(256) NOT NULL,
  `name` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `token` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mei_user`
--

LOCK TABLES `mei_user` WRITE;
/*!40000 ALTER TABLE `mei_user` DISABLE KEYS */;
INSERT INTO `mei_user` VALUES (1,'123@qq.com','e10adc3949ba59abbe56e057f20f883e','jack','13844567879','bc8e06462c07db470d39dedef13036cf');
/*!40000 ALTER TABLE `mei_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-19 22:11:20
