# ==========================================
# DAY 27: SEARCH & MATH OPTIMIZATION 🔍
# ==========================================

# PROBLEM 1: BINARY SEARCH
# Challenge: Find the index of a target in a SORTED list.
# Efficiency: O(log n) time | O(1) space
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1        # Target is in the right half
        else:
            high = mid - 1       # Target is in the left half
            
    return -1 # Target not found

# PROBLEM 2: SQR(X)
# Challenge: Compute the square root of x without built-in functions.
# Hint: This is actually a Binary Search problem!
def my_sqrt(x):
    if x < 2: return x
    low, high = 2, x // 2
    
    while low <= high:
        mid = (low + high) // 2
        num = mid * mid
        if num == x: return mid
        if num > x: high = mid - 1
        else: low = mid + 1
    return high

# PROBLEM 3: EFFICIENT PRIME CHECK
# Challenge: Check if a number is prime.
# Optimization: Only check up to the square root of n.
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# --- Testing the Logic ---
sorted_list = [10, 20, 30, 40, 50, 60]
print(f"Index of 40: {binary_search(sorted_list, 40)}")
print(f"Square root of 16: {my_sqrt(16)}")
print(f"Is 29 prime? {is_prime(29)}")