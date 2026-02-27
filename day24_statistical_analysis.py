# ==========================================
# DAY 24: STATISTICAL DATA ANALYSIS 🧠
# ==========================================
import pandas as pd
import numpy as np
from scipy import stats

# Create a sample dataset of exam scores
scores = [88, 92, 78, 95, 89, 100, 72, 85, 91, 88, 84, 90]
df = pd.DataFrame(scores, columns=['Scores'])

# 1. MEASURES OF CENTRAL TENDENCY
print(f"Mean (Average): {df['Scores'].mean():.2f}")
print(f"Median (Middle): {df['Scores'].median()}")
print(f"Mode (Frequent): {df['Scores'].mode()[0]}")

# 2. MEASURES OF DISPERSION
print(f"Variance: {df['Scores'].var():.2f}")
print(f"Standard Deviation: {df['Scores'].std():.2f}")

# 3. PERCENTILES & QUARTILES
# 75th percentile means 75% of scores are below this value
print(f"75th Percentile: {np.percentile(scores, 75)}")

# 4. Z-SCORE (Detecting Outliers)
# A Z-score > 3 or < -3 is typically an outlier
df['Z-Score'] = stats.zscore(df['Scores'])
print("\nScores with Z-Scores:")
print(df.head())