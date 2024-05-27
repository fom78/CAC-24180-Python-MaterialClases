-- EJEMPLOS DE CONSULTAS BASICAS

-- 1 Encuentra el título y la fecha de estreno de las 
-- películas que tienen  "El" en su título

select title, release_year FROM movies where title like 'EL%' or title like 'The%' ;





-- 2 Encuentra el título y si es para adulto de las peliculas 
-- estrenadas después de 2000:

select title, adult from movies where release_year > 2000;



-- 3 Encuentra el título  de las películas que fueron estrenadas 
-- antes de 1990 o después de 2010

SELECT title, release_year 
FROM movies 
WHERE  release_year < 1990 OR release_year > 2010



-- 4 Encuentra todas las películas cuyo año de estreno sea 1994 o 1997.
SELECT title, release_year 
FROM movies 
WHERE  release_year in (1994, 1997,2021)
order by release_year desc

-- EJEMPLOS DE CONSULTAS AVANZADAS

-- 5 Encuentra todas las películas junto con las críticas asociadas.


-- 6 Encuentra todas las películas, incluso si no tienen críticas asociadas.


--  7 Encuentra el título de la película, el nombre del crítico y su comentario para
-- todas las críticas con una calificación de 4 o más:



-- 8 Encuentra el promedio de calificaciones por película, solo para películas 
-- con más de una crítica:


-- Encuentra las películas junto con sus géneros:

-- buscar el nombre de la pelicula y el rating maximo y minimo recibido
