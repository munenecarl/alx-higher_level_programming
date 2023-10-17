USE hbtn_0c_0;

-- Import the table dump from temperatures.sql
SOURCE temperatures.sql;

-- Compute the average temperature by city and order by temperature (descending)
SELECT city, AVG(temperature) AS avg_temperature_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;