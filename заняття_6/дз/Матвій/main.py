class User:
    def __init__(self, name, age):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Ім'я не може бути порожнім")
        self.name = name.strip()
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not self.is_valid_age(value):
            raise ValueError("Вік має бути цілим числом від 0 до 130")
        self._age = value

    @staticmethod
    def is_valid_age(value):
        return type(value) is int and 0 <= value <= 130

    def describe(self):
        return f"Користувач {self.name}, вік: {self.age}"

    @classmethod
    def from_dict(cls, data):
        if not isinstance(data, dict):
            raise ValueError("Очікується словник")
        try:
            return cls(**data)
        except TypeError as error:
            raise ValueError("Перевірте поля словника") from error

    def __str__(self):
        return self.describe()


class Student(User):
    def __init__(self, name, age, group_name):
        super().__init__(name, age)
        if not isinstance(group_name, str) or not group_name.strip():
            raise ValueError("Назва групи не може бути порожньою")
        self.group_name = group_name.strip()
        self.tasks = []

    def add_task(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Назва завдання не може бути порожньою")
        self.tasks.append(title.strip())

    def describe(self):
        return f"Студент {self.name}, вік: {self.age}, група: {self.group_name}"

    def __len__(self):
        return len(self.tasks)


class Teacher(User):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("Предмет не може бути порожнім")
        self.subject = subject.strip()

    def describe(self):
        return f"Викладач {self.name}, вік: {self.age}, предмет: {self.subject}"


def main():
    student = Student.from_dict({"name": "Олена", "age": 18, "group_name": "Python"})
    teacher = Teacher.from_dict({"name": "Дмитро", "age": 35, "subject": "Python"})
    assert isinstance(student, Student)
    student.add_task("Класи")
    student.add_task("Поліморфізм")
    assert len(student) == 2
    for user in [student, teacher]:
        print(user.describe())
    print(str(student))
    print("Кількість завдань:", len(student))
    assert User.is_valid_age(18)
    assert not User.is_valid_age(True)
    invalid_data = [
        {"name": "Іван", "age": -1, "group_name": "Python"},
        {"name": "Іван", "age": 18},
        {"name": "", "age": 18, "group_name": "Python"},
        {"name": "Іван", "age": "18", "group_name": "Python"},
        [],
    ]
    for data in invalid_data:
        try:
            Student.from_dict(data)
        except ValueError as error:
            print("Помилка:", error)
        else:
            raise AssertionError("Помилкові дані прийнято")
    second = Student("Іван", 19, "Java")
    assert len(second) == 0
    print("Перевірки пройдено")


if __name__ == "__main__":
    main()
