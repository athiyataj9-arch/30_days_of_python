# ==========================================
# DAY 16: DATA SELECTION 🎯
# ==========================================
import pandas as pd

data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
    'Price': [1200, 800, 450, 300],
    'Stock': [15, 50, 25, 10]
}
df = pd.DataFrame(data)

# 1. SELECTING COLUMNS
print("Prices only:")
print(df['Price'])

# 2. SELECTING BY LOCATION (iloc & loc)
print(f"\nFirst row data:\n{df.iloc[0]}") # Integer-based
print(f"\nProduct at index 2: {df.loc[2, 'Product']}") # Label-based

# 3. CONDITIONAL FILTERING (Crucial for Data Cleaning)
# Find products where Price > 500
expensive_items = df[df['Price'] > 500]
print("\nExpensive Items (>500):")
print(expensive_items)

# 4. MULTIPLE CONDITIONS
# Price > 500 AND Stock > 20
target = df[(df['Price'] > 500) & (df['Stock'] > 20)]
print("\nHigh Price & High Stock:")
print(target)