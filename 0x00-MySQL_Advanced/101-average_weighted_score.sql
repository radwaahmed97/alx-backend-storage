-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users As u, (SELECT u.id, SUM(score * weight) / SUM(weight) AS average_weighted_score FROM users AS u JOIN corrections AS c ON u.id = c.user_id JOIN projects AS p ON c.project_id = p.id GROUP BY u.id) AS t SET u.average_score = t.average_weighted_score WHERE u.id = t.id;
END
//
DELIMITER ;