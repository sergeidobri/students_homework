"""Модуль для тестирования работы классов, их методов и функций, связанных с ними"""

from roles import Lecturer, Reviewer, Student
from calculate_utils import calc_avg_homework_grade, calc_avg_lecturers_grade


def main():
    """Функция, тестирующая работу с классами"""
    frst_student = Student("Валерий", "Леонтьев", "male")
    scnd_student = Student("Кира", "Найтли", "female")
    thrd_student = Student("Памела", "Вурхиз", "female")
    for student in (frst_student, scnd_student, thrd_student):
        student.courses_in_progress += [
            "Дифференциальные уравнения", 
            "Механика космического полета", 
            "Теоретическая механика", 
            "Математическая статистика",
            "Программирование на C/C++",
            "Линейная алгебра",
            ]
        student.finished_courses += [
            "Комплексный анализ", 
            "Математический анализ", 
            "Теория вероятностей", 
            "Дискретная математика", 
            "Программирование на Python"
            ]

    best_lecturer = Lecturer("Александр", "Демидов")
    best_lecturer.courses_attached += ["Дифференциальные уравнения"]
    other_lecturer = Lecturer("Александ", "Самохин")
    other_lecturer.courses_attached += ["Линейная алгебра"]

    best_reviewer = Reviewer("Татьяна", "Коноваленко")
    best_reviewer.courses_attached += ["Дифференциальные уравнения"]

    frst_student.rate_lecture(best_lecturer, "Дифференциальные уравнения", 10)
    scnd_student.rate_lecture(best_lecturer, "Дифференциальные уравнения", 9)
    thrd_student.rate_lecture(best_lecturer, "Дифференциальные уравнения", 9)
    frst_student.rate_lecture(other_lecturer, "Линейная алгебра", 5)
    scnd_student.rate_lecture(other_lecturer, "Линейная алгебра", 4)
    thrd_student.rate_lecture(other_lecturer, "Линейная алгебра", 5)

    best_reviewer.rate_hw(frst_student, "Дифференциальные уравнения", 10)
    best_reviewer.rate_hw(scnd_student, "Дифференциальные уравнения", 1)
    best_reviewer.rate_hw(thrd_student, "Дифференциальные уравнения", 6)

    print(frst_student)
    print()
    print(scnd_student)
    print()
    print(thrd_student)
    print()
    print(best_lecturer)
    print()
    print(other_lecturer)
    print()
    print(frst_student > scnd_student)
    print(frst_student == scnd_student)
    print(frst_student != scnd_student)
    print(frst_student < scnd_student)
    print(frst_student >= scnd_student)
    print(frst_student <= scnd_student)
    print()
    print(best_lecturer > other_lecturer)
    print(best_lecturer == other_lecturer)
    print(best_lecturer != other_lecturer)
    print(best_lecturer < other_lecturer)
    print(best_lecturer >= other_lecturer)
    print(best_lecturer <= other_lecturer)
    print()
    print(calc_avg_homework_grade(
        [frst_student, scnd_student, thrd_student],
        "Дифференциальные уравнения",
        ))
    print(calc_avg_lecturers_grade(
        [best_lecturer, other_lecturer],
        "Дифференциальные уравнения",
        ))


if __name__ == "__main__":
    main()
