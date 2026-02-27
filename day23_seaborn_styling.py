# ==========================================
# DAY 23: SEABORN VISUALIZATION 🎨
# ==========================================
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set the style to look professional
sns.set_theme(style="whitegrid")

# 1. LOAD A BUILT-IN DATASET
tips = sns.load_dataset("tips")

# 2. VIOLIN PLOT (Shows distribution & density)
plt.figure(figsize=(8, 5))
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True)
plt.title("Bill Distribution by Day and Gender")
plt.show()

# 3. HEATMAP (Visualizing correlations)
# Great for seeing which variables move together
corr = tips.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 4. PAIR PLOT (The 'Magic' Command)
# Shows relationships between every single numeric variable
# sns.pairplot(tips, hue="time")
# plt.show()