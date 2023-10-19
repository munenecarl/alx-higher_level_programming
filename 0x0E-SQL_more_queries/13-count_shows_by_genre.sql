-- import databse dump from hbtn_0d_tvshows to your MySQL server
-- script that lists all genres from hbtn_0d_tvshows and their number of shows
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows
  FROM genres
  JOIN tv_show_genres
    ON genres.id = tv_show_genres.genre_id
  JOIN tv_shows
    ON tv_show_genres.tv_show_id = tv_shows.id
 GROUP BY genres.id
 ORDER BY number_of_shows DESC;