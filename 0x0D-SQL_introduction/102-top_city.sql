USE hbtn_0c_0;

-- Import the table dump from temperatures.sql
SOURCE temperatures.sql;

-- Compute the top 3 cities with highest temperature during July and August and order by temperature (descending)
SELECT city, MAX(temperature) AS max_temperature_fahrenheit
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY max_temperature_fahrenheit DESC
LIMIT 3;