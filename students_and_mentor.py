class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __eq__(self, other):
        return isinstance(other, Student) and self.name == other.name and self.surname == other.surname

    def __lt__(self, other):
        return isinstance(other, Student) and (self.name, self.surname) < (other.name, other.surname)

    def __gt__(self, other):
        return isinstance(other, Student) and (self.name, self.surname) > (other.name, other.surname)

    def cool_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        avg_grade = sum([sum(grades) for grades in self.grades.values()]) / sum([len(grades) for grades in self.grades.values()])
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {avg_grade}\nКурсы в процессе изучения: {in_progress}\nЗавершенные курсы: {finished}"
    
def score_homework(students, course):
    total_score = 0
    total_students = 0

    for student in students:
        if course in student.grades:
            total_score += sum(student.grades[course])
            total_students += len(student.grades[course])

    if total_students == 0:
        return 0
    else:
        return total_score / total_students

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __eq__(self, other):
        return isinstance(other, Mentor) and self.name == other.name and self.surname == other.surname

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = sum([sum(grades) for grades in self.grades.values()]) / sum([len(grades) for grades in self.grades.values()])
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}"
    
    def __eq__(self, other):
        return isinstance(other, Lecturer) and self.name == other.name and self.surname == other.surname


def calculate_average_lecture_score(lecturers, course):
    total_score = 0
    total_lecturers = 0
    
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_score += sum(lecturer.grades[course])
            total_lecturers += 1
    
    if total_lecturers == 0:
        return 0
    else:
        return total_score / total_lecturers

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
    
    def __eq__(self, other):
        return isinstance(other, Reviewer) and self.name == other.name and self.surname == other.surname

best_student = Student('Ruoy', 'Eman', 'мужской')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

student2 = Student('Bebey', 'Rogers', 'женский')
student2.courses_in_progress += ['Python', 'JavaScript']
student2.finished_courses += ['Введение в программирование']

students = [best_student, student2]

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

mentor2 = Mentor('Emily', 'Brown')
mentor2.courses_attached += ['JavaScript']

cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached += ['Python']

lecturer2 = Lecturer('Grase', 'Glark')
lecturer2.courses_attached += ['JavaScript']

reviewer1 = Reviewer('Johny', 'Silverhend')
reviewer2 = Reviewer('George', 'Martinez')

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(student2, 'Python', 8)

mentor2.rate_hw(best_student, 'JavaScript', 9)
mentor2.rate_hw(student2, 'JavaScript', 7)

best_student.cool_lecturer(cool_lecturer, 'Python', 6)
best_student.cool_lecturer(lecturer2, 'JavaScript', 9)

student2.cool_lecturer(cool_lecturer, 'Python', 4)
student2.cool_lecturer(lecturer2, 'JavaScript', 7)

students = [best_student, student2]
lecturers = [cool_lecturer, lecturer2]  

average_homework_score_python = score_homework(students, 'Python')
average_lecture_score_python = calculate_average_lecture_score(lecturers, 'Python')

student1 = Student('John', 'Doe', 'male')
student2 = Student('Alice', 'Smith', 'female')

print(best_student)
print(student2)

print(cool_lecturer)
print(mentor2)

print(lecturer2)
print(reviewer1)
print(reviewer2)

print(f'средняя оценка за домашние задания по Python: {average_homework_score_python}')
print(f'Средний балл за лекции по курсу Python:{average_lecture_score_python}')

print(student1 == student2)  
print(student1 < student2)    
print(student1 > student2) 