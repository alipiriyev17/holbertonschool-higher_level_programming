-- 9-full_creation.sql
-- Create second_table if it does not exist and insert multiple rows

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Təkrar insertləri önləmək üçün cədvəli boşaldırıq
TRUNCATE TABLE second_table;

-- Yeni sətirləri əlavə edirik
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
