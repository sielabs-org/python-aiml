num1 = input("Enter first number: ")
num2 = input("Enter first number: ")

result = int(num1) + int(num2)
print(result)

print(type(num1))

Jab type convertion hota hai to python new object banata hai instead of changing in that object itself.

======

print(4+'4')

TypeError: unsupported operand type(s) for +: 'int' and 'str'

Implicit VS Explicite

implicit: print(5+5.6)

explicite: 

1. print(type(int('5)))

2. print(int(4.5))
=> 4

3. print(int(4+5j))
=> TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

4. str(5)

5. float(4)

# Literals

a = 2
a = variable, = = is operator and 2 is literal

1. binary
a = 0b1010
print(a)
=> 10

# Decimal Literal
b = 100  

# Octal Literal
c = 0o310 

# Octal Literal
d = 0x12c #Hexadecimal Literal

print(b,c,d)
=> 100 200 300

# Float Literal

float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3

# Complex Literal
x = 1+4j
y = 5.5j;
print(x.real,x.imag)

x = 1+4j
y = 5.5j;
print(x.real,x.imag)
print(y)
=> 1.0 4.0
5.5j

# String Literal

strings = 'Elon'
strings = "Elon'
char = "B"

print("\n")
=> 

print(r"\n")

# Boolean Literal
a = True + 4
b = False + 10

print("a:", a)
print("b:", b)

# None Literal

a
b = 5
c = 10
print("hello")

python error dega so use a = None

a = None
print(a)

