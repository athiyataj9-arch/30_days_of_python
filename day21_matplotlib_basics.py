# ==========================================
# DAY 21: MATPLOTLIB BASICS 📊
# ==========================================
import matplotlib.pyplot as plt

# 1. LINE PLOT (Tracking progress over time)
days = [1, 2, 3, 4, 5, 6, 7]
confidence_level = [20, 35, 30, 50, 65, 80, 95]

plt.figure(figsize=(8, 5))
plt.plot(days, confidence_level, marker='o', color='green', linestyle='--', label='My Learning Curve')

# 2. ADDING LABELS & TITLES
plt.title("Learning Progress Over 7 Days", fontsize=14)
plt.xlabel("Day Number")
plt.ylabel("Confidence (%)")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# 3. SAVING THE PLOT
plt.savefig("learning_curve.png")
print("Line plot saved as learning_curve.png")
plt.show()

# 4. BAR CHART (Comparing categories)
categories = ['Lists', 'Dicts', 'NumPy', 'Pandas']
scores = [90, 85, 80, 75]

plt.bar(categories, scores, color=['blue', 'orange', 'green', 'red'])
plt.title("Topic Proficiency")
plt.show()