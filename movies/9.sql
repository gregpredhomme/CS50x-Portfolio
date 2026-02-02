-- 9. Names of all people who starred in a movie released in 2004, ordered by birth year
SELECT p.id, p.name
FROM people p
JOIN stars s ON p.id = s.person_id
JOIN movies m ON s.movie_id = m.id
WHERE m.year IS 2004 AND p.birth IS NOT NULL
GROUP BY p.id
ORDER BY p.birth asc

