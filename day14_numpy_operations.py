# ==========================================
# DAY 14: NUMPY OPERATIONS ⚡
# ==========================================
import numpy as np

arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])

# 1. ELEMENT-WISE MATH (Vectorization)
print(f"Addition: {arr1 + arr2}")
print(f"Multiplication: {arr1 * arr2}")

# 2. STATISTICAL FUNCTIONS
data = np.array([1, 5, 8, 12, 20])
print(f"\nData: {data}")
print(f"Mean: {np.mean(data)}")
print(f"Standard Deviation: {np.std(data):.2f}")
print(f"Sum: {np.sum(data)}")

# 3. RESHAPING DATA
# Changing 1D (6 elements) to 2D (2x3)
grid = np.arange(6).reshape(2, 3)
print(f"\nReshaped Grid:\n{grid}")

# 4. BROADCASTING
# Adding a single number to every element in an array
print(f"\nAdding 10 to all: {arr1 + 10}")