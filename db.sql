-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`user` (
  `CNo` INT NOT NULL,
  `Cname` VARCHAR(45) NULL,
  `Cmail` VARCHAR(45) NULL,
  `identify_INo` INT NOT NULL,
  PRIMARY KEY (`CNo`, `identify_INo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`movie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`movie` (
  `MNo` INT NOT NULL,
  `Mview` VARCHAR(45) NULL,
  `Mactor` VARCHAR(45) NULL,
  `Mdic` VARCHAR(45) NULL,
  `Mtime` VARCHAR(45) NULL,
  `Mgenre` VARCHAR(45) NULL,
  `Mname` VARCHAR(45) NULL,
  `Murl` VARCHAR(45) NULL,
  `Mposter` VARCHAR(45) NULL,
  PRIMARY KEY (`MNo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Review`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Review` (
  `RNo` INT NOT NULL,
  `Ruser` VARCHAR(45) NOT NULL,
  `Rstar` INT NULL,
  `Rident` INT NOT NULL,
  `Rreview` VARCHAR(500) NOT NULL,
  `Rsite` INT NOT NULL,
  `favorite_FNo` INT NOT NULL,
  PRIMARY KEY (`RNo`, `favorite_FNo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`identify`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`identify` (
  `user_CNo` INT NOT NULL,
  `user_identify_INo` INT NOT NULL,
  `Review_RNo` INT NOT NULL,
  `Review_favorite_FNo` INT NOT NULL,
  PRIMARY KEY (`user_CNo`, `user_identify_INo`, `Review_RNo`, `Review_favorite_FNo`),
  INDEX `fk_identify_user1_idx` (`user_CNo` ASC, `user_identify_INo` ASC),
  INDEX `fk_identify_Review1_idx` (`Review_RNo` ASC, `Review_favorite_FNo` ASC),
  CONSTRAINT `fk_identify_user1`
    FOREIGN KEY (`user_CNo` , `user_identify_INo`)
    REFERENCES `mydb`.`user` (`CNo` , `identify_INo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_identify_Review1`
    FOREIGN KEY (`Review_RNo` , `Review_favorite_FNo`)
    REFERENCES `mydb`.`Review` (`RNo` , `favorite_FNo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`favorite`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`favorite` (
  `FNo` INT NOT NULL,
  `Review_RNo` INT NOT NULL,
  `Review_favorite_FNo` INT NOT NULL,
  `movie_MNo` INT NOT NULL,
  PRIMARY KEY (`FNo`, `Review_RNo`, `Review_favorite_FNo`, `movie_MNo`),
  INDEX `fk_favorite_Review1_idx` (`Review_RNo` ASC, `Review_favorite_FNo` ASC),
  INDEX `fk_favorite_movie1_idx` (`movie_MNo` ASC),
  CONSTRAINT `fk_favorite_Review1`
    FOREIGN KEY (`Review_RNo` , `Review_favorite_FNo`)
    REFERENCES `mydb`.`Review` (`RNo` , `favorite_FNo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorite_movie1`
    FOREIGN KEY (`movie_MNo`)
    REFERENCES `mydb`.`movie` (`MNo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
