# 1. Global Variable: Defined outside any function
name = "Global"

def outer_function():
    # 2. Local Variable: Defined inside a function (acts as enclosing scope for inner_function)
    name = "Local (Outer Function)"
    print(f"Inside outer_function (before inner): {name}")
    
    def inner_function():
        # 3. Nonlocal Keyword: Modifies the variable in the nearest enclosing scope (outer_function)
        nonlocal name
        name = "Nonlocal (Modified by Inner Function)"
        print(f"Inside inner_function: {name}")
        
    inner_function()
    # The value here is changed because of the 'nonlocal' keyword inside inner_function
    print(f"Inside outer_function (after inner): {name}")

def modify_global():
    # Global Keyword: Tells Python we want to modify the global variable, not create a local one
    global name
    name = "Global (Modified)"
    print(f"\nInside modify_global: {name}")


# Execution starts here
print(f"Starting value: {name}\n")

print("--- Testing Local and Nonlocal ---")
outer_function()

print("\n--- Testing Global ---")
print(f"Global value before modify_global: {name}")
modify_global()
print(f"Global value after modify_global: {name}")