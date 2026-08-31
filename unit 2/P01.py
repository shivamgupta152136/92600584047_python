# 1. Using 'if' statement 
number = 10
print("--- 1. if statement ---")
if number > 0:
    print(f"{number} is a positive number.")

# 2. Using 'if-else' statement 
age = 16
print("\n--- 2. if-else statement ---")
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# 3. Using 'if-elif-else' statement s
score = 85
print("\n--- 3. if-elif-else statement ---")
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F or D")