-- 16-no_link.sql
-- Lists all records of second_table with a name, ordered by score descending

-- Add the new rows
INSERT INTO second_table (id, name, score) VALUES
(5, 'Aria', 18),
(6, 'Aria', 12)
ON DUPLICATE KEY UPDATE name = VALUES(name), score = VALUES(score);

-- Select all rows where name is not NULL, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
