print("--- 1. Demonstrating 'break' ---")

for i in range(1, 6):
    if i == 3:
        print("Encountered break! Stopping the loop.")
        break
    print(f"Number: {i}")

print("\n--- 2. Demonstrating 'continue' ---")
for j in range(1, 6):
    if j == 3:
        print("Encountered continue! Skipping number 3.")
        continue
    print(f"Number: {j}")

print("\n--- 3. Demonstrating 'pass' ---")
for k in range(1, 6):
    if k == 3:
        pass  # Placeholder: No action taken, loop proceeds normally
        print("Encountered pass! Doing nothing and proceeding.")
    print(f"Number: {k}")