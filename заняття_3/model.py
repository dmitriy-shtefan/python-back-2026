class Course:
    category = "Навчання"

    def __init__(self, title):
        self.title = title
        self.students = []

    def label(self):
        return f"Курс: {self.title}"

    def enroll(self, student):
        if student in self.students:
            return False

        self.students.append(student)
        return True

    def student_count(self):
        return len(self.students)


class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def profile(self):
        return f"{self.name} <{self.email}>"

python_course = Course("Python")
django_course = Course("Django")

python_course.lessons_number = 10
print(python_course.lessons_number)

print(python_course.label())
print(django_course.label())

oleg = Student("Oleg", "oleg99@gmail.com")

# python_course.category = "Програмування"
print(python_course.enroll(oleg))
print(python_course.enroll(oleg))

print(python_course.category)
print(django_course.category)
print(python_course.students)
