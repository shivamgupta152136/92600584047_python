print("--- 1. Iterating over a List ---")
my_list = ["Apple", "Banana", "Cherry"]

for fruit in my_list:
    print(f"Fruit: {fruit}")


print("\n--- 2. Iterating over a String ---")
my_string = "Code"

for letter in my_string:
    print(f"Letter: {letter}")


print("\n--- 3. Iterating over a Dictionary ---")
my_dict = {"Name": "Alice", "Age": 25, "City": "New York"}

for key, value in my_dict.items():
    print(f"{key} -> {value}")