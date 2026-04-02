-- 7-insert_value.sql
-- Insert a new row in first_table

-- Mövcud sətirləri silmək istəmirsənsə, IF NOT EXISTS ilə yoxlaya bilərsən:
INSERT INTO first_table (id, name)
SELECT 89, 'Best School'
WHERE NOT EXISTS (
    SELECT 1 FROM first_table WHERE id = 89
);
