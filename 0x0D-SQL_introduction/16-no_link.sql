--  script listing all records of table second_table in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
