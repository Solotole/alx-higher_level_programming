-- average of tempearature in cities
SELECT city, AVG(value) AS avg_temp
FROM temperatures
ORDER BY avg_temp DESC
GROUP BY city;
