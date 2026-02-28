# ==========================================
# DAY 25: STRING INTERVIEW CHALLENGES 🔠
# ==========================================

# PROBLEM 1: VALID PALINDROME
# Challenge: Check if a string is a palindrome, ignoring case and non-alphanumeric chars.
# Example: "A man, a plan, a canal: Panama" -> True
def is_palindrome(s):
    # Filter: keep only letters and numbers, then lowercase
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    # Compare with its reverse
    return clean_s == clean_s[::-1]

# PROBLEM 2: VALID ANAGRAM
# Challenge: Given two strings, return True if they are anagrams of each other.
# Example: "silent", "listen" -> True
def are_anagrams(s1, s2):
    # Anagrams must have the same characters in the same frequency
    # Sorting is the easiest way to check this (O(n log n))
    return sorted(s1.lower()) == sorted(s2.lower())

# PROBLEM 3: FIRST UNIQUE CHARACTER
# Challenge: Find the index of the first non-repeating character.
# Example: "leetcode" -> 'l' is at index 0
def first_unique_char(s):
    count = {}
    # Build frequency map
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    # Find the first char with count of 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

# --- Testing the Logic ---
print(f"Is 'Racecar' a palindrome? {is_palindrome('Race Car')}")
print(f"Are 'Heart' and 'Earth' anagrams? {are_anagrams('Heart', 'Earth')}")
print(f"First unique index in 'swiss': {first_unique_char('swiss')}") # 'w' at index 1