# ==========================================
# DAY 5: DICTIONARIES 📖
# ==========================================

# 1. CREATING A DICTIONARY
# Storing data in Key:Value pairs (like a real dictionary).
student = {
    "name": "Athiya",
    "course": "Data Science",
    "progress": 75,
    "is_certified": False
}
print(f"Student Profile: {student}")

# 2. ACCESSING & UPDATING
# Using keys to get or change information.
print(f"Name: {student['name']}")
student["progress"] = 80  # Updating value
student["city"] = "Mumbai" # Adding new key-value pair

# 3. DICTIONARY METHODS
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")

# 4. LOOPING THROUGH DICTIONARIES
print("\n--- Iterating through data ---")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")

# End of Day 5 Script