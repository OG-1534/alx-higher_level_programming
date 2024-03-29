-- Script that lists all records with a score >= 10 in second_table database hbtn_0c_0
-- Results should display both the score and the name
-- Records should be ordered by score (top first)
-- The database name will be passed as an argument of the mysql command
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
