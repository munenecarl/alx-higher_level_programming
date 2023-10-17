-- Script that displays max temp
USE hbtn_0c_0;

-- Import the table dump from temperatures.sql
SOURCE temperatures.sql;

-- Compute the max temperature of each state and order by state name
SELECT state, MAX(temperature) AS max_temperature_fahrenheit
FROM temperatures
GROUP BY state
ORDER BY state;