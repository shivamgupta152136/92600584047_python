
number = int(input("Enter a number: "))


temp = abs(number)
sum_of_digits = 0


while temp > 0:
    digit = temp % 10              
    sum_of_digits += digit         
    temp = temp // 10              

print(f"The sum of the digits is: {sum_of_digits}")