--Знайти список студентів у певній групі.
SELECT g.group_name, s.student_id, s.student_name
FROM students s
JOIN groups g ON s.group_id = g.group_id 
WHERE s.group_id = 2;