## Список і індекси

cities = ["Київ", "Львів", "Полтава"]

print(cities[0])
print(cities[-1])
print(len(cities))   # 3

cities[0] = "Одеса"
print(cities[0])


a = 'Hello'
b = 'World'

# Swap:
c = a
a = b  # World
b = c  # Hello


a = 'Hello'
b = 'World'

a, b = b, a

print(a, b)

result, new_result = "Hello", "World"
print(result, new_result)