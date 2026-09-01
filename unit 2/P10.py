def generate_evens(limit):
    print("[Generator Started]")
    number = 2
    
    while number <= limit:
        yield number
        number += 2
        
    print("[Generator Finished]")

print("--- Creating the Generator ---")
even_sequence = generate_evens(8)
print("Generator object created successfully.")

print("\n--- Fetching Numbers from the Generator ---")
for num in even_sequence:
    print(f"Received: {num}")