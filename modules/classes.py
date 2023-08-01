from modules.functions import average_rate
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecture, course, grade):
        if isinstance(lecture,
                      Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}' \
               f'\nСредняя оценка за лекции:{average_rate(self)}' \
               f'\nКурсы в процессе изучения: {self.courses_in_progress}' \
               f'\nЗавершенные курсы: {", ".join(self.finished_courses)}\n'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student")
        return self.average_rate() < other.average_rate()
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Наследование
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}' \
               f'\nСредняя оценка за лекции: {average_rate(self)}\n'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer")
            return self._average_rate() < other._average_rate()


class Reviewer(Mentor):
    def rate_hw(self, stud, course, grade):
        if isinstance(stud, Student) and course in stud.courses_in_progress and course in self.courses_attached:
            if course in stud.grades:
                stud.grades[course].append(grade)
            else:
                stud.grades[course] = [grade]

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'