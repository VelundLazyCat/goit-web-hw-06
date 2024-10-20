--Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT s.student_id, s.student_name, ROUND(AVG(g.grade_name), 1) AS average_grade
FROM students AS s
LEFT JOIN grades AS g ON s.student_id = g.student_id
GROUP BY s.student_id
ORDER BY average_grade DESC
LIMIT 5;