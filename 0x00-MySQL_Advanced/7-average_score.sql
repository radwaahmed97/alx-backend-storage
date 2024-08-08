-- SQL SCRIPT THAT CREATES A STORED PROCEDURE COMPUTEAVERAGESCOREFORUSER THAT COMPUTES AND STORE THE AVERAGE SCORE FOR A STUDENT. NOTE: AN AVERAGE SCORE CAN BE A DECIMAL
CREATE PROCEDURE computeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_score FLOAT DEFAULT 0;
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_count INT DEFAULT 0;
    
    SELECT SUM(score), COUNT(score)
        INTO total_score, total_count
        FROM corrections
        WHERE user_id = user_id;
    IF total_count > 0 THEN
        SET average_score = total_score / total_count;
    END IF;
    INSERT INTO average_scores(user_id, score)
        VALUES (user_id, average_score);
END