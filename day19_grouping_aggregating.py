# ==========================================
# DAY 19: GROUPING & AGGREGATING 📊
# ==========================================
import pandas as pd

data = {
    'Department': ['HR', 'IT', 'IT', 'HR', 'Sales', 'Sales', 'IT'],
    'Employee': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'Salary': [50000, 70000, 80000, 55000, 60000, 65000, 75000],
    'Experience': [2, 5, 8, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

# 1. GROUP BY SINGLE COLUMN
dept_salaries = df.groupby('Department')['Salary'].mean()
print("Average Salary by Department:")
print(dept_salaries)

# 2. MULTIPLE AGGREGATIONS
# Finding min, max, and sum at once
stats = df.groupby('Department')['Salary'].agg(['min', 'max', 'sum'])
print("\nSalary Stats by Department:")
print(stats)

# 3. GROUPING BY MULTIPLE COLUMNS (Hypothetical)
# df.groupby(['Region', 'Department'])['Salary'].mean()