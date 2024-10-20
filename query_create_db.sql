-- Table: groups
CREATE TABLE IF NOT EXISTS groups(
    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(50) UNIQUE NOT NULL);

-- Table: teachers
CREATE TABLE IF NOT EXISTS teachers(
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_name VARCHAR(150) UNIQUE NOT NULL);

-- Table: students
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(150) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY(group_id) REFERENCES groups(group_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE);

-- Table: subjects
CREATE TABLE IF NOT EXISTS subjects(
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(50) UNIQUE NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY(teacher_id) REFERENCES teachers(teacher_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE);

-- Table: grades
CREATE TABLE IF NOT EXISTS grades(
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id  INTEGER REFERENCES students(student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    subject_id INTEGER REFERENCES subjects(subject_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    grade_name INTEGER CHECK(grade_name >= 0 AND grade_name <= 100),
    grade_date DATE NOT NULL);
