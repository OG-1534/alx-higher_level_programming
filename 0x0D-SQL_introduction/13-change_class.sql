-- Script that removes records with a score <= 5 in second_table database hbtn_0c_0
-- The database name will be passed as an argument of the mysql command
DELETE FROM `second_table`
WHERE `score` <= 5;
