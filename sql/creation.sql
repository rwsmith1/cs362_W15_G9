SET FOREIGN_KEY_CHECKS=0;

/* User */
DROP TABLE IF EXISTS `User`; 
CREATE TABLE User (
  `pkUser` INT(11) NOT NULL AUTO_INCREMENT,
  `fname` VARCHAR(255) NOT NULL,
  `lname` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`pkUser`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* Student: name, email */ 
DROP TABLE IF EXISTS `Student`; 
CREATE TABLE Student (
  `pkStudent` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`pkStudent`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* Mailbox: message */ 
-- DROP TABLE IF EXISTS `Mailbox`; 
-- CREATE TABLE Mailbox (
--   `pkMailbox` INT(11) NOT NULL AUTO_INCREMENT,
--   `message` VARCHAR(255) NOT NULL,
--   PRIMARY KEY (`pkMailbox`)
-- )ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* Appointment: User_id, Student_id, time, date, location */
DROP TABLE IF EXISTS `Appointment`;
CREATE TABLE Appointment (
  `pkAppointment` INT(11) NOT NULL AUTO_INCREMENT,
  `fkUser` INT(11) DEFAULT NULL,
  `fkStudent` INT(11) DEFAULT NULL,
  `uId` VARCHAR(255) DEFAULT NULL,
  `timeStart` TIME NOT NULL,
  `timeEnd` TIME NOT NULL,
  `date` DATE NOT NULL,
  `location` VARCHAR(255) DEFAULT NULL,
  `canceled` INT(11) NOT NULL,
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
  `mailbox` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY  (`pkMessage`),
  FOREIGN KEY (`fkUser`) REFERENCES `User` (`pkUser`) ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY (`fkStudent`) REFERENCES `Student` (`pkStudent`) ON DELETE SET NULL ON UPDATE CASCADE
  )ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ALTER TABLE Message CHANGE Mailbox Mailbox VARCHAR(255)

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


