# Operators

# Arithmetic Operators

print(5 + 3)  # Addition
print(5 - 3)  # Subtraction
print(5 * 3)  # Multiplication
print(5 / 3)  # Division
print(5 // 4)  # Integer Division
print(5 % 4)  # Modulus
print(5 ** 4)  # Power of operator

# Relational Operators

print(5 > 3)  # Greater than
print(5 < 3)  # Less than
print(5 == 3)  # Equal to
print(5 != 3)  # Not equal to
print(5 >= 3)  # Greater than or equal to
print(5 <= 3)  # Less than or equal to

# Logical Operators

print(1 and 0)  # Logical AND
print(1 or 0)  # Logical OR
print(not 1)  # Logical NOT

print(10 and 40) # 40
print(10 and 0) # 0
print(10 or 40) # 10
print(0 or 40) # 40
print(10 and False) # False

Why: In Python, and doesn’t return True or False. It returns one of its operands:

If the first value is falsy, and returns it right away.
Otherwise, it returns the second value.

# Bitwise Operators

print(5 & 3)  # Bitwise AND
print(5 | 3)  # Bitwise OR
print(5 ^ 3)  # Bitwise XOR
print(~5)  # Bitwise NOT 
print(5 << 1)  # Bitwise Left Shift
print(5 >> 1)  # Bitwise Right Shift

# Assignment Operators

a = 5
a += 3  # a = a + 3
print(a) # 8

x = "hello"
x+= "world"  # x = x + " world"
print(x) # helloworld

a %= 3  # a = a % 3
print(a) # 2

a **= 3  # a = a ** 3
print(a) # 8

# a++ ++a Python does not support the increment (++) or decrement (--) operators. Instead, you can use += 1 or -= 1 to achieve the same effect.

# Membership Operators

There are two membership operators in Python:  
1. in: Returns True if a value is found in the specified sequence
2. not in: Returns True if a value is not found in the specified sequence

print('S' in 'SieLabs')  # True
print('s' in 'SieLabs')  # False
print('L' not in 'SieLabs')  # False
print('x' not in 'SieLabs')  # True

numbers = [1, 2, 3]
print(1 in numbers)  # True
print(2 not in numbers)  # False

# Find the sum of 3 digit number entered by user

number = int(input("Enter a 3-digit number: "))
a = number % 10
number = number // 10

b = number % 10
number = number // 10

c = number % 10
print("The sum of the digits is:", a + b + c)

# IF-ELSE Statement

# Create login form for sielabs

email = input("Enter your email: ")
password = input("Enter your password: ")

# if(condition):
#     # code to execute if condition is true
# else:
#     # code to execute if condition is false

if(email == "admin@sielabs.com" and password == "123"):
    print("Login successful!")
else:
    print("Invalid email or password.")

INDENTATION: Python uses indentation to define blocks of code. The standard practice is to use 4 spaces for each level of indentation.

Question: 

if(email == "admin@sielabs.com" and password == "123"):
    print("Login successful!")
elif email == "user@sielabs.com" and password != "123":
    print("Incorrect password")
    password = input("Please try again: ")
    if password == "123":
        print("Login successful!")
    else:
        print("Beta tumse na ho payega")
else:
    print("Invalid email")

Question: # min of 3 numbers