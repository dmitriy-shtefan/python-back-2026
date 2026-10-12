## Словник і зміна значень

student = {
    "name": "Оля",
    "points": [10, 11]
}

student["points"].append(12)
student["group"] = "Red"

print(student["name"])
print(student["points"])
print(student["group"])
