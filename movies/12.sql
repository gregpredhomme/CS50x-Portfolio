-- 12. Titles of all of movies in which both Jennifer Lawrence and Bradley Cooper starred
SELECT title
FROM movies
WHERE id IN (
    SELECT movie_id
    FROM stars s
    JOIN people p ON s.person_id = p.id
    WHERE name = 'Bradley Cooper'
)
AND id IN (
    SELECT movie_id
    FROM stars s
    JOIN people p ON s.person_id = p.id
    WHERE name = 'Jennifer Lawrence'
)


