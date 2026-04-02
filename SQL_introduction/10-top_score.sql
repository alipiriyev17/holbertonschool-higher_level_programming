-- 10-top_score.sql
-- List all records from second_table by score (top first)

SELECT score, name
FROM second_table
ORDER BY score DESC;
