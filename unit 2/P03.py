number = int(input("Enter a number for the multiplication table: "))

print(f"\n--- Multiplication Table for {number} ---")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
