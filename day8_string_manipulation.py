# ==========================================
# DAY 8: STRING MANIPULATION 🧩
# ==========================================

# 1. STRING METHODS
raw_data = "  python for data science  "
print(f"Original: '{raw_data}'")
print(f"Cleaned: '{raw_data.strip().title()}'") # Removes spaces & capitalizes

# 2. SPLITTING & JOINING
# Useful for processing CSV-like strings.
tags = "python,ml,ai,data"
tag_list = tags.split(",")
print(f"List of tags: {tag_list}")
print(f"Rejoined: {' | '.join(tag_list)}")

# 3. ADVANCED F-STRINGS
# Formatting numbers for cleaner reports.
pi = 3.14159265
revenue = 5000000
print(f"\nPi to 2 decimals: {pi:.2f}")
print(f"Formatted Revenue: ${revenue:,}") # Adds commas for readability

# 4. SUBSTRING CHECKING
message = "Learning Data Science with Gemini"
print(f"Does it contain 'Data'? {'Data' in message}")

# End of Day 8 Script