
name = "Global"

def outer_function():
    #Local Variable: Defined inside a function (acts as enclosing scope for inner_function)
    name = "Local (Outer Function)"
    print(f"Inside outer_function (before inner): {name}")
    
    def inner_function():
        #Nonlocal Keyword: Modifies the variable in the nearest enclosing scope (outer_function)
        nonlocal name
        name = "Nonlocal (Modified by Inner Function)"
        print(f"Inside inner_function: {name}")
        
    inner_function()
    print(f"Inside outer_function (after inner): {name}")

def modify_global():
    global name
    name = "Global (Modified)"
    print(f"\nInside modify_global: {name}")


print(f"Starting value: {name}\n")

print("--- Testing Local and Nonlocal ---")
outer_function()

print("\n--- Testing Global ---")
print(f"Global value before modify_global: {name}")
modify_global()
print(f"Global value after modify_global: {name}")
