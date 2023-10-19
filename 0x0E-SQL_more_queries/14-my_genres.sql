-- import database dump from hbtn_0d_tvshows to your MySQL server
-- script that creates the database hbtn_0d_tvshows and the table genres (in the database hbtn_0d_tvshows) on your MySQL server.
-- tv_shows table description:
-- tv_shows contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT `tv_genres`.`name`
  FROM `tv_genres`
  JOIN `tv_show_genres`
    ON `tv_genres`.`id` = `tv_show_genres`.`genre_id`
  JOIN `tv_shows`
    ON `tv_shows`.`id` = `tv_show_genres`.`tv_show_id`
 WHERE `tv_shows`.`title` = 'Dexter';