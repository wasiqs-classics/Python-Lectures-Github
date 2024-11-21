#Lists

tasks = ["Study", "Go to dinner", "Cricket"]
print(tasks[1])

# functionality in lists
tasks.append("Buy grocery")
print(tasks)

list_1 = [1,"string", True, 3.14]
print(list_1)

tasks.insert(2,"Wash clothes")
print(tasks)
print(tasks[1:3])

tasks.remove("Cricket")
print(tasks)

tasks.pop(1)
print(tasks)

alpha = ["Z", "K", "A", "X", "O","j","c","4","1","3"]
alpha.sort()

print(alpha)

items = ["Car", "Plane", "Truck"]
items.reverse()
print(items)

print(items.count("Car"))
print(len(items))

items[1] = "Bike"
print(items)

#Dictionary

student_details = {
    "id" : 1,
    "name" : "Rayan",
    "age" : 26,
    "location" : "UK"
}

student_details["experience"] = "5 years"

print(student_details)

student_details["id"] = 15
print(student_details)

student_details["Skills"] = ["Python", "DB", "SQL"]
print(student_details)

print(student_details["name"])

student_details["education"] = {
    "basic" : "ABC School",
    "College" : "XYZ College",
    "University" : "Some Uni"
}

print(student_details)
print(student_details["education"]["University"])
print(student_details["Skills"][1])

print(student_details.get("phone")) # a safer method! 


print(student_details.pop("age"))

print(student_details)

del student_details["Skills"]

print(student_details)

student_details["experience"] = "6 years"

print(student_details)

print(student_details.keys())
print(student_details.values())
print(student_details.items())

print(len(student_details.keys()))

#Tuples

location = (50.8978, 72.3450)


names = ("Alpha", "Bravo")

print(names.count("Alpha"))
print(names.index("Bravo"))

# Sets

days = {"M", "T", "W", "M"}
print(days)

days.add("F")
print(days)

days.discard("M")
print(days)

set1 = {1,3,5,7,10,13}
set2 = {2,4,6.9,10}

set3 = set1.union(set2)
print(set3)

print(set1.intersection(set2))
