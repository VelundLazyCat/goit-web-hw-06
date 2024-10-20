--Знайти середній бал у групах з певного предмета.
SELECT gr.group_id , gr.group_name, sub.subject_name,
       ROUND(AVG(g.grade_name), 1) AS average_grade
FROM grades g
JOIN subjects sub ON sub.subject_id = g.subject_id
JOIN students s ON s.student_id = g.student_id
JOIN groups gr ON gr.group_id = s.group_id 
WHERE g.subject_id = 2
GROUP BY gr.group_id