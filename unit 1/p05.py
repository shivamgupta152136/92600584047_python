'''5. Write a program to create and manipulate lists
using indexing slicing and list comprehensions.'''

print('indexing'.center(100,'-'))

num=[10,20,30,40,50,60,70]
print('Originl list', num)
print("First element:", num[0])
print("Third element:", num[2])
print("Last element:", num[-1])
print('\n')

print('Slicing'.center(100,'-'))
print("First three elements:", num[:3])
print("Elements from index 2 to 4:", num[2:5])
print("Last three elements:", num[-3:])
print('\n')

print('List Manipulate'.center(100,'-'))
num.append(80)
print('after adding :',num)

num.pop()
print('after removing:',num)
print('\n')

print('List Comprehension'.center(100,'-'))

squares = [x*x for x in num]
print('squares:',squares)
print('\n')

print('list comprehension using condition'.center(100,'-'))
even_numbers = [x for x in num if x % 2 == 0]
print("Even numbers:", even_numbers)
