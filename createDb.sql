SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;

SET NAMES utf8mb4;

CREATE DATABASE `digigarden` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `digigarden`;

DROP TABLE IF EXISTS `piData`;
CREATE TABLE `piData` (
  `recordTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `hostname` varchar(64) NOT NULL,
  `wlan_ipaddress` varchar(64) NOT NULL,
  `free_space` bigint NOT NULL,
  `pi_temperature` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `solarControllerData`;
CREATE TABLE `solarControllerData` (
  `recordTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `batteryVoltage` float NOT NULL,
  `solarVoltage` float NOT NULL,
  `chargingCurrent` float NOT NULL,
  `loadCurrent` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
