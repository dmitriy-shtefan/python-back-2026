
def greet(username, prefix="Вітаю"):
    print(prefix + ", " + username)


def describe_user():
    return None


def do_something(my_list = None):
    my_list = my_list or []
    my_list.append("hello")
    print(my_list)


do_something()
do_something()
do_something()





def generate():
    my_list = [1, 2, 3, 4, 5]
    return my_list


def generate2():
    my_list = [1, 2, 3, 4, 5]

    for item in my_list:
        yield item


gen = generate2()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 4
print(next(gen))  # 5

print(list(generate2()))










formatter = describe_user
print(type(formatter)) # Danil: str; Ivan, Nikita, Matviy: func;


formatter()


# scope | Область видимості

# LEGB: Local | Enclosed | Global | Built-In

a = 2


def main():
    n = 1

    def greet():
        nonlocal n
        print(n)
        n = n + 1  # Ivan: n локальною для grid
        return "hello"

    return greet


g = main()

g()
g()
g()




# Завдання порахувати виклики функції


def decorator(func):
    calls_number = 0
    def wrapper(*args, **kwargs):
        nonlocal calls_number
        calls_number += 1
        print("Викликів функції: ", calls_number)
        result = func(*args, **kwargs)
        print("Finished")
        return result

    return wrapper


@decorator
def query_database():
    # запит до бази даних
    return True


print(query_database())

print(query_database())



if query_database():
    print(True)
else:
    print(False)










