'''4. Write a program to demonstrate string
operations including slicing formatting and
built-in string functions.'''


print('String slicing'.center(100,'-'))

x='hello welcome to marwadi'

print('original string:',x)
print('first five character:',x[:5])
print('characters from index 5 to 9 :',x[6:9])
print('last 6 characters:',x[-6:])
print('reverse string:',x[::-1])
print('\n')

print('String formatting'.center(100,'-'))

name = "Rahul"
age = 20

print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")
print('\n')

print('String Built-in function'.center(100,'-'))
print('LowerCase:',x.lower())
print('UpperCase:',x.upper())
print('Length:',len(x))
print('Replace string:',x.replace('hello','hii'))
print("count of 'o':",x.count('o'))
print('position of character :',x.find('to'))
print('Is aplhabetic:',x.isalpha())
print("Starts with 'Hello':", x.startswith("hello"))
print("Ends with '!':", x.endswith("!"))
