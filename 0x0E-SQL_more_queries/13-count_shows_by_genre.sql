-- count number of shows
SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres, tv_show_genres
WHERE tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
