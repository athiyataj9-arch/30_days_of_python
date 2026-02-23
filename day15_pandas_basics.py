# ==========================================
# DAY 15: PANDAS BASICS 🐼
# ==========================================
import pandas as pd

# 1. SERIES (1D Data)
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("Pandas Series:")
print(s)

# 2. DATAFRAMES (2D Data)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

# 3. QUICK INSPECTION
print("\nFirst 2 rows:")
print(df.head(2))
print(f"\nColumns: {df.columns.tolist()}")
print(f"Summary Statistics:\n{df.describe()}")