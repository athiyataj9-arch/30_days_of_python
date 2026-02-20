# ==========================================
# DAY 6: CONDITIONAL STATEMENTS 🚦
# ==========================================

# 1. IF-ELIF-ELSE LOGIC
score = 85

print(f"Checking Grade for Score: {score}")
if score >= 90:
    print("Grade: A+ 🏆")
elif score >= 80:
    print("Grade: A 🌟")
elif score >= 70:
    print("Grade: B 👍")
else:
    print("Grade: Keep Practicing! 💪")

# 2. LOGICAL OPERATORS (and, or, not)
has_laptop = True
has_internet = True

if has_laptop and has_internet:
    print("\nYou are ready to code!")

# 3. NESTED CONDITIONALS
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive to the data center.")
    else:
        print("You are old enough, but need a license.")

# End of Day 6 Script