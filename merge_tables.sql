CREATE TABLE `.students` AS
SELECT *
FROM .students_personal_info
JOIN .students_university USING (Student_ID)
JOIN .students_home_info USING (Student_ID)
JOIN .parents_info USING (Student_ID);