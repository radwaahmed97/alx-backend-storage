-- SQL SCRIPT THAT CREATES A STORED PROCEDURE ADDBONUS THAT ADDS A NEW CORRECTION FOR A STUDENT.
DELIMITER $$ ;
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name varchar(255), IN score FLOAT)
BEGIN
    INSERT INTO projects (name)
    SELECT project_name FROM DUAL
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END $$ ;