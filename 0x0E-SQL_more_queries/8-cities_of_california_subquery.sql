-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- The states table contains only one record where name = California but the id can be different
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword
-- The database name will be passed as an argument of the mysql command
SELECT cities.id, state.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;