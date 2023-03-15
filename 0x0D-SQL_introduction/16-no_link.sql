-- This script lists all records of the table of the database in MYSQL server.
-- It doesn't list rows without a name value and the results should be in
-- Descending order.
SELECT score, name FROM second_table
where name != ""
ORDER BY score DESC;
