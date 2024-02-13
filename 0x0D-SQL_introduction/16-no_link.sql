-- Script that lists all records of table second_table database hbtn_0c_0
-- Don't list rows without a name value
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
-- The database name will be passed as an argument to the mysql command
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
