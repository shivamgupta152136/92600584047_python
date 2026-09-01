print("--- 1. List Comprehension (with condition) ---")
even_squares_list = [x * x for x in range(1, 11) if x % 2 == 0]
print(f"Even squares list: {even_squares_list}")


print("\n--- 2. Set Comprehension ---")
words = ["hello", "world", "python", "code", "loops", "code"]
unique_lengths = {len(word) for word in words}
print(f"Unique word lengths: {unique_lengths}")


print("\n--- 3. Dictionary Comprehension ---")
word_dict = {word: word.upper() for word in words}
print(f"Word mapping dictionary:\n{word_dict}")