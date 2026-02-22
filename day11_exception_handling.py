# ==========================================
# DAY 11: EXCEPTION HANDLING 🛡️
# ==========================================

# 1. BASIC TRY-EXCEPT
# Preventing the program from crashing on user error.
try:
    number = int(input("Enter a number to divide 100: "))
    result = 100 / number
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a valid integer, not text.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

# 2. THE 'ELSE' AND 'FINALLY' BLOCKS
try:
    file = open("day11_test.txt", "w")
    file.write("Testing exception handling.")
except IOError:
    print("Error: Could not write to file.")
else:
    print("\nFile written successfully!")
finally:
    # This block runs no matter what happens
    if 'file' in locals():
        file.close()
        print("File resource closed.")

# 3. RAISING CUSTOM EXCEPTIONS
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return f"Age set to {age}"

try:
    print(check_age(-5))
except ValueError as e:
    print(f"Custom Error: {e}")

# End of Day 11 Script