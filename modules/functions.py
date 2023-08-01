# Функция определения среднего балла

def average_rate(someone):
    total_grades = 0
    count = 0

    for value in someone.grades.values():
        total_grades += sum(value)
        count += len(value)
    average = total_grades / count
    return average


# Функция определения среднего балла у студентов одного курса

def average_rating_stud(st_list, course):
    lec_course = []
    total_grades = 0
    count_grades = 0
    for st in st_list:
        if course in st.courses_in_progress:
            lec_course.append(st)
    for obj in lec_course:
        for grade in obj.grades.values():
            total = sum(grade)
            total_grades += total
            count_grades += len(grade)
    student_average = total_grades / count_grades
    return student_average


# Функция определения среднего балла у лекторов одного курса

def average_rating_lect(lec_list, course):
    lec_course = []
    total_grades = 0
    count_grades = 0
    for lec in lec_list:
        if course in lec.courses_attached:
            lec_course.append(lec)
    for obj in lec_course:
        for grade in obj.grades.values():
            total = sum(grade)
            total_grades += total
            count_grades += len(grade)
    lecturer_average = total_grades / count_grades
    return lecturer_average