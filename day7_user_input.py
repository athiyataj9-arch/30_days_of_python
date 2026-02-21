# ==========================================
# DAY 7: USER INPUT & TYPE CASTING 📥
# ==========================================

# 1. TAKING BASIC INPUT
# input() always returns data as a STRING.
user_name = input("Enter your name: ")
print(f"Welcome to the team, {user_name}!")

# 2. TYPE CASTING INPUT
# We must convert the string to an int or float to do math.
birth_year = input("Enter your birth year: ")
age = 2026 - int(birth_year)  # Converting str -> int
print(f"You are approximately {age} years old.")

# 3. INPUT VALIDATION (Simple)
# Checking if input is numeric before processing.
price_input = input("\nEnter the product price: ")
if price_input.replace('.', '', 1).isdigit():
    price = float(price_input)
    print(f"Price with 10% tax: {price * 1.1:.2f}")
else:
    print("Invalid input. Please enter a number.")

# End of Day 7 Script