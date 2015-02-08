SET FOREIGN_KEY_CHECKS=0;

/* User */
DROP TABLE IF EXISTS `User`; 
CREATE TABLE User (
  `pkUser` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`pkUser`),
  UNIQUE KEY `email` (`email`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* Student: name, email */ 
DROP TABLE IF EXISTS `Student`; 
CREATE TABLE Student (
  `pkStudent` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`pkStudent`),
  UNIQUE KEY `email` (`email`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* Mailbox: message */ 
DROP TABLE IF EXISTS `Mailbox`; 
-- CREATE TABLE Mailbox (
--   `pkMailbox` INT(11) NOT NULL AUTO_INCREMENT,
--   `message` VARCHAR(255) NOT NULL,
--   PRIMARY KEY (`pkMailbox`)
-- )ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* Appiontment: User_id, Student_id, time, date, location */
DROP TABLE IF EXISTS `Appiontment`;
CREATE TABLE Appiontment (
  `pkMessage` INT(11) NOT NULL AUTO_INCREMENT,
  `fkUser` INT(11) DEFAULT NULL,
  `fkStudent` INT(11) DEFAULT NULL,
  `time` INT(11) NOT NULL,
  `date` DATE NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  PRIMARY KEY  (`pkMessage`),
  FOREIGN KEY (`fkUser`) REFERENCES `User` (`pkUser`) ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY (`fkStudent`) REFERENCES `Student` (`pkStudent`) ON DELETE SET NULL ON UPDATE CASCADE
  )ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* Message: User, Student, Mailbox */
DROP TABLE IF EXISTS `Message`;
CREATE TABLE Message (
  `pkMessage` INT(11) NOT NULL AUTO_INCREMENT,
  `fkUser` INT(11) DEFAULT NULL,
  `fkStudent` INT(11) DEFAULT NULL,
  `fkMailbox` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY  (`pkMessage`),
  FOREIGN KEY (`fkUser`) REFERENCES `User` (`pkUser`) ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY (`fkStudent`) REFERENCES `Student` (`pkStudent`) ON DELETE SET NULL ON UPDATE CASCADE
  )ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS=0;

/* User */
DROP TABLE IF EXISTS `User`; 
CREATE TABLE User (
  `pkUser` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`pkUser`),
  UNIQUE KEY `email` (`email`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* Student: name, email */ 
DROP TABLE IF EXISTS `Student`; 
CREATE TABLE Student (
  `pkStudent` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`pkStudent`),
  UNIQUE KEY `email` (`email`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* Mailbox: message */ 
DROP TABLE IF EXISTS `Mailbox`; 
-- CREATE TABLE Mailbox (
--   `pkMailbox` INT(11) NOT NULL AUTO_INCREMENT,
--   `message` VARCHAR(255) NOT NULL,
--   PRIMARY KEY (`pkMailbox`)
-- )ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* Appiontment: User_id, Student_id, time, date, location */
DROP TABLE IF EXISTS `Appiontment`;
CREATE TABLE Appiontment (
  `pkMessage` INT(11) NOT NULL AUTO_INCREMENT,
  `fkUser` INT(11) DEFAULT NULL,
  `fkStudent` INT(11) DEFAULT NULL,
  `time` INT(11) NOT NULL,
  `date` DATE NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  PRIMARY KEY  (`pkMessage`),
  FOREIGN KEY (`fkUser`) REFERENCES `User` (`pkUser`) ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY (`fkStudent`) REFERENCES `Student` (`pkStudent`) ON DELETE SET NULL ON UPDATE CASCADE
  )ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* Message: User, Student, Mailbox */
-- DROP TABLE IF EXISTS `Message`;
-- CREATE TABLE Message (
--   `pkMessage` INT(11) NOT NULL AUTO_INCREMENT,
--   `fkUser` INT(11) DEFAULT NULL,
--   `fkStudent` INT(11) DEFAULT NULL,
--   `fkMailbox` INT(11) DEFAULT NULL,
--   PRIMARY KEY  (`pkMessage`),
--   FOREIGN KEY (`fkUser`) REFERENCES `User` (`pkUser`) ON DELETE SET NULL ON UPDATE CASCADE,
--   FOREIGN KEY (`fkStudent`) REFERENCES `Student` (`pkStudent`) ON DELETE SET NULL ON UPDATE CASCADE,
--   FOREIGN KEY (`fkMailbox`) REFERENCES `Mailbox` (`pkMailbox`) ON DELETE SET NULL ON UPDATE CASCADE
--   )ENGINE=InnoDB DEFAULT CHARSET=utf8;


