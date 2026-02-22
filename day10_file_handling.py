# ==========================================
# DAY 10: FILE HANDLING BASICS 📂
# ==========================================

file_name = "practice.txt"

# 1. WRITING TO A FILE
# 'w' mode creates a new file or overwrites existing content.
with open(file_name, "w") as file:
    file.write("Hello! This is Day 10 of my Python journey.\n")
    file.write("I am learning how to handle files today.")
print(f"Successfully wrote to {file_name}")

# 2. READING FROM A FILE
# 'r' mode opens the file for reading.
print("\n--- Reading File Content ---")
with open(file_name, "r") as file:
    content = file.read()
    print(content)

# 3. APPENDING TO A FILE
# 'a' mode adds text to the end of the file.
with open(file_name, "a") as file:
    file.write("\nAppending this new line for practice.")

# 4. READING LINE BY LINE
print("\n--- Reading Line by Line ---")
with open(file_name, "r") as file:
    for line in file:
        print(f"Line data: {line.strip()}")

# End of Day 10 Script