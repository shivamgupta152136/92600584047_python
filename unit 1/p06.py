# Program to demonstrate tuples and sets

print('Tuple'.center(100,'-'))
numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)
print(" tuple First element:", numbers[0])
print("tuple Last element:", numbers[-1])

print('slicing'.center(100,'-'))
print("Tuple slicing:", numbers[1:4])

print('Set'.center(100,'-'))
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print("Set A:", a)
print("Set B:", b)

print('Basic set operations'.center(100,'-'))
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

print('Add and Remove'.center(100,'-'))
a.add(70)
print("After adding 70:", a)

a.remove(20)
print("After removing 20:", a)
