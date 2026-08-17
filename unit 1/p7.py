'''7. Write a program to create a dictionary and demonstrate dictionary methods and iteration.'''

# Create a dictionary
student = {
    "name": "Shivam",
    "age": 20,
    "course": "BCA",
    "marks": 85
}

print("Display dictionary")
print("\n")
print("Dictionary:", student)
print("\n")

print("Dictionary methods")
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("\n")

print("Access a value")
print("Name:", student.get("name"))
print("\n")

print("Add a new item")
student["city"] = "Ahmedabad"
print("After adding city:", student)
print("\n")

print("Update a value")
student["marks"] = 90
print("After updating marks:", student)
print("\n")

print("Remove an item")
student.pop("age")
print("After removing age:", student)
print("\n")

#Iteration through dictionary
print("\nIteration through dictionary:")
for key, value in student.items():
    print(key, ":", value)
