# ==========================================
# DAY 20: MERGING & JOINING 🔗
# ==========================================
import pandas as pd

# DataFrame 1: Employee Info
emp_df = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'name': ['Athiya', 'John', 'Sarah', 'Mike']
})

# DataFrame 2: Salary Info
sal_df = pd.DataFrame({
    'emp_id': [1, 2, 3, 5],
    'salary': [5000, 6000, 4500, 7000]
})

# 1. INNER JOIN (Only matches found in both)
inner_join = pd.merge(emp_df, sal_df, on='emp_id', how='inner')
print("Inner Join (Only matching IDs):")
print(inner_join)

# 2. LEFT JOIN (All from emp_df, matches from sal_df)
left_join = pd.merge(emp_df, sal_df, on='emp_id', how='left')
print("\nLeft Join (All employees, even without salary data):")
print(left_join)

# 3. CONCATENATION (Stacking data on top of each other)
# df_combined = pd.concat([df1, df2], axis=0)