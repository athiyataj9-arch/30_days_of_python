"""
Day 1: Variables & Data Types
Focus: Understanding how to store and identify information.
"""

# 1. THE FOUR CORE DATA TYPES
# ---------------------------
# String (str): For text. Must be inside quotes.
my_name = "Athiya" 

# Integer (int): For whole numbers.
my_age = 22 

# Float (float): For decimals.
my_score = 95.5 

# Boolean (bool): For True/False logic.
is_learning_python = True 

# 2. PRINTING AND FORMATTING
# ---------------------------
# f-strings (formatted strings) make it easy to mix text and variables.
print("--- Day 1 Results ---")
print(f"Name: {my_name}")
print(f"Age: {my_age}")
print(f"Current Score: {my_score}")
print(f"Learning Python? {is_learning_python}")

# 3. IDENTIFYING TYPES
# ---------------------------
# The type() function is like an X-ray; it tells you what data type a variable is.
print("\n--- Identifying Types ---")
print(f"Type of my_name: {type(my_name)}")
print(f"Type of my_age: {type(my_age)}")

# 4. TYPE CASTING (CONVERSION)
# ---------------------------
# Sometimes we need to change a data type to perform math.
# Example: Turning a string "10" into an actual number.
str_number = "10"
int_number = int(str_number)  # Converting string -> integer

print(f"\nMath result: {int_number + 5}") # Should output 15