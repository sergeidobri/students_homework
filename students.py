class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
            and 0 < grade <= 10 and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def calc_avg_grade(self):
        grades = self.grades
        sum_grades = 0
        cnt_grades = 0

        for course in grades:
            sum_grades += sum(grades[course])
            cnt_grades += len(grades[course])

        return (0 if cnt_grades == 0 else sum_grades / cnt_grades)
    
    def __str__(self):
        avg_grade = self.calc_avg_grade()
        return (f'Имя: {self.name}\n' + 
            f'Фамилия: {self.surname}\n' + 
            f'Средняя оценка за домашние задания: {avg_grade}\n' + 
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' + 
            f'Завершенные курсы: {", ".join(self.finished_courses)}')
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.calc_avg_grade() == other.calc_avg_grade()
        else:
            raise TypeError("Студентов можно сравнивать только друг с другом")

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.calc_avg_grade() != other.calc_avg_grade()
        else:
            raise TypeError("Студентов можно сравнивать только друг с другом")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.calc_avg_grade() < other.calc_avg_grade()
        else:
            raise TypeError("Студентов можно сравнивать только друг с другом")

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.calc_avg_grade() > other.calc_avg_grade()
        else:
            raise TypeError("Студентов можно сравнивать только друг с другом")
        
    def __le__(self, other):
        if isinstance(other, Student):
            return self.calc_avg_grade() <= other.calc_avg_grade()
        else:
            raise TypeError("Студентов можно сравнивать только друг с другом")
        
    def __ge__(self, other):
        if isinstance(other, Student):
            return self.calc_avg_grade() >= other.calc_avg_grade()
        else:
            raise TypeError("Студентов можно сравнивать только друг с другом")


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

 
class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.calc_avg_grade()
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n' + 
            f'Средняя оценка за лекции: {avg_grade:.1f}')

    def calc_avg_grade(self):
        grades = self.grades
        sum_grades = 0
        cnt_grades = 0

        for course in grades:
            sum_grades += sum(grades[course])
            cnt_grades += len(grades[course])
        
        return (0 if cnt_grades == 0 else sum_grades / cnt_grades)

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.calc_avg_grade() == other.calc_avg_grade()
        else:
            raise TypeError("Лекторов можно сравнивать только друг с другом")

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.calc_avg_grade() != other.calc_avg_grade()
        else:
            raise TypeError("Лекторов можно сравнивать только друг с другом")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.calc_avg_grade() < other.calc_avg_grade()
        else:
            raise TypeError("Лекторов можно сравнивать только друг с другом")

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.calc_avg_grade() > other.calc_avg_grade()
        else:
            raise TypeError("Лекторов можно сравнивать только друг с другом")
        
    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.calc_avg_grade() <= other.calc_avg_grade()
        else:
            raise TypeError("Лекторов можно сравнивать только друг с другом")
        
    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.calc_avg_grade() >= other.calc_avg_grade()
        else:
            raise TypeError("Лекторов можно сравнивать только друг с другом")


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached 
            and course in student.courses_in_progress and 0 < grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def calc_avg_homework_grade(list_of_students, course_name):
    sum_of_grades = 0
    cnt_of_grades = 0
    for student in list_of_students:
        for course in student.grades:
            if course == course_name:
                sum_of_grades += sum(student.grades[course])
                cnt_of_grades += len(student.grades[course])
                break

    avg = (0 if cnt_of_grades == 0 
                    else round(sum_of_grades / cnt_of_grades, 2))
    return f"Средняя оценка домашнего задания по предмету {course_name}: {avg}"

def calc_avg_lecturers_grade(list_of_lecturers, course_name):
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

def main():
    frst_student = Student("Валерий", "Леонтьев", "male")
    scnd_student = Student("Кира", "Найтли", "female")
    thrd_student = Student("Памела", "Вурхиз", "female")
    for student in (frst_student, scnd_student, thrd_student):
        student.courses_in_progress += [
            "Дифференциальные уравнения", 
            "Механика космического полета", 
            "Теоретическая механика", 
            "Математическая статистика",
            "Программирование на C/C++"
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
    frst_student.rate_lecture(other_lecturer, "Дифференциальные уравнения", 5)
    scnd_student.rate_lecture(other_lecturer, "Дифференциальные уравнения", 4)
    thrd_student.rate_lecture(other_lecturer, "Дифференциальные уравнения", 5)

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