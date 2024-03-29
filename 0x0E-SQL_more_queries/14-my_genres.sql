-- List all genres of a specified show in a database.

SELECT name FROM tv_genres
	INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	WHERE title = 'Dexter'
	ORDER BY name ASC;
