-- 11. Titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated
SELECT m.title
FROM people p
JOIN stars s ON p.id = s.person_id
JOIN movies m ON s.movie_id = m.id
JOIN ratings r ON m.id = r.movie_id
WHERE p.name IS "Chadwick Boseman"
ORDER BY r.rating desc
LIMIT 5
