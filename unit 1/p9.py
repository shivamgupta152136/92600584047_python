def greet(name):
    print("Hello", name)


def add(a, b):
    return a + b


def student(name, age=18):
    print("Name:", name)
    print("Age:", age)


def total(*numbers):
    return sum(numbers)


print("\nFunction with positional argument")
greet("Shivam")

print("\nFunction with two arguments")
print("Addition:", add(10, 20))

print("\nFunction with default argument")
student("Shivam")

print("\nFunction with keyword argument")
student(age=20, name="Shivam")

print("\nFunction with variable length argument")
print("Total:", total(10, 20, 30, 40))
