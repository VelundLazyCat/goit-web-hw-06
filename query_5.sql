--Знайти які курси читає певний викладач.
SELECT t.teacher_name, s.subject_name
FROM teachers t 
JOIN subjects s ON s.teacher_id = t.teacher_id 
WHERE s.teacher_id = 3;