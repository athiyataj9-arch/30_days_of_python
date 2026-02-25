# ==========================================
# DAY 18: HANDLING MISSING DATA 🔍
# ==========================================
import pandas as pd
import numpy as np

data = {
    'Revenue': [100, np.nan, 150, 200, np.nan],
    'Expenses': [80, 70, np.nan, 90, 60],
    'Branch': ['East', 'West', 'East', 'North', 'South']
}
df = pd.DataFrame(data)

# 1. CHECKING FOR NULLS
print("Null counts per column:")
print(df.isnull().sum())

# 2. DROPPING MISSING DATA
# Use this if the row is useless without the data
df_dropped = df.dropna(subset=['Revenue'])

# 3. FILLING MISSING DATA (Imputation)
# Filling Revenue with the Average
mean_rev = df['Revenue'].mean()
df['Revenue'] = df['Revenue'].fillna(mean_rev)

# Filling Expenses with a constant (0)
df['Expenses'] = df['Expenses'].fillna(0)

print("\nDataFrame after Imputation:")
print(df)