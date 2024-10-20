--Знайти список курсів, які відвідує студент.
SELECT s.student_name, sb.subject_name
FROM 
     (SELECT gr.student_id, gr.subject_id
     FROM grades gr
     WHERE student_id = 17) AS stu_sub
JOIN students s ON s.student_id = stu_sub.student_id
JOIN subjects sb ON sb.subject_id = stu_sub.subject_id
GROUP BY sb.subject_name;