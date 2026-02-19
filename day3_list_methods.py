# ==========================================
# DAY 3: LISTS & LIST METHODS 📋
# ==========================================

# 1. CREATING A LIST
# A collection of items in a specific order.
fruits = ["apple", "banana", "cherry"]
print(f"Initial List: {fruits}")

# 2. ADDING ELEMENTS
fruits.append("orange")      # Adds to the end
fruits.insert(1, "mango")    # Adds at index 1
print(f"After Adding: {fruits}")

# 3. REMOVING ELEMENTS
fruits.pop()                 # Removes the last item
fruits.remove("banana")      # Removes specific item
print(f"After Removing: {fruits}")

# 4. SLICING (The "Pizza Cutter" technique)
# list[start : stop : step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nOriginal Numbers: {numbers}")
print(f"First three: {numbers[:3]}")
print(f"Middle section (3-7): {numbers[3:8]}")
print(f"Every second number: {numbers[::2]}")

# 5. NESTED LISTS (Matrix)
matrix = [[1, 2], [3, 4]]
print(f"\nNested Item (Row 1, Col 0): {matrix[1][0]}")

# End of Day 3 Script