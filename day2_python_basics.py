"""
Day 2: Loops & Functions
Focus: Automating repetitive tasks and creating reusable code.
"""

# 1. FUNCTIONS (The "Recipe")
# ---------------------------
# 'def' tells Python we are defining a function.
# 'username' is a placeholder (parameter).
def greet_user(username):
    """This function takes a name and prints a welcome message."""
    print(f"Hello {username}, welcome to Day 2!")

# We "call" the function to run it:
print("--- [Section 1: Functions] ---")
greet_user("Athiya")


# 2. THE 'FOR' LOOP (The Counter)
# ---------------------------
# Use this when you want to do something a specific number of times.
print("\n--- [Section 2: For Loops] ---")
print("Counting steps:")
for step in range(1, 4):  # range(1, 4) gives us 1, 2, and 3
    print(f"Step {step} completed! ✅")


# 3. THE 'WHILE' LOOP (The Condition)
# ---------------------------
# Use this when you want to repeat until a condition is met.
print("\n--- [Section 3: While Loops] ---")
battery_life = 3
while battery_life > 0:
    print(f"Phone is ON. Battery at {battery_life}%")
    battery_life -= 1 # Decreasing battery so the loop stops eventually
print("Phone shut down. 🪫")


# 4. THE 'RETURN' KEYWORD
# ---------------------------
# 'return' gives a result back to the main program instead of just printing it.
def add_bonus(current_score):
    return current_score + 10

final_result = add_bonus(90)
print(f"\nFinal Score after bonus: {final_result}")