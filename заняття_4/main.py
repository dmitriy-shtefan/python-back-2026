class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def describe(self):
        return f"{self._name} is {self.age} years old"

class Student(Person):
    pass

class Educator(Person):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty

    def describe(self):
        # print(f"{self.__name} is {self.specialty} years old")
        return f"{super().describe()}, speciality is {self.specialty} "


class Course:
    def __init__(self, title, educator):
        self.title = title
        self.educator = educator
        self.students = []

    def enroll(self, student):
        if student not in self.students:
            self.students.append(student)
            return True

        return False

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(student.describe())


alex = Educator("Alex", 32, "Python")
print(alex.describe())

mike = Student("Mike", 19)
mike2 = Student("Mike", 19)
print(mike.describe())

python = Course("Python", alex)
python.enroll(mike)
python.enroll(mike2)
python.enroll(mike)

python.list_students()
# how many students on the list?


mike2._name = "Mike2"

print(mike2.describe())


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > self.balance:
            self.balance += amount

    def show_balance(self):
        print(self.balance)



balance = BankAccount(100)

balance.balance += 1000

balance.show_balance()



