class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_grades(self, course, grade, lecturer):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        mid_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Оценок нет!'
        else:
            return f"{mid_sum / len(self.grades.values()):.2f}"

    def __lt__(self, student):
        if self.average_grades() < student.average_grades():
            return ("Первый студент учится лучше! \n")
        else:
            return("Второй студент учится лучше! \n")

    def __eq__(self, other):
        if not isinstance(other, (int, Student)):
            raise TypeError("Операнд справа должен иметь тип int или Student")
        comparison_grade = other if isinstance(other, int) else other.grades
        return self.grades == comparison_grade

    def __str__(self):
        self.courses_in_progress = ", ".join(self.courses_in_progress)
        self.finished_courses = ", ".join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grades()}\n"
                f"Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}")



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] # закрепленные за преподавателем список курсов


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    grades = {}

    def average_grades_lecturer(self):
        mid_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Оценок нет!'
        else:
            return f"{mid_sum / len(self.grades.values()):.2f}"

    def __lt__(self, lecturer):
        if  self.average_grades_lecturer() < lecturer.average_grades_lecturer():
            return("Первый лектор преподает лучше! \n")
        else:
            return("Второй лектор преподает лучше! \n")


    def __eq__(self, other):
        if not isinstance(other, (int, Lecturer)):
            raise TypeError("Операнд справа должен иметь тип int или Lecturer")
        comparison_grade = other if isinstance(other, int) else other.grades
        return self.grades == comparison_grade

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.average_grades_lecturer()}"


student1 = Student("Иван", "Иванов", "М")
student1.finished_courses = ["Введение в програмирование"]
student1.courses_in_progress = ["Python", "Git"]
student1.grades = {}

student2 = Student("Анна", "Петрова", "Ж")
student2.finished_courses = ["Введение в програмирование"]
student2.courses_in_progress = ["Python", "Git"]
student2.grades = {}

lecturer1 = Lecturer("Петя", "Маслов")
lecturer1.grades = {}

lecturer2 = Lecturer("Вася", "Пупкин")
lecturer2.grades = {}

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']


any_reviewer = Reviewer('Some', 'Buddy')
any_reviewer.courses_attached += ['Python']

any_reviewer.rate_hw(best_student, 'Python', 8)
any_reviewer.rate_hw(best_student, 'Python', 10)
any_reviewer.rate_hw(best_student, 'Python', 10)

any_lector = Lecturer("Alex", "Long")
any_lector.courses_attached += ['Python']
best_student.lecturer_grades('Python', 8, any_lector)
best_student.lecturer_grades('Python', 10, any_lector)
best_student.lecturer_grades('Python', 10, any_lector)



#print(best_student.grades)
#print(any_lector.grades)
print(best_student)

print(any_lector)

print(any_reviewer)

print(student1 < student2)
print(lecturer1 < lecturer2)