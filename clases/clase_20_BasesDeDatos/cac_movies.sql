CREATE DATABASE  IF NOT EXISTS `cac-movies` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cac-movies`;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;

CREATE TABLE `genres` (
  `id_genre` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id_genre`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `movies`;

CREATE TABLE `movies` (
  `id_movie` int NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `release_year` int DEFAULT '2024',
  `adult` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id_movie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `reviews`;

CREATE TABLE `reviews` (
  `id_review` INT NOT NULL AUTO_INCREMENT,
  `id_movie` INT NULL,
  `reviewer_name` VARCHAR(100) NULL,
  `comment` TEXT NULL,
  `rating` DECIMAL(4,2) NULL,
  PRIMARY KEY (`id_review`));

ALTER TABLE `reviews` 
ADD INDEX `fk_movie_idx` (`id_movie` ASC) VISIBLE;
;
ALTER TABLE `reviews` 
ADD CONSTRAINT `fk_movie`
  FOREIGN KEY (`id_movie`)
  REFERENCES `movies` (`id_movie`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;


DROP TABLE IF EXISTS `movies_genres`;

CREATE TABLE `movies_genres` (
  `id_movie_genre` int NOT NULL AUTO_INCREMENT,
  `id_movie` int DEFAULT NULL,
  `id_genre` int DEFAULT NULL,
  PRIMARY KEY (`id_movie_genre`),
  KEY `FK1_movie_idx` (`id_movie`),
  KEY `FK2_idx` (`id_genre`),
  CONSTRAINT `FK1_movie` FOREIGN KEY (`id_movie`) REFERENCES `movies` (`id_movie`),
  CONSTRAINT `FK2` FOREIGN KEY (`id_genre`) REFERENCES `genres` (`id_genre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* INSERTS */
-- generos
INSERT INTO genres (name) VALUES ('Acción');
INSERT INTO genres (name) VALUES ('Comedia');
INSERT INTO genres (name) VALUES ('Drama');
INSERT INTO genres (name) VALUES ('Ciencia Ficción');
INSERT INTO genres (name) VALUES ('Romance');
INSERT INTO genres (name) VALUES ('Terror');
INSERT INTO genres (name) VALUES ('Aventura');
INSERT INTO genres (name) VALUES ('Animación');
INSERT INTO genres (name) VALUES ('Fantasía');
INSERT INTO genres (name) VALUES ('Documental');

-- peliculas
INSERT INTO movies (title, release_year, adult) VALUES ('El Señor de los Anillos: La Comunidad del Anillo', 2021, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Pulp Fiction', 1994, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Titanic', 1997, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Forrest Gump', 1994, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('El Rey León', 1994, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('El Padrino', 1972, 1);
INSERT INTO movies (title, release_year, adult) VALUES ('Interestelar', 2014, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Harry Potter y la piedra filosofal', 2001, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('La La Land', 2016, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('El club de la lucha', 1999, 0);

-- Asociación de "El Señor de los Anillos: La Comunidad del Anillo" con los géneros "Acción" y "Aventura"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (1, 1), (1, 7);

-- Asociación de "Pulp Fiction" con los géneros "Drama" y "Crimen"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (2, 3), (2, 8);

-- Asociación de "Titanic" con los géneros "Romance" y "Drama"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (3, 5), (3, 3);

-- Asociación de "Forrest Gump" con el género "Drama"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (4, 3);

-- Asociación de "El Rey León" con los géneros "Animación" y "Aventura"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (5, 8), (5, 7);

-- Asociación de "El Padrino" con los géneros "Drama" y "Crimen"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (6, 3), (6, 8);

-- Asociación de "Interestelar" con el género "Ciencia Ficción"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (7, 4);

-- Asociación de "Harry Potter y la piedra filosofal" con los géneros "Fantasía" y "Aventura"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (8, 9), (8, 7);

-- Asociación de "La La Land" con los géneros "Musical" y "Drama"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (9, 10), (9, 3);

-- Asociación de "El club de la lucha" con los géneros "Drama" y "Crimen"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (10, 3), (10, 8);