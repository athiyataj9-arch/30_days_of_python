# ==========================================
# DAY 9: LIST COMPREHENSIONS ⚡
# ==========================================

# 1. BASIC COMPREHENSION
# Goal: Create a list of squares for numbers 0-9
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# 2. WITH CONDITIONALS (Filtering)
# Goal: Get only even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(f"Evens only: {evens}")

# 3. WITH IF-ELSE (Transformation)
# Goal: Label numbers as 'Even' or 'Odd'
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(f"Labels: {labels}")

# 4. STRING PROCESSING
names = ["athiya", "python", "data"]
caps = [name.upper() for name in names]
print(f"Uppercased: {caps}")

# End of Day 9 Script