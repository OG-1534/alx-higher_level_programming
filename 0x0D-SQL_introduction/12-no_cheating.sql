-- Script that updates the score of Bob to 10 in table second_table
-- Not allowed to use Bob's id value, only the name field
-- The database name will be passed as an argument of the mysql command
UPDATE `second_table`
SET `score` = 10
WHERE LOWER(`name`) = LOWER("Bob");
