import sqlite3
import logging
from faker import Faker
import random
from sqlite3 import DatabaseError


NUMBER_STUDENTS = 50
NUMBER_TECHERS = 5
NUMBER_SUBJECTS = 8
NUMBER_GROUPS = 3
NUMBER_GRADES = 20
MIN_GRADE = 1
MAX_GRADE = 100


def generate_fake_data(number_students, number_teachers, number_subjects, number_groups, number_grades) -> tuple:

    fake_students = []  # тут зберігатимемо студентів
    fake_teachers = []  # тут зберігатимемо викладачів
    fake_subjects = []  # тут зберігатимемо предмети
    fake_groups = []    # тут зберігатимемо групи студентів
    fake_grades = []    # тут зберігатимемо оцінки з предмету предмету для кожного студента

    fake_data = Faker()

    # створення груп
    for _ in range(number_groups):
        fake_groups.append((fake_data.word(),))

    # створення викладачів
    for _ in range(number_teachers):
        fake_teachers.append((fake_data.name(),))

    # створення студентів із вказівклю до якої групи належить
    for _ in range(number_students):
        groups_id = random.randint(1, number_groups + 1)
        fake_students.append((fake_data.name(), groups_id))

    # створення предметів із вказівкою викладача
    for _ in range(number_subjects):
        teacher_id = random.randint(1, number_teachers + 1)
        fake_subjects.append((fake_data.word(), teacher_id))

    # створення оцінок з предметів із вказівкою викладача
    for student in range(1, number_students + 1):
        for _ in range(1, number_grades + 1):
            fake_grades.append((student,
                                random.randint(1, number_subjects + 1),
                                random.randint(MIN_GRADE, MAX_GRADE),
                                fake_data.date_this_decade()))

    return fake_groups, fake_teachers, fake_students, fake_subjects, fake_grades


def create_db() -> None:
    # читаємо файл зі скриптом для створення БД
    try:
        with open('query_create_db.sql', 'r') as f:
            sql = f.read()
    except FileNotFoundError as e:
        logging.error(e)

    with sqlite3.connect('grades.db') as conn:
        try:
            cur = conn.cursor()
            # виконуємо скрипт який створить таблиці в БД
            cur.executescript(sql)
            logging.info('база створена')
        except DatabaseError as e:
            logging.error('p1', e)
            conn.rollback()
            cur.close()


def insert_data_to_db(sql_query: str, variables: list) -> None:

    with sqlite3.connect('grades.db') as conn:
        try:
            cur = conn.cursor()
            cur.executemany(sql_query, variables)
            logging.info(f'База оновлена, додано {len(variables)} строк')
        except DatabaseError as e:
            logging.error(e)
            conn.rollback()
            cur.close()


def fill_db(*args: list) -> None:

    sql_fill = ["""INSERT INTO groups(group_name) VALUES (?);""",
                """INSERT INTO teachers(teacher_name) VALUES (?);""",
                """INSERT INTO students(student_name, group_id) VALUES (?, ?);""",
                """INSERT INTO subjects(subject_name, teacher_id) VALUES (?, ?);""",
                """INSERT INTO grades(student_id, subject_id, grade_name, grade_date) VALUES (?, ?, ?, ?);"""]

    for num, vars in enumerate(args):
        insert_data_to_db(sql_fill[num], vars)


def execute_query(sql_file: str) -> list:
    # читаємо файл зі скриптом для запиту до БД
    try:
        with open(sql_file, 'r') as f:
            sql_query = f.read()
    except FileNotFoundError as e:
        logging.error(e)

    with sqlite3.connect('grades.db') as conn:
        try:
            cur = conn.cursor()
            cur.execute(sql_query)
        except DatabaseError as e:
            logging.error(e)
            cur.close()
        return cur.fetchall()


def print_result(query) -> None:
    for q in query:
        print(q)


if __name__ == "__main__":

    create_db()
    fill_db(*generate_fake_data(
        NUMBER_STUDENTS, NUMBER_TECHERS, NUMBER_SUBJECTS, NUMBER_GROUPS, NUMBER_GRADES))
    print('-'*20)
    # 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    print('student_id, student_name, max of avg grade')
    print_result(execute_query('query_1.sql'))
    print('-'*30)
    # 2. Знайти студента із найвищим середнім балом з певного предмета.
    print('subject, student_id, student_name, max avg grade')
    print_result(execute_query('query_2.sql'))
    print('-'*30)
    # 3. Знайти середній бал у групах з певного предмета.
    print('group_id, group_name, subject_name, avg grade')
    print_result(execute_query('query_3.sql'))
    print('-'*30)
    # 4. Знайти середній бал на потоці (по всій таблиці оцінок).
    print('avg grade on course')
    print_result(execute_query('query_4.sql'))
    print('-'*30)
    # 5. Знайти які курси читає певний викладач.
    print('teacher_name, subject_name')
    print_result(execute_query('query_5.sql'))
    print('-'*30)
    # 6. Знайти список студентів у певній групі.
    print('group_name, student_id, student_name')
    print_result(execute_query('query_6.sql'))
    print('-'*30)
    # 7. Знайти оцінки студентів у окремій групі з певного предмета.
    print('id_group, subject_name, student_name, grade')
    print_result(execute_query('query_7.sql'))
    print('-'*30)
    # 8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
    print('teacher_name, subject_name, avg_grade')
    print_result(execute_query('query_8.sql'))
    print('-'*30)
    # 9. Знайти список курсів, які відвідує студент.
    print('student_name, subject_name')
    print_result(execute_query('query_9.sql'))
    print('-'*30)
    # 10. Знайти список курсів, які певному студенту читає певний викладач.
    print('teacher_name, subject_name, student_name')
    print_result(execute_query('query_10.sql'))
    print('-'*30)

    # Додаткові завдання
    # 11. Середній бал, який певний викладач ставить певному студентові.
    print('student_name, avg_grade, teacher_name')
    print_result(execute_query('query_11.sql'))
    print('-'*30)
    # 12. Оцінки студентів у певній групі з певного предмета на останньому занятті.
    print('group_id, subject_name, student_name, grade, last_date')
    print_result(execute_query('query_12.sql'))
    print('-'*30)
