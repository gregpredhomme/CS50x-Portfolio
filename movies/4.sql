-- 4. Number of movies with a 10.0 rating
SELECT COUNT(*) AS "10.0 Movies"
FROM ratings
WHERE rating = 10.0
