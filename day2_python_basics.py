"""
Day 2 - Python Control Flow & Logic
Author: Athiya
Goal: Mastering decision-making and loops for data processing.
"""

print("--- Day 2: Control Flow & Logic ---")

# 1. Conditionals (if-elif-else)
# Simulating a simple data quality check
data_value = 85

print("\n[1] Data Validation:")
if data_value > 100:
    print(f"Alert: {data_value} is an outlier.")
elif data_value < 0:
    print(f"Error: {data_value} is a negative value.")
else:
    print(f"Confirmed: {data_value} is within the normal range.")


# 2. For Loops
# Iterating through a list (simulating processing a dataset)
measurements = [1.2, 3.5, 0.8, 5.2, 2.1]
scaled_measurements = []

print("\n[2] Processing Dataset:")
for val in measurements:
    # Applying a scaling factor
    scaled_measurements.append(round(val * 10, 2))

print(f"Original: {measurements}")
print(f"Scaled:   {scaled_measurements}")


# 3. While Loops
# Useful for processes that run until a target is reached
threshold = 0
limit = 3
print("\n[3] System Initialization:")
while threshold < limit:
    threshold += 1
    print(f"Loading component... {threshold}/{limit}")
print("System Ready.")


# 4. Logic Gates in Practice
# Combining loops and conditionals to filter data
raw_data = [12, 45, 7, 89, 32, 56, 4, 10]
filtered_data = []

print("\n[4] Data Filtering:")
for num in raw_data:
    if num > 20 and num % 2 == 0:
        filtered_data.append(num)

print(f"Items > 20 and Even: {filtered_data}")