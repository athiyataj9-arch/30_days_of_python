# ==========================================
# DAY 4: TUPLES & SETS 🔒 Elements
# ==========================================

# 1. TUPLES (The "Locked" List)
# Tuples are immutable - they cannot be changed after creation.
coordinates = (10.5, 20.0)
print(f"Coordinate Tuple: {coordinates}")
# coordinates[0] = 15.0  # This would cause an ERROR

# 2. SETS (The "Unique" Collection)
# Sets automatically remove duplicates and have no fixed order.
ids = {101, 102, 103, 101, 105}
print(f"\nUnique IDs (Duplicates removed): {ids}")

# 3. SET OPERATIONS (Math Logic)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Intersection: What do they share?
print(f"Shared items: {set_a.intersection(set_b)}")

# Union: Combine all unique items
print(f"All items combined: {set_a.union(set_b)}")

# Difference: What is in A but NOT in B?
print(f"Only in Set A: {set_a.difference(set_b)}")

# End of Day 4 Script