# ==========================================
# DAY 22: SCATTER PLOTS & HISTOGRAMS 🎯
# ==========================================
import matplotlib.pyplot as plt
import numpy as np

# 1. SCATTER PLOT (Correlation between two variables)
# Generating random data: Hours Studied vs Exam Score
hours = np.random.normal(5, 2, 50)
scores = hours * 15 + np.random.normal(0, 10, 50)

plt.scatter(hours, scores, alpha=0.7, color='purple')
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.show()

# 2. HISTOGRAM (Distribution of a single variable)
# Generating data with a normal distribution
data = np.random.normal(100, 15, 500)

plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of IQ Scores")
plt.xlabel("IQ Value")
plt.ylabel("Frequency")
plt.show()

# 3. SUBPLOTS (Putting multiple charts in one window)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot([1, 2, 3], [1, 4, 9])
ax1.set_title("Plot 1")

ax2.bar(['A', 'B'], [10, 20])
ax2.set_title("Plot 2")

plt.tight_layout()
plt.show()