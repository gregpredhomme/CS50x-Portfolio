-- 7. All movies and ratings from 2010, in decreasing order by rating (alphabetical for those with same rating)
SELECT m.title, r.rating
FROM ratings r
JOIN movies m ON r.movie_id = m.id
WHERE m.year = 2010
ORDER BY r.rating desc, m.title asc
