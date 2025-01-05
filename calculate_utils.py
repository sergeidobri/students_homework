"""Утилиты для работы с классами и их объектами"""

def calc_avg_homework_grade(
        list_of_students: list | tuple,
        course_name: str) -> str:
    """
    Функция подсчета средней оценки за домашнюю работу
    :param list_of_students: [int, tuple] - список студентов
    :param course_name: [str] - название курса
    :result: [str] - функция выводит строку, поясняющую текущую 
                     среднюю оценку за домашние задания по курсу
    """
    sum_of_grades = 0
    cnt_of_grades = 0
    for student in list_of_students:
        for course in student.grades:
            if course == course_name:
                sum_of_grades += sum(student.grades[course])
                cnt_of_grades += len(student.grades[course])
                break

    avg = (0 if cnt_of_grades == 0
                    else sum_of_grades / cnt_of_grades)
    return f"Средняя оценка домашнего задания по предмету {course_name}: {avg:.2f}"

def calc_avg_lecturers_grade(
        list_of_lecturers: list | tuple,
        course_name: str) -> str:
    """
    Функция подсчета средней оценки за лекции от студентов
    :param list_of_lecturers: [int, tuple] - список лекторов
    :param course_name: [str] - название курса
    :result: [str] - функция выводит строку, поясняющую текущую 
                     среднюю оценку за лекции по курсу
    """
    sum_of_grades = 0
    cnt_of_grades = 0
    for lecturer in list_of_lecturers:
        for course in lecturer.grades:
            if course == course_name:
                sum_of_grades += sum(lecturer.grades[course])
                cnt_of_grades += len(lecturer.grades[course])
                break

    avg = (0 if cnt_of_grades == 0
                    else round(sum_of_grades / cnt_of_grades, 2))
    return f"Средняя оценка лекций по предмету {course_name}: {avg}"
