# ==========================================
# DAY 17: DATA CLEANING 🧹
# ==========================================
import pandas as pd

data = {
    'ID': [101, 102, 102, 104, 105],
    'Name': ['Alice', 'Bob', 'Bob', 'Charlie', 'Alice'],
    'Score': [85, 90, 90, None, 88]
}
df = pd.DataFrame(data)

# 1. IDENTIFYING DUPLICATES
print(f"Duplicate rows count: {df.duplicated().sum()}")

# 2. REMOVING DUPLICATES
# keep='first' is default; it keeps the first occurrence.
df_clean = df.drop_duplicates()
print("\nAfter removing duplicates:")
print(df_clean)

# 3. RENAMING COLUMNS
df_clean = df_clean.rename(columns={'Score': 'Final_Exam', 'Name': 'Student_Name'})

# 4. STRING CLEANING IN COLUMNS
# Imagine names had leading/trailing spaces
df_clean['Student_Name'] = df_clean['Student_Name'].str.strip().str.upper()
print("\nCleaned and Renamed DataFrame:")
print(df_clean)