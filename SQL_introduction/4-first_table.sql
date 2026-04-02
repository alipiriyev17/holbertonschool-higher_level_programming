-- 4-first_table.sql
-- This script creates a table called first_table in the current database
-- The table has two columns: id (INT) and name (VARCHAR(256))
-- If the table already exists, it will not fail

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
