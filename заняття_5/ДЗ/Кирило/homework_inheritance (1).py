class User:

    def __init__(self, user_id, name, age):
        self.id = user_id
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Вік має бути додатним")
        self._age = value

    def describe(self):
        return f"{self.name}, {self.age} років (id={self.id})"


class Student(User):

    group = None


class Teacher(User):

    def __init__(self, user_id, name, age, department):
        super().__init__(user_id, name, age)
        self.department = department

    def describe(self):
        return f"{super().describe()}; кафедра: {self.department}"


class Group:

    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.group = self

    def show_students(self):
        print(f"Група {self.name}:")
        for student in self.students:
            print(" ", student.describe())


if __name__ == "__main__":
    teacher = Teacher(1, "Alex", 32, "Інформатика")
    olena = Student(2, "Олена", 18)

    print(teacher.describe())
    print(olena.describe())

    group = Group("PY-101")
    group.add_student(olena)
    group.add_student(olena)
    group.show_students()

    for cls, args in ((Student, (3, "Тест", -1)),
                      (Teacher, (4, "Тест", 0, "Фізика"))):
        try:
            cls(*args)
        except ValueError as error:
            print(f"{cls.__name__}: {error}")

    olena.age = 19
    print("Новий вік:", olena.age)
    try:
        olena.age = -5
    except ValueError as error:
        print("Student.age = -5 ->", error)

    print(isinstance(teacher, User), issubclass(Student, User))
    print("property age одна на всіх:", Student.age is User.age is Teacher.age)
    print("describe перевизначено в Teacher:",
          Teacher.describe is not User.describe)
    print("describe не перевизначено в Student:",
          Student.describe is User.describe)
