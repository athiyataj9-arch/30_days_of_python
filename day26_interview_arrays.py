# ==========================================
# DAY 26: ARRAY INTERVIEW CHALLENGES 📋
# ==========================================

# PROBLEM 1: TWO SUM
# Challenge: Find indices of two numbers that add up to a specific target.
# Optimal: O(n) using a Hash Map (Dictionary)
def two_sum(nums, target):
    prev_map = {} # val : index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return []

# PROBLEM 2: MOVE ZEROES
# Challenge: Move all 0's to the end of the array while maintaining order.
# Constraint: Must do this in-place (without making a new list).
def move_zeroes(nums):
    # 'l' is the position to place the next non-zero element
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    return nums

# PROBLEM 3: FIND THE MISSING NUMBER
# Challenge: Given a list containing n distinct numbers in range [0, n], 
# return the only number in the range that is missing.
def find_missing(nums):
    n = len(nums)
    # The sum of first n numbers is (n * (n + 1)) / 2
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# --- Testing the Logic ---
print(f"Two Sum [2,7,11,15] Target 9: {two_sum([2, 7, 11, 15], 9)}")
print(f"Move Zeroes [0,1,0,3,12]: {move_zeroes([0, 1, 0, 3, 12])}")
print(f"Missing Number in [3,0,1]: {find_missing([3, 0, 1])}") # Expect 2