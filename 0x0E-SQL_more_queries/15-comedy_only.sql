-- Import the database dump from hbtn_0d_tvshows to your MySQL server:
-- script that lists all Comedy shows in the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by tv_shows.title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT `tv_shows`.`title`
  FROM `tv_shows`
  JOIN `tv_show_genres`
    ON `tv_shows`.`id` = `tv_show_genres`.`tv_show_id`
  JOIN `tv_genres`
    ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
 WHERE `tv_genres`.`name` = 'Comedy'
 ORDER BY `tv_shows`.`title`;