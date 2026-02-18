# ==========================================
# DAY 2: LOOPS & FUNCTIONS 🔄
# ==========================================

# 1. FUNCTIONS (The Recipe)
# We define a task once and use it many times.
def daily_update(day_num, topic):
    print(f"Today is Day {day_num} and I am learning {topic}.")

print("--- [Section 1: Functions] ---")
daily_update(2, "Loops and Logic")

# 2. FOR LOOPS (The Repetition)
# Repeating a task a set number of times.
print("\n--- [Section 2: For Loops] ---")
for i in range(1, 4):
    print(f"Processing data point {i}...")

# 3. WHILE LOOPS (The Condition)
# Repeat as long as a condition stays True.
print("\n--- [Section 3: While Loops] ---")
energy = 3
while energy > 0:
    print(f"Coding... Energy left: {energy}")
    energy -= 1
print("Battery empty. Time to rest!")

# 4. RETURN KEYWORD
# Giving a result back to the main program.
def add_bonus(score):
    return score + 5

final_score = add_bonus(90)
print(f"\nFinal Score: {final_score}")

# End of Day 2 Script