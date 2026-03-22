# Start with one value
score = 0
print(score)  # Shows: 0

# Change it
score = 10
print(score)  # Shows: 10

# Change it again
score = score + 5
print(score)  # Shows: 15

# Check different types
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>

# Check variables
age = 25
name = "Alice"
print(type(age))         # <class 'int'>
print(type(name))        # <class 'str'>

a = 123
b = 1_000_000
c = a + b
print(c)

# Single quotes
first = 'Python'

# Double quotes  
second = "Python"

# Triple quotes for multiple lines
paragraph = """This is
a multi-line
string"""
print(len(paragraph))

# Basic math
print(10 + 3)   # 13 - Addition
print(10 - 3)   # 7  - Subtraction
print(10 * 3)   # 30 - Multiplication
print(10 / 3)   # 3.333... - Division (always gives float)

# Special operators
print(10 // 3)  # 3  - Floor division (rounds down)
print(10 % 3)   # 1  - Modulo (remainder)
print(10 ** 3)  # 1000 - Exponent (power)

age = 18

print(age == 18)    # True  - Equal to
print(age != 21)    # True  - Not equal to
print(age > 17)     # True  - Greater than
print(age < 20)     # True  - Less than
print(age >= 18)    # True  - Greater than or equal
print(age <= 18)    # True  - Less than or equal

age = 25
has_license = True

# AND - both must be true
can_drive = age >= 16 and has_license
print(can_drive)  # True

# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False


first_name = "Jane"
last_name = "Doe"

# Using +
full_name = first_name + " " + last_name  # "Jane Doe"

# Using f-strings (modern Python way!)
greeting = f"Hello, {first_name}!"  # "Hello, Jane!"
print(greeting)

# Multiple variables
age = 25
intro = f"I'm {first_name} and I'm {age} years old"
print(intro)

for i in range(5):
    print("Hello!") 
    
numbers = [1, 2, 3, 4]
numbers = [num for num in numbers if num != 2]
print(numbers)