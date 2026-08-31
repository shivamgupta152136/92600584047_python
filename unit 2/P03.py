# Take input from the user
number = int(input("Enter a number for the multiplication table: "))

print(f"\n--- Multiplication Table for {number} ---")

# Use a for loop to multiply the number by 1 through 10
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")