-- import the databases dump from hbtn_0d_tvshows to your MySQL server:
-- Script that creates the database hbtn_0d_tvshows and the table genres (in the database hbtn_0d_tvshows) on your MySQL server.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT `tv_shows`.`title`, `tv_genres`.`name`
  FROM `tv_shows`
  LEFT JOIN `tv_show_genres`
    ON `tv_shows`.`id` = `tv_show_genres`.`tv_show_id`
  LEFT JOIN `tv_genres`
    ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
 ORDER BY `tv_shows`.`title`, `tv_genres`.`name`;