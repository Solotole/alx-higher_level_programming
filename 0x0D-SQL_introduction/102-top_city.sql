-- average of tempearature in cities
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE temperatures.month = 7 AND temperatures.month = 8
LIMIT 3
GROUP BY city
ORDER BY avg_temp DESC;
