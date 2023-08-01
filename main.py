from modules.classes import Student, Lecturer, Reviewer
from modules.functions import average_rating_lect, average_rating_stud

st_list = []
lec_list = []

student = Student('Алина', 'Никитина', 'женский')
student.finished_courses += ['Data Scientist']
student.courses_in_progress += ['Python', 'Git']
st_list.append(student)

student1 = Student('Василий', 'Иванов', 'мужской')
student1.finished_courses += ['Введение в программирование']
student1.courses_in_progress += ['Git', 'Аналитика', 'Python']
st_list.append(student1)

lecturer = Lecturer('Андрей', 'Росновский')
lecturer.courses_attached = ('Введение в программирование', 'Python', 'Git')
lec_list.append(lecturer)

lecturer1 = Lecturer('Иван', 'Лазарев')
lecturer1.courses_attached = ('Git', 'Аналитика', 'Data Scientist', 'Python')
lec_list.append(lecturer1)

reviewer = Reviewer('Анастасия', 'Толкина')
reviewer.courses_attached += ['Python', 'Git', 'Аналитика']

reviewer1 = Reviewer('Александр', 'Панов')
reviewer1.courses_attached += ['Введение в программирование', 'Data Scientist', 'Java']

student.rate_lecturer(lecturer, 'Python', 10)
student.rate_lecturer(lecturer1, 'Python', 7)
student1.rate_lecturer(lecturer, 'Python', 8)
student1.rate_lecturer(lecturer1, 'Python', 9)

reviewer.rate_hw(student, 'Python', 8)
reviewer.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student, 'Python', 7)
reviewer1.rate_hw(student1, 'Python', 8)

print(student)
print(student1)
print(lecturer)
print(lecturer1)
print(reviewer)
print(reviewer1)

print(f'Средняя оценка студентов на курсе Python: {average_rating_stud(st_list, "Python")}')
print(f'Средняя оценка преподавателей на курсе Python: {average_rating_lect(lec_list, "Python")}\n')

print(student == student1)
print(lecturer < lecturer1)