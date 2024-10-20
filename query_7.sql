--Знайти оцінки студентів у окремій групі з певного предмета.
SELECT group_students.group_id, sb.subject_name, 
       group_students.student_name, gr.grade_name
FROM (
    SELECT g.group_id, s.student_name, s.student_id
    FROM students s
    JOIN groups g 
    ON g.group_id = s.group_id
    WHERE g.group_id = 2
    ) AS group_students
JOIN grades AS gr 
ON  gr.student_id = group_students.student_id
JOIN subjects sb 
ON sb.subject_id = gr.subject_id 
WHERE gr.subject_id = 2;