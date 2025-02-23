import random
import string

def generate_password(name, dob, special_char):
    if len(name) < 5:
        raise ValueError("Name must be at least 5 characters long")
    
    year = dob.split('-')[0]
    month = dob.split('-')[1]
    day = dob.split('-')[2]
    
    unit_digits = int(year[-1]) + int(month[-1]) + int(day[-1])
    
    if unit_digits > 10:
        unit_digits = sum(int(digit) for digit in str(unit_digits))
    
    name_part = name[:5]
    
    password = name_part + special_char + str(unit_digits)
    
    return password

name = input("Enter your name : ")
dob = input("Enter your date of birth (YYYY-MM-DD): ")
special_char = input("Enter a special character: ")

try:
    password = generate_password(name, dob, special_char)
    print("Generated password:", password)
except ValueError as e:
    print(e)


#output

# Enter your name : mounika
# Enter your date of birth (YYYY-MM-DD): 2004-04-14
# Enter a special character: @
# Generated password: mouni@3
