--Знайти студента із найвищим середнім балом з певного предмета.

SELECT sub.subject_name , s.student_id, s.student_name , 
       ROUND(AVG(g.grade_name), 1) AS average_grade
FROM grades g
JOIN subjects sub ON sub.subject_id = g.subject_id
JOIN students s 
ON s.student_id = g.student_id
WHERE g.subject_id = 2
GROUP BY s.student_id
ORDER  BY average_grade DESC
LIMIT 1
