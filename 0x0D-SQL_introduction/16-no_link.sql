-- The script to lists rows with name value
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;

