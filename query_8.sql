--Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.teacher_name, sb.subject_name, ROUND(AVG(tch_sub.grade_name), 1)
FROM 
     (SELECT g.subject_id, g.grade_name, s.teacher_id
     FROM grades g
     JOIN subjects s ON s.subject_id = g.subject_id 
     WHERE s.teacher_id = 3) AS tch_sub
JOIN teachers t ON t.teacher_id = tch_sub.teacher_id
JOIN subjects sb ON sb.subject_id = tch_sub.subject_id
GROUP BY sb.subject_name;