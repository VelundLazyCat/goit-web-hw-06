--Знайти середній бал на потоці (по всій таблиці оцінок).
SELECT AVG(total_grades.average_grade)
FROM
(SELECT s.student_id, s.student_name, ROUND(AVG(g.grade_name), 1) AS average_grade
FROM students AS s
LEFT JOIN grades AS g ON s.student_id = g.student_id
GROUP BY s.student_id) AS total_grades