print("--- 1. The Iterable ---")
my_list = ["Apple", "Banana", "Cherry"]
print(f"My list: {my_list}")

print("\n--- 2. Creating the Iterator ---")
my_iterator = iter(my_list)
print("Successfully created an iterator from the list.")

print("\n--- 3. Stepping through with next() ---")
print(f"First item: {next(my_iterator)}")
print(f"Second item: {next(my_iterator)}")
print(f"Third item: {next(my_iterator)}")

print("\n--- 4. Hitting the end ---")
try:
    print(next(my_iterator))
except StopIteration:
    print("Caught a StopIteration! There are no more items left to fetch.")