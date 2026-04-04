-- Task 10: Genre ID by show
-- List all shows that have at least one genre linked
-- Display: tv_shows.title - tv_show_genres.genre_id
-- Results sorted by title and genre_id ascending
-- Only one SELECT statement is used

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
