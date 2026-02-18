"""
Day 1 - Python Basics
Author: Athiya
Goal: Build strong Python foundation for Data Science
"""

print("Day 1 - Python Basics")


# 1. Variables

name = "Athiya"
age = 22
goal = "Data Scientist"

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"My goal is to become a {goal}.")


# 2. Data Types

integer_num = 10
float_num = 10.5
string_text = "Machine Learning"
is_learning = True

print("\nData Types:")
print(type(integer_num))
print(type(float_num))
print(type(string_text))
print(type(is_learning))


# 3. Lists

numbers = [1, 2, 3, 4, 5]
print("\nOriginal List:", numbers)

numbers.append(6)
print("Updated List:", numbers)


# 4. Loop

print("\nSquares of numbers:")
for num in numbers:
    print(num ** 2)

# 5. Function

def greet(person):
    return f"Keep going, {person}! Consistency is key 💚"

print("\nFunction Output:")
print(greet("Athiya"))
