# ==========================================
# DAY 13: NUMPY BASICS 🔢
# ==========================================
import numpy as np

# 1. CREATING ARRAYS
# Arrays are faster and more memory-efficient than Python lists.
arr = np.array([1, 2, 3, 4, 5])
print(f"1D Array: {arr}")
print(f"Shape: {arr.shape} | Data Type: {arr.dtype}")

# 2. MULTI-DIMENSIONAL ARRAYS (Matrices)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D Matrix:\n{matrix}")
print(f"Dimensions: {matrix.ndim}")

# 3. HELPER FUNCTIONS
zeros = np.zeros((2, 3))    # 2 rows, 3 columns of 0s
ones = np.ones((3, 2))      # 3 rows, 2 columns of 1s
sequence = np.arange(0, 10, 2) # Start, Stop, Step
print(f"\nZeros Matrix:\n{zeros}")
print(f"Sequence: {sequence}")

# 4. BASIC INDEXING
print(f"\nElement at Row 0, Col 1: {matrix[0, 1]}")