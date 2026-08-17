# Mutable object
print("\n------Mutable Object----------")
list1 = [10, 20, 30]
print("Original list:", list1)

list1[0] = 100
print("After changing first element:", list1)

# Immutable object
print("\n------Immutable Object--------")
tuple1 = (10, 20, 30)
print("Original tuple:", tuple1)

try:
    tuple1[0] = 100
    
except TypeError:
    print('changing for index [0]')
    print("Tuple cannot be changed because it is immutable")
