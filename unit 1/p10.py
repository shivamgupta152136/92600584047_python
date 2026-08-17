def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("\nRecursion using Factorial")
num = int(input("enter no:"))
print("Number:", num)
print("Factorial:", factorial(num))
