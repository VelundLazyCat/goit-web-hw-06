--Середній бал, який певний викладач ставить певному студентові.
SELECT st.student_name, ROUND(AVG(st_sub.grade_name), 1) AS avg_grade, tch_sub.teacher_name
FROM
(SELECT s.subject_id, s.subject_name, t.teacher_name
FROM teachers t 
JOIN subjects s ON s.teacher_id = t.teacher_id 
WHERE s.teacher_id = 3) AS tch_sub
JOIN 
(SELECT gr.subject_id, gr.grade_name, gr.student_id
FROM grades gr
WHERE gr.student_id = 17) AS st_sub
ON tch_sub.subject_id = st_sub.subject_id
JOIN students st ON st.student_id = st_sub.student_id