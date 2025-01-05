"""Классы и их методы"""

class Student:
    """Класс студента"""
    def __init__(self, name: str, surname: str, gender: str) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course: str, grade: int) -> None:
        """
        Метод для оценки лектора
        :param lecturer: [Lecturer] - лектор
        :param course: [str] - название курса
        :param grade: [int] - оценка лекции
        :result: None - Функция ничего не выводит
        """
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
            and 0 < grade <= 10 and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            errno = "Некорректные значения"
            if not isinstance(lecturer, Lecturer):
                errno += ", лектор должен быть объектом класса Lecturer"
            if course not in self.courses_in_progress:
                errno += ", студент должен изучать данный курс"
            if not 0 < grade <= 10:
                errno += ", оценка должна быть от 1 до 10"
            if not course in lecturer.courses_attached:
                errno += ", лектор должен вести данный курс"

            raise ValueError(errno)

    def calc_avg_grade(self) -> float | 0:
        """
        Метод для подсчета средней оценки студента
        :result: float | 0 - Функция выводит среднюю оценку студента
                            по всем курсам, на которых он обучается.
                            Результат представлен вещественным числом или
                            нулем в случае отсутствия отметок
        """
        grades_lst = [grade for grades in self.grades.values() for grade in grades]
        return 0 if len(grades_lst) == 0 else sum(grades_lst) / len(grades_lst)

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
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.calc_avg_grade() < other.calc_avg_grade()
        else:
            raise TypeError("Студентов можно сравнивать только друг с другом")

    def __ge__(self, other):
        return not self.__lt__(other)

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.calc_avg_grade() > other.calc_avg_grade()
        else:
            raise TypeError("Студентов можно сравнивать только друг с другом")

    def __le__(self, other):
        return not self.__gt__(other)

class Mentor:
    """Родительский класс преподавателей"""

    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс лекторов"""
    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.calc_avg_grade()
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n' +
            f'Средняя оценка за лекции: {avg_grade:.1f}')

    def calc_avg_grade(self) -> None:
        """
        Метод для подсчета средней оценки лектора
        :result: float | 0 - Функция выводит среднюю оценку лектора
                            по всем курсам, которые он ведет.
                            Результат представлен вещественным числом или
                            нулем в случае отсутствия отметок
        """
        grades_lst = [grade for grades in self.grades.values() for grade in grades]
        return 0 if len(grades_lst) == 0 else sum(grades_lst) / len(grades_lst)

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.calc_avg_grade() == other.calc_avg_grade()
        else:
            raise TypeError("Лекторов можно сравнивать только друг с другом")

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.calc_avg_grade() < other.calc_avg_grade()
        else:
            raise TypeError("Лекторов можно сравнивать только друг с другом")

    def __ge__(self, other):
        return not self.__lt__(other)

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.calc_avg_grade() > other.calc_avg_grade()
        else:
            raise TypeError("Лекторов можно сравнивать только друг с другом")

    def __le__(self, other):
        return not self.__gt__(other)


class Reviewer(Mentor):
    """Класс ревьюверов"""
    def rate_hw(self, student, course: str, grade: int) -> None:
        """
        Метод для оценки домашнего задания
        :param student: [Student] - студент
        :param course: [str] - название курса
        :param grade: [int] - оценка домашнего задания
        :result: None - Функция ничего не выводит
        """
        if (isinstance(student, Student) and course in self.courses_attached
            and course in student.courses_in_progress and 0 < grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            errno = "Некорректные значения"
            if not isinstance(student, Student):
                errno += ", студент должен быть объектом класса Student"
            if course not in course in self.courses_attached :
                errno += ", ревьювер должен иметь право ставить оценки на этом курсе"
            if not 0 < grade <= 10:
                errno += ", оценка должна быть от 1 до 10"
            if not course in student.courses_in_progress:
                errno += ", студент должен изучать данный курс"

            raise ValueError(errno)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
