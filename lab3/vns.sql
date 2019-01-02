-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema VNS
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema VNS
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `VNS` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `VNS` ;

-- -----------------------------------------------------
-- Table `VNS`.`Professor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VNS`.`Professor` (
  `professor_id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(20) NOT NULL,
  `mid_name` VARCHAR(20) NOT NULL,
  `last_name` VARCHAR(20) NOT NULL,
  `email` VARCHAR(20) NOT NULL,
  `department` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`professor_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `VNS`.`Courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VNS`.`Courses` (
  `course_id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(20) NOT NULL,
  `description` VARCHAR(200) NULL DEFAULT NULL,
  `number_of_lectures` INT(11) NOT NULL,
  `Professor_professor_id` INT(11) NOT NULL,
  PRIMARY KEY (`course_id`),
  INDEX `fk_Courses_Professor1_idx` (`Professor_professor_id` ASC),
  CONSTRAINT `fk_Courses_Professor1`
    FOREIGN KEY (`Professor_professor_id`)
    REFERENCES `VNS`.`Professor` (`professor_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `VNS`.`Students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VNS`.`Students` (
  `student_id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(20) NOT NULL,
  `mid_name` VARCHAR(20) NOT NULL,
  `last_name` VARCHAR(20) NOT NULL,
  `email` VARCHAR(20) NOT NULL,
  `year_of_study` INT(11) NOT NULL,
  PRIMARY KEY (`student_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `VNS`.`Application`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VNS`.`Application` (
  `application_id` INT(11) NOT NULL AUTO_INCREMENT,
  `status` TINYINT(1) NULL DEFAULT NULL,
  `Courses_course_id` INT(11) NOT NULL,
  `Students_student_id` INT(11) NOT NULL,
  PRIMARY KEY (`application_id`),
  INDEX `fk_Application_Courses1_idx` (`Courses_course_id` ASC),
  INDEX `fk_Application_Students1_idx` (`Students_student_id` ASC),
  CONSTRAINT `fk_Application_Courses1`
    FOREIGN KEY (`Courses_course_id`)
    REFERENCES `VNS`.`Courses` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Application_Students1`
    FOREIGN KEY (`Students_student_id`)
    REFERENCES `VNS`.`Students` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `VNS`.`Students_has_Courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VNS`.`Students_has_Courses` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `Students_student_id` INT(11) NOT NULL,
  `Courses_course_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`, `Students_student_id`, `Courses_course_id`),
  INDEX `fk_Students_has_Courses_Courses1_idx` (`Courses_course_id` ASC),
  INDEX `fk_Students_has_Courses_Students1_idx` (`Students_student_id` ASC),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  CONSTRAINT `fk_Students_has_Courses_Students1`
    FOREIGN KEY (`Students_student_id`)
    REFERENCES `VNS`.`Students` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Students_has_Courses_Courses1`
    FOREIGN KEY (`Courses_course_id`)
    REFERENCES `VNS`.`Courses` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
